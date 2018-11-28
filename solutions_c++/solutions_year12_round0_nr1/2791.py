#include<string>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
string UnCrp[5];
string Crped[5];
char maps[300];
void dbinit()
{
	ifstream datafin("database.txt");
	for(int i=1;i<=3;i++)
	getline(datafin,UnCrp[i]);
	for(int i=1;i<=3;i++)
	getline(datafin,Crped[i]);
	for(int i=1;i<=3;i++)
	{
		for(int j=0;j<UnCrp[i].size();j++)
		{
			char a=UnCrp[i][j];
			char b=Crped[i][j];
			maps[a]=b;
		}
	}
}
int N;
string Org[50];
char ans[50][200];
int main()
{
	ios::sync_with_stdio(0);
	dbinit();
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin>>N;
	getline(fin,Org[0]);
	for(int i=1;i<=N;i++)
	getline(fin,Org[i]);
	maps['q']='z',maps['z']='q';
	for(int i=1;i<=N;i++)
	{
		for(int j=0;j<Org[i].size();j++)
		ans[i][j]=maps[Org[i][j]],ans[i][j+1]='\n';
	}
	for(int i=1;i<=N;i++)
	{
		fout<<"Case #"<<i<<": ";
		for(int j=0;ans[i][j]!='\n';j++)
		fout<<ans[i][j];
		fout<<endl;
	}
	return 0;
}