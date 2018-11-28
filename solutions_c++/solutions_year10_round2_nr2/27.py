#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <deque>
#include <algorithm>
#include <complex>
using namespace std;


typedef long long LL;
typedef pair<int,int> PII;

#define pb push_back
#define mp make_pair
#define sz size()
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define FOR(i,a,b) for(int i=(a),_b(b); i<_b; ++i)
#define RFOR(i,a,b) for(int i=(a)-1,_b(b); i>=_b; --i)
#define CLR(a,v) memset((a),(v),sizeof(a))
#define CPY(a,b) memcpy((a),(b),sizeof(a))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) ((a)<(0)?-(a):(a))
#define HAS(x,k) ((x).find(k)!=(x).end())
#define sqr(a) ((a)*(a))

#define PREV(x) ((x)&((x)-1))
#define NEXT(x) (((x)<<1) - PREV(x))




int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int t; scanf("%d",&t);
	int tc=0;
	while(t--)
	{
		++tc;
		int N,K,B,T;
		scanf("%d%d%d%d",&N,&K,&B,&T);
		int X[64];
		int V[64];
		FOR(i,0,N) scanf("%d",X+i);
		FOR(i,0,N) scanf("%d",V+i);
		int r=0;
		int c=0;
		int has=K;
		RFOR(i,N,0)
		{
			if (has>0)
			{
				if (X[i]+V[i]*T>=B)
				{
					r+=c;
					--has;
				}
				else
					++c;
			}
		}
		if (has>0)printf("Case #%d: IMPOSSIBLE\n",tc);
		else
			printf("Case #%d: %d\n",tc,r);
	}


	
	
	return 0;
}