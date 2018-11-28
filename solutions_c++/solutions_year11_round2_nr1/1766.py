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
int T[1000],W[1000];
double owp[1000],oowp[1000];
char ar[1000][1000];
ifstream fin("A-large.in");
ofstream fout("out.txt");
int main()
{
	int tc;
	fin>>tc;
	int cnt=0;
	while(tc--)
	{
		++cnt;
		memset(T,0,sizeof(T));
		memset(W,0,sizeof(W));
		REP(i,1000) oowp[i]=0,owp[i]=0;
		int n;
		fin>>n;
		REP(i,n) REP(j,n) fin>>ar[i][j];
		REP(i,n)
		{
			REP(j,n) 
			{
				if(ar[i][j]!='.') ++T[i];
				if(ar[i][j]=='1') ++W[i];
			}
		}
		REP(i,n)
		{
			REP(j,n)
			if(ar[j][i]!='.')
			{
				int tot=T[j]-1,wins=W[j]-(ar[j][i]=='1');
				owp[i]+=wins*1.0/tot;
			}
			owp[i]/=T[i];
		}
		REP(i,n)
		{
			REP(j,n)
			if(ar[j][i]!='.')
			{
				oowp[i]+=owp[j];
			}
			oowp[i]/=T[i];
		}
		fout<<"Case #"<<cnt<<":"<<endl;
		REP(i,n)
		{
			double ans = (0.25 * W[i]*1.0/T[i]) + 0.50 * owp[i] + 0.25 * oowp[i];
			fout<<ans<<endl;
		}
	}
}
