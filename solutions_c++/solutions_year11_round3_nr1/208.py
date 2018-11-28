#include <string>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <sstream>
# include<fstream>
using namespace std;
# define FOR(i,a,n) for(int i=a;i<n;++i)
# define REP(i,n) FOR(i,0,n)
typedef long long LL;
ifstream fin("A-large.in");
ofstream fout("out.txt");
char ar[100][100];
int main()
{
	int tc;
	fin>>tc;
	int cnt=0;
	while(tc--)
	{
		++cnt;
		int r,c;
		fin>>r>>c;
		REP(i,r) REP(j,c) fin>>ar[i][j];
		REP(i,r-1)
		REP(j,c-1)
		if(ar[i][j]=='#'&&ar[i][j+1]=='#')
		{
			if(ar[i+1][j]=='#'&&ar[i+1][j+1]=='#')
			{
				ar[i][j]='//';
				ar[i+1][j+1]='//';
				ar[i+1][j]='\\';
				ar[i][j+1]='\\';
			}
		}
		bool ok=true;
		REP(i,r) REP(j,c) if(ar[i][j]=='#') 
		{
			ok=false;
			break;
		}
		fout<<"Case #"<<cnt<<":"<<endl;
		if(!ok) fout<<"Impossible"<<endl;
		else
		{
			REP(i,r)
			{
				REP(j,c)
				fout<<ar[i][j];
				fout<<endl;
			}
		}
	}
}

		
