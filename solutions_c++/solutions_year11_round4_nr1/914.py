/* AnilKishore ( RedAnt ) */

#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>

#include <iostream>
#include <algorithm>
#include <string>

#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;

#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define F first
#define S second
#define SET(v,x) memset(v,x,sizeof v)
#define FOR(i,a,b) for(int _n(b),i(a);i<_n;i++) 
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define SORT(v) sort(ALL(v))
#define SZ(v) int(v.size())
#define SI ({int x;scanf("%d",&x);x;})

#define MX 1003

LL b[MX],e[MX],w[MX];
LL speed[1000006];

void solve()
{	
	LL X = SI, S = SI, R = SI, t = SI, N = SI;
	
	REP(i,N) b[i]=SI, e[i]=SI, w[i]=SI;
	
	FOR(i,1,X+1) speed[i]=S;
	REP(i,N) for(int j=b[i]+1;j<=e[i];j++) speed[j]+=w[i];

	sort(speed+1,speed+1+X);

	double ans = 0.0;

	bool run = true;
	double left = 1.*t;
	
	for(int j=1;j<=X;j++)
	{
		if(run)
		{
			double ct = 1.0/(speed[j]+R-S);
			if(ct<=left+1e-9) ans+=ct;
			else
			{
				double d = 1.0-(speed[j]+R-S)*left;
				ans+=left + (d/speed[j]);
				run=false;
			}
			left-=ct;
		}
		else ans+=1.0/(speed[j]);
	}

	printf("%.10lf\n",ans);
}


void run()
{
	for(int kase=1,kases=SI;kase<=kases;kase++)
	{
		printf("Case #%d: ",kase);
		solve();
		//puts("");
	}	
}


int main(int argc, char **argv)
{
	if(argc==2)
	{
		if(argv[1][0]=='s' || argv[1][0]=='S')
		{
			freopen("./../A-small-attempt3.in","r",stdin);
			freopen("A-small-output.out","w",stdout);
		}
	
		if(argv[1][0]=='l' || argv[1][0]=='L')
		{
			freopen("./../A-large.in","r",stdin);
			freopen("A-large-output.out","w",stdout);
		}
	}

	run();
					
	return 0;
}
