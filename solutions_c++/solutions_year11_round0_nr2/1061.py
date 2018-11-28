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
char P[12312];
char A[321][312];
bool Op[312][321];
int main ()
{
	int c,n;
	scanf ("%d",&c);
	
	FOR(cas,1,c)
	{
		memset(A,0,sizeof A);
		memset(Op,0,sizeof Op);
		scanf ("%d",&n);
		REP(i,n)
		{
			scanf ("%s",P);
			A[P[0]][P[1]]=P[2];
			A[P[1]][P[0]]=P[2];
		}
		scanf ("%d",&n);
		REP(i,n)
		{
			scanf ("%s",P);
			Op[P[0]][P[1]]=1;
			Op[P[1]][P[0]]=1;
		}
		scanf ("%d",&n);
		scanf("%s",P);
		vector<char> Q;
		REP(i,n)
		{
			if (SZ(Q))
			{
				char p=Q.back();
				char q=P[i];
				
				if(A[q][p])
				{
					Q.pop_back();
					Q.PB(A[q][p]);
				}
				else
				{
					bool bad=false;
					REP(j,SZ(Q))
					{
						p=Q[j];
						if (Op[p][q])
						{
							Q.clear();

						bad=true;
							break;

						}
					}
					if (!bad)
					Q.PB(q);
				}
			}
			else
				Q.PB(P[i]);
		}
		printf ("Case #%d: [",cas);
		
		REP(i,SZ(Q))
		{
			if (i<SZ(Q)-1)
			{
				printf ("%c, ",Q[i]);
				
			}
			else
				printf ("%c",Q[i]);
		}
		printf ("]\n");
	}
	return 0;
}

