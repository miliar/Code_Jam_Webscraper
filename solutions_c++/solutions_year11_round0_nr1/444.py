#include <iostream>
#include <fstream>
using namespace std;

int AllSequence[100];
char CSequence[100];

int Search(char c,int place)
{
	if (c=='B')
	{
		for (int i=place;i<=99;i++)
		{
			if (CSequence[i]=='B')
			{
				return AllSequence[i];
			}
		}
		return 0;
	}
	else
	{
		for (int i=place;i<=99;i++)
		{
			if (CSequence[i]=='O')
			{
				return AllSequence[i];
			}
		}
		return 0;
	}
}

int main()
{
	int T;
	int BluePlace;
	int OrangePlace;
	int AllStep;
	int NextB;
	int NextO;
	int N;

	int Time;
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("Alarge.txt");
	fin>>T;
	for (int i=1;i<=T;i++)
	{
		fin>>N;	
		for (int j=0;j<N;j++)
		{
			fin>>CSequence[j];
			fin>>AllSequence[j];

		}
		BluePlace=1;
		OrangePlace=1;
		AllStep=-1;
		Time=0;
		while (AllStep!=N-1)
		{
			NextB=Search('B',AllStep+1);
			NextO=Search('O',AllStep+1);
			if (CSequence[AllStep+1]=='B')
			{
				if (NextO==0)
				{
					
				}
				else
				{
					if (abs(NextB-BluePlace)+1<abs(NextO-OrangePlace))
					{
						if (NextO>=OrangePlace)
						{
							OrangePlace=OrangePlace+abs(NextB-BluePlace)+1;
						}
						else
						{
							OrangePlace=OrangePlace-abs(NextB-BluePlace)-1;
						}
					}
					else
					{
						OrangePlace=NextO;
					}
				}
				Time=Time+abs(NextB-BluePlace)+1;
				BluePlace=NextB;
				AllStep++;
			}
			else
			{
				if (NextB==0)
				{
					
				}
				else
				{
					if (abs(NextO-OrangePlace)+1<abs(NextB-BluePlace))
					{
						if (NextB>=BluePlace)
						{
							BluePlace=BluePlace+abs(NextO-OrangePlace)+1;
						}
						else
						{
							BluePlace=BluePlace-abs(NextO-OrangePlace)-1;
						}
					}
					else
					{
						BluePlace=NextB;
					}
				}
				Time=Time+abs(NextO-OrangePlace)+1;
				OrangePlace=NextO;
				AllStep++;
			}
		}
		fout<<"Case #"<<i<<": "<<Time<<endl;
	}
	return 0;
}