#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define Tmax 100
#define Nmax 100

int main()
{
	char * filenamein="B-large.in";
	char * filenameout="B-large.out";
	ifstream fin(filenamein);
	ofstream fout(filenameout);

	int gler[Tmax][Nmax];
	int Ntable[Tmax];
	int Stable[Tmax];
	int Ptable[Tmax];

	int T;
	fin >> T;
	for (int i=0; i<T; i++)
	{
		fin >> Ntable[i];
		fin >> Stable[i];
		fin >> Ptable[i];
		for (int j=0; j<Ntable[i]; j++)
		{
			fin >> gler[i][j];
		}
	}
	fin.close();

	for (int i=0; i<T; i++)
	{
		int sur=Stable[i];
		int bey=Ptable[i];
		int total=0;
		fout << "Case #"<< i+1 << ": ";
		for (int j=0; j<Ntable[i]; j++)
		{
			int ave=gler[i][j]/3;
			int left=gler[i][j]%3;
			if (left==0)
			{
				if (ave>=bey)
					total++;
				else if (ave+1>=bey && sur>0 && ave!=0)
				{
					sur--;
					total++;
				}
			}
			else if (left==1)
			{
				if (ave+1>=bey)
					total++;
				else if (ave+1>=bey && sur>0)
				{
					sur--;
					total++;
				}
			}
			else if (left==2)
			{
				if (ave+1>=bey)
					total++;
				else if (ave+2>=bey && sur>0)
				{
					sur--;
					total++;
				}
			}
		}
		fout << total << endl;
	}

	return 0;
}