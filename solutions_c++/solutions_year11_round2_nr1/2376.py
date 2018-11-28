#include <math.h>
#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

#define MAX_CASES 20

class Record{
	char record[100];
	int numberOf;
public:

	Record(){
		numberOf=3;
	}

	char GetChar(int i)
	{
		return record[i];
	}

	void SetRecord(char *inRecord, int noOfOthers)
	{
		for (int i=0;i<noOfOthers;i++)
		{
			record[i]=inRecord[i];
		}
		numberOf=noOfOthers;
	}

	float GetWP()
	{
		int numberOfGames=0,numberOfWins=0;

		for (int i=0;i<numberOf;i++)
		{
			if (record[i]=='1')
			{
				numberOfGames++;
				numberOfWins++;
			}
			if (record[i]=='0')
			{
				numberOfGames++;
			}
		}
		return (float)numberOfWins/(float)numberOfGames;
	}

	float GetOWP(int excluding)
	{
		int numberOfGames=0,numberOfWins=0;

		for (int i=0;i<numberOf;i++)
		{
			if (i!=excluding)
			{
				if (record[i]=='1')
				{
					numberOfGames++;
					numberOfWins++;
				}
				if (record[i]=='0')
				{
					numberOfGames++;
				}
			}
		}
		return (float)numberOfWins/(float)numberOfGames;
	}
};

class Team{
	Record tRecord;
	float WP,OWP,OOWP;
	int others;

	float RPI;

public:
	Team(){
		OWP=OOWP=0;
		others=0;
	}

	bool PlayedThis(int i)
	{
		if (tRecord.GetChar(i)=='.') return false;
		return true;
	}

	void SetRecord(char *inRecord, int noOfOthers)
	{
		tRecord.SetRecord(inRecord,noOfOthers);
		OWP=OOWP=0;
		others=0;
	}

	float GetWP()
	{
		WP=tRecord.GetWP();
		return WP;
	}

	void AddOWP(float inOWP)
	{
		OWP=OWP+inOWP;
		others++;
	}

	void AddOOWP(float inOOWP)
	{
		OOWP=OOWP+inOOWP;
	}

	float GetOWP(int exc)
	{
		return tRecord.GetOWP(exc);
	}
	void SetTOWP(){
		OWP=OWP/(float)others;
	}

	float GetTOWP(){
		return OWP;
	}
	void SetOOWP(){
		OOWP=OOWP/(float)others;
	}

	float GetOOWP(){
		return OOWP;
	}
	float GetRPI()
	{
		return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP;
	}
};

int main() {
	ifstream in("inputFile.inp");
	ofstream out("outputFile.out");

	int number, T, candy;
	char rec[100];

	Team team[MAX_CASES];

	in>>T;
	for (int i=0;i<T;i++)
	{
		cout << "Case #"<<i+1 <<endl;
		in>>number;
		cout << number <<endl;
		for (int j=0;j<number;j++)
		{
			in>>rec;
			team[j].SetRecord(rec,number);
			cout <<team[j].GetWP() <<" ";
		}
		cout <<endl;

		for (int j=0;j<number;j++)
		{
			for (int k=0;k<number;k++)
			{
				if (team[j].PlayedThis(k))
				{
					team[j].AddOWP(team[k].GetOWP(j));
				}
			}
			team[j].SetTOWP();
			cout <<team[j].GetTOWP()<<" ";
		}
		cout <<endl;

		for (int j=0;j<number;j++)
		{
			for (int k=0;k<number;k++)
			{
				if (team[j].PlayedThis(k))
				{
					team[j].AddOOWP(team[k].GetTOWP());
				}
			}
			team[j].SetOOWP();
			cout <<team[j].GetOOWP()<<" ";
		}
		cout <<endl;

		out << "Case #" << i+1 << ":" <<endl;
		for (int j=0;j<number;j++)
		{
			out << team[j].GetRPI()<<endl;
		}
	}


	in.close();
	out.close();

	return 0;
}
