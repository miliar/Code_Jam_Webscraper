#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string.h>
using namespace std;
#define REP(i,n) for(int i=0,n_=(n);i<n_;i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOR(i,a,b) for (int i=a,b_=b;i<=(b);i++)
#define ALL(a) a.begin(),a.end()
#define SZ(a) (int)(a).size()
#define SORT(a) sort(ALL(a))
#define INF 1073741823
#define DEB(x) cerr<<#x<<":"<<x<<"\n"
#define PB(b) push_back(b)
#define i64 long long 
#define FOREACH(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

vector<int> SplitInt(string &s)
{
	vector<int>Res;int tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}

vector<string> SplitStr(string &s)
{
	vector<string>Res;string tmp;stringstream a(s);
	while (a>>tmp){Res.push_back(tmp);}return Res;
}

//////////////////////////////////////////////////////////////
double R[1000],W[1000],OWP[1000],OOWP[1000],W2[1000];
char P[123][123];
int main ()
{
	int c,n;
	scanf ("%d",&c);
	long long N,pd,pg;
	FOR(cas,1,c)
	{
		//TODO
		
		scanf ("%d",&n);
		REP(i,n)
		{
			scanf ("%s",P[i]);
			R[i]=0;
		}	
		REP(i,n)
		{
			double w=0,t=0;
			REP(j,n)
			{
				if (P[i][j]=='1')
					w++;
				if (P[i][j]!='.')
					t++;
			}
			W[i]=(w)/(double)t;
		}
		REP(i,n)
		{
//			REP(k,n) W2[k]=0;
			REP(k,n)
			{
				double w=0,t=0;
				if (P[k][i]=='.')continue;
				REP(j,n)
				{
					if (j==i)continue;
					if (P[k][j]=='1')
					{
						w++;
					}
					if (P[k][j]!='.')
						t++;
				}
				W2[k]=(w)/(double)t;
			}
			double o=0;
			double t=0;
			REP(k,n)
			{
				if (P[i][k]!='.')
				{
					o+=W2[k];
					t++;
				}
			}
			OWP[i]=o/t;
		}
		REP(i,n)
		{
			double w=0;
			double t=0;
			REP(j,n)
			{
				if (P[i][j]!='.')
				{
					w+=OWP[j];
					t++;
				}
			}
			OOWP[i]=w/t;
		}
		REP(i,n)
		{
			R[i]=0.25 * W[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
		}
		printf ("Case #%d:\n",cas);
		REP(i,n)
			printf("%.6lf\n",R[i]);
		
		
	}
	return 0;
}

