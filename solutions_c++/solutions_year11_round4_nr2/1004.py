#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<list>
#include<stdio.h>
#include<sstream>
#include<set>
#include<deque>
#include<cmath>
#include<numeric>
#include<fstream>

using namespace std;

typedef long long LInt;
typedef vector<int> intvec;
typedef vector<intvec> intvec2;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define FOR(i,k,n) for (int i=(k); i<(int)(n); ++i)
#define DEC(i,k) for (int i=(k); i>=0; --i)
#define FORIT(i,c) for (decltype((c).begin())i=(c).begin();i!=(c).end();++i)

/////////////////////////
#define fin cin
#define fout cout
////////////////////////

int main()
{
	ifstream fin("E:\\Buid\\Algorithm\\GoogleJam\\2011Round2\\B-small-attempt1.in");
	ofstream fout("E:\\Buid\\Algorithm\\GoogleJam\\2011Round2\\B-small-attempt0.out");
	ofstream foutt("E:\\Buid\\Algorithm\\GoogleJam\\2011Round2\\B-small-attempt0.test");
	
	int T,ans;
	fin>>T;
	foutt<<T<<endl;

	REP(TEST,T)
	{
		ans = 0;
		int R,C,D;
		fin>>R>>C>>D;
		intvec2 sht;
		REP(i,R)
		{
			string ss;
			fin>>ss;
			intvec row;
			REP(j,C)
			{
				int tem;
				tem = ss[j]-'0';
				foutt<<tem<<" ";
				row.push_back(tem);
			}
			sht.push_back(row);
			foutt<<endl;
		}
		REP(x,R)
		{
			REP(y,C)
			{
				int K = min(min(x,R-1-x),min(y,C-1-y));
				int u;
				int wx = 0;
				int wy = 0;
				for(u = 1;u<=K;++u)
				{
					for(int ii = y-u;ii<=y+u;++ii)
					{
						int dd = sht[x-u][ii];
						wx+=dd*(x-u-x);
						wy+=dd*(ii-y);
					}
					for(int ii = y-u;ii<=y+u;++ii)
					{
						int dd = sht[x+u][ii];
						wx+=dd*(x+u-x);
						wy+=dd*(ii-y);
					}
					for(int ii = x-u+1;ii<=x+u-1;++ii)
					{
						int dd = sht[ii][y-u];
						wx+=dd*(ii-x);
						wy+=dd*(y-u-y);
					}
					for(int ii = x-u+1;ii<=x+u-1;++ii)
					{
						int dd = sht[ii][y+u];
						wx+=dd*(ii-x);
						wy+=dd*(y+u-y);
					}
					int d1 = sht[x-u][y-u],d2=sht[x-u][y+u],d3=sht[x+u][y-u],d4=sht[x+u][y+u];
					if((wx-(d1*(-u)+d2*(-u)+d3*(u)+d4*(u))) == 0 && (wy-(d1*(-u)+d2*(u)+d3*(-u)+d4*(u))) == 0)
					{
						ans = max(ans,u*2+1);
					}
				}
			}
		}

		REP(x,R-1)
		{
			REP(y,C-1)
			{
				double wx = 0;
				double wy = 0;
				REP(u,600)
				{
					if(x-u<0 || y-u<0 || x+u+1>=R || y+u+1>=C)
						break;
					for(int ii = y-u;ii<=y+u+1;++ii)
					{
						int dd = sht[x-u][ii];
						wx+=1.0*dd*(x-u-x-0.5);
						wy+=1.0*dd*(ii-y-0.5);
					}
					for(int ii = y-u;ii<=y+u+1;++ii)
					{
						int dd = sht[x+u+1][ii];
						wx+=1.0*dd*(x+u+1-x-0.5);
						wy+=1.0*dd*(ii-y-0.5);
					}
					for(int ii = x-u+1;ii<=x+u;++ii)
					{
						int dd = sht[ii][y-u];
						wx+=1.0*dd*(ii-x-0.5);
						wy+=1.0*dd*(y-u-y-0.5);
					}
					for(int ii = x-u+1;ii<=x+u;++ii)
					{
						int dd = sht[ii][y+u+1];
						wx+=1.0*dd*(ii-x-0.5);
						wy+=1.0*dd*(y+u+1-y-0.5);
					}
					int d1 = sht[x-u][y-u],d2=sht[x-u][y+u+1],d3=sht[x+u+1][y-u],d4=sht[x+u+1][y+u+1];
					if(fabs(wx-1.0*(1.0*d1*(-u-0.5)+1.0*d2*(-u-0.5)+1.0*d3*(u+0.5)+1.0*d4*(u+0.5)))<1e-6 && fabs(wy-1.0*(1.0*d1*(-u-0.5)+1.0*d2*(u+0.5)+1.0*d3*(-u-0.5)+1.0*d4*(u+0.5))) <1e-6)
					{
						ans = max(ans,2*(u+1));
					}
				}
			}
		}

		if(ans>=3)
		fout<<"Case #"<<TEST+1<<": "<<ans<<endl;
		else
			fout<<"Case #"<<TEST+1<<": "<<"IMPOSSIBLE"<<endl;
	}
	system("pause");
	return 0;
}