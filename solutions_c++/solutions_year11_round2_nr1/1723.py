/*
 * Olaf "Ritave" Tomalka
 * GCJ 2011
 */
#include <iostream>
#include <vector>

const char Won='1';
const char Lost='0';
const char NotPlayed='.';

struct Team
{
	int Won;
	int Total;
	double OWP,OOWP;
};

void DoTest()
{
	std::vector<std::vector<char>> Plays;
	std::vector<Team> T;
	int n;
	std::cin >> n;
	{
		std::vector<char> Temp;
		Temp.resize(n,NotPlayed);
		Plays.resize(n,Temp);
		T.resize(n);
	}
	// Read in, and calculate WP
	for (int i=0;i<n;i++)
	{
		for (int j=0;j<n;j++)
		{
			std::cin >> Plays[j][i];
			if (Plays[j][i]==Won)
			{
				T[i].Won++;
				T[i].Total++;
			} else if (Plays[j][i]==Lost)
				T[i].Total++;
		}
	}

	// Calculate OWP
	for (int i=0;i<n;i++)
	{
		double OWPHelper=0;
		int Divisor=n;
		for (int j=0;j<n;j++)
		{
			if (Plays[i][j]==Won)
				OWPHelper+=(double(T[j].Won-1)/double(T[j].Total-1));
			else if (Plays[i][j]==Lost)
				OWPHelper+=(double(T[j].Won)/double(T[j].Total-1));
			else
				Divisor--;
		}
		if (Divisor==0)
			T[i].OWP=0;
		else
			T[i].OWP=OWPHelper/double(Divisor);
	}

	// Calculate OOWP
	for (int i=0;i<n;i++)
	{
		double OOWPHelper=0;
		int Divisor=n;
		for (int j=0;j<n;j++)
		{
			if (Plays[j][i]!=NotPlayed)
			{
				OOWPHelper+=T[j].OWP;
			} else
				Divisor--;
		}
		if (Divisor==0)
			T[i].OOWP=0;
		else
			T[i].OOWP=OOWPHelper/double(Divisor);
	}
	
	// Calculate RPI
	for (int i=0;i<n;i++)
	{
		double RPI=0;
		if (T[i].Total!=0)
			RPI=(0.25*(double(T[i].Won)/double(T[i].Total)))+(0.5*T[i].OWP)+(0.25*T[i].OOWP);
		std::cout << RPI << '\n';
	}

	// End of stupid shortcuts
}

int main()
{
	std::ios::sync_with_stdio(false);
	std::cin.tie(false);
	std::cout.precision(12);
	int t;
	std::cin >> t;
	for (int i=1;i<=t;i++)
	{
		std::cout << "Case #" << i << ":\n";
		DoTest();
	}
	//std::system("PAUSE");
}