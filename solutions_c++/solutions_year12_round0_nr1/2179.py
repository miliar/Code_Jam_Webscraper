#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define Tmax 30
#define Gmax 200
//#define

int main()
{
	char * filenamein="A-small-attempt2.in";
	char * filenameout="A-small-attempt2.out";
	ifstream fin(filenamein);
	ofstream fout(filenameout);

	string known="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvyeq";
	string match="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupaoz";

	int matchsize=match.size();

	char lookup[26];

	for (int i=0; i<26; i++)
	{
		lookup[i]=' ';
	}

	int sum=0;
	int asum=0;
	int bsum=0;
	int total=0;
	for (int i=0; i<26; i++)
	{
		total+=i;
	}

	for (int i=0; i<matchsize; i++)
	{
		int index=int (known[i]-'a');
		if (lookup[index]==' ')
		{
			lookup[index]=match[i];
			asum+=index;
			bsum+=int(match[i]-'a');
		}
	}

	int aindex=total-asum;
	int bindex=total-bsum;

	lookup[aindex]='a'+bindex;

	int T;

	string tcase[Tmax];

	fin >> T;

	string getendl;

	getline(fin,getendl);

	for (int i=0; i<T; i++)
	{
		getline(fin,tcase[i]);
	}
	

	fin.close();

	for (int i=0; i<T; i++)
	{
		fout << "Case #"<< i+1 << ": ";
		int linesize=tcase[i].size();
		for (int j=0; j<linesize; j++)
		{
			if (tcase[i][j]==' ')
				fout << ' ';
			else
			{
				fout << lookup[int(tcase[i][j]-'a')];
			}
		}
		fout << endl;
	}

	fout.close();

	return 0;

}