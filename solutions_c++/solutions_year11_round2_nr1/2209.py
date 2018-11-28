#include <iostream>
#define WIN '1'
#define LOSE '0'
#define NOTHING '.'

using namespace std;

typedef struct tag_team
{
	string games;
	double wp, owp, oowp;
	double nwins, nloses;
	
	void calcWP()
	{
		wp = 0;
		nwins = nloses = 0;
		for (unsigned int i=0; i < games.size(); i++)
		{
			if (games[i] == WIN) nwins++;
			else if (games[i] == LOSE) nloses++;
		}
		if (nwins || nloses) wp = nwins / (nwins + nloses);
		//cout << "wp: " << wp << endl;
	}
	
	void calcOWP(tag_team others[])
	{
		owp = 0;
		int noponents = 0;
		for (unsigned int i=0; i<games.size(); i++)
		{
			if (games[i] != NOTHING){
				noponents++;
				double xwins = others[i].nwins;
				double xloses = others[i].nloses;
				if (games[i] == WIN) xloses--;
				else xwins--;
				if (xwins || xloses)
				{
					owp += xwins / (xwins + xloses);
					
				}
			}
		}
		owp /= noponents;
		//cout << "owp: " << owp << endl;
	}
	
	void calcOOWP(tag_team others[])
	{
		oowp = 0;
		int noponents = 0;
		for (unsigned int i=0; i<games.size(); i++)
		{
			if (games[i] != NOTHING)
			{
				noponents++;
				oowp += others[i].owp;
			}
		}
		oowp /= noponents;
		//cout << "oowp: " << oowp << endl;
	}
	
	double calcRPI()
	{
		return (0.25 * wp) + (0.5 * owp) + (0.25 * oowp);
	}
}
team;

int main()
{
	int ccase = 0, ncases;
	cin >> ncases;
	cout.precision(12);
	while (ccase++ < ncases)
	{
		int nteams;
		cin >> nteams;
		team teams[nteams];
	
		for (int i=0; i<nteams; i++) cin >> teams[i].games;		
		for (int i=0; i<nteams; i++) teams[i].calcWP();
		for (int i=0; i<nteams; i++) teams[i].calcOWP(teams);
		for (int i=0; i<nteams; i++) teams[i].calcOOWP(teams);
	
		cout << "Case #" << ccase << ":" << endl;
		for (int i=0; i<nteams; i++) cout << teams[i].calcRPI() << endl;
	}
	
	return 0;
}
