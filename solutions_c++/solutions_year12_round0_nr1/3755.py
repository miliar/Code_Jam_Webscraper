#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>
using namespace std;
const int MAX_LENGTH = 1000;
int T;
char MAP[26];
bool flag1[26];
bool flag2[26];
int main()
{
	memset(flag1,false,sizeof(bool)*26);
	memset(flag2,false,sizeof(bool)*26);
	ifstream fin("sample.txt");
	ifstream fin2("sampleout.txt");
	fin>>T;
	char temp[MAX_LENGTH];
	fin.getline(temp,MAX_LENGTH);
	for(int i = 0; i < T; i++)
	{
		char line[MAX_LENGTH];
		char lineout[MAX_LENGTH];
		fin.getline(line,MAX_LENGTH);
		fin2.getline(lineout,MAX_LENGTH);
		for(int j = 0 ; j < strlen(line); j++)
		{
			if(line[j]==' ')
				continue;
			else
			{
				int pos = line[j] - 'a';
				if(flag1[pos]==true)
					continue;
				MAP[pos] = lineout[j];
				flag1[pos] = true;
				flag2[(lineout[j]-'a')] = true;
			}
		}
	}
	fin.close();
	fin2.close();

	MAP[('q'-'a')]='z';
	MAP['z'-'a']='q';

	ifstream newfin("A.in");
	ofstream fout("A.out");
	newfin>>T;
	newfin.getline(temp,MAX_LENGTH);
	for(int i = 0;i < T; i ++)
	{
		fout<<"Case #"<<i+1<<": ";
		char line[MAX_LENGTH];
		newfin.getline(line,MAX_LENGTH);
		for(int j = 0 ; j < strlen(line); j++)
		{
			if(line[j]==' ')
				fout<<" ";
			else
			{
				fout<<MAP[(line[j]-'a')];
			}
		}
		fout<<"\n";
	}
	fout.close();
	newfin.close();
}