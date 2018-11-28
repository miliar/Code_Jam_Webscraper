#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<queue>
#include<cmath>
#include<set>
#include<map>
#include<vector>
#include<complex>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define REP(a,b,c) for(int a=b; a<c; a++)
#define REPS(a,b,c) for(int a=b; a<=c; a++)
#define REPD(a,b,c) for(int a=b; a>=c; a--)
#define REPI(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)
#define RESET(a,b) memset(a,b,sizeof(a))
using namespace std;
 
typedef long long LL;
typedef pair<int,int> pii;
typedef complex<double> pt;
 
const int INF = 1000000000;
const double EPS = 1e-9;
 
//sicasli's template

int n;
char iput[105][105];

double wp(int x,  int z)
{
	double tot = 0.0;
	double win = 0.0;
	
	REP(i,0,n) if (i!=x && i!=z && iput[x][i]!='.')
	{
		tot += 1.0;
		win += iput[x][i]=='1';
	}	
	
	return win/tot;
}

double owp(int x)
{
	double tot = 0.0;
	double jum = 0.0;
	
	REP(i,0,n) if (i!=x && iput[x][i]!='.')
	{
		jum += 1.0;
		tot += wp(i,x);	
	}
	
	return tot/jum;
}

double oowp(int x)
{
	double tot = 0.0;
	double jum = 0.0;	
	
	REP(i,0,n) if (i!=x && iput[x][i]!='.')
	{
		jum += 1.0;
		tot += owp(i);
	}
	
	return tot/jum;
}

int main()
{
	int t;
	scanf("%d",&t);
	
	int cas = 0;
	
	while (t--)
	{
		printf("Case #%d:\n",++cas);
		scanf("%d",&n);
		REP(i,0,n) scanf("%s",iput[i]);
		REP(i,0,n)
		{
			double ans = (0.25 * wp(i,-1)) + (0.5 * owp(i)) + (0.25 * oowp(i));
			printf("%.10lf\n",ans);
		}
	}
	
	return 0;
}

