#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<map>
#include<algorithm>
#include<cmath>
#include<set>
#include<sstream>
#include<map>
#include<utility>
#include<cmath>

#define S(n) scanf("%d",&n)
#define SL(n) scanf("%lld",&n)
#define SF(n) scanf("%Lf",&n)

#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)
#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>

#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000

#define CLR(var,val) memset(var,val,sizeof((var)))
#define S(n) scanf("%d",&n)
#define LL long long
#define LD long double
#define triple pair<int, pair<int,int> >
#define OFF 0
#define MOD
#define ISBITSET(n,i) ((n&(1<<i))>>i)
#define TOGGLEBIT(n,i) (n^(1<<i))
#define SETBIT(n,i) (n|(1<<i))
#define CLRBIT(n,i) (n & (n^(1<<i)))
#define FIN freopen("inp.in","r",stdin)
#define FOUT freopen("out.out", "w",stdout)
using namespace std;

int nextPos[1001];
int cost[1001];
long long g[1001];

int main()
{	
	int T, prevPos, i, pos, N;
	long long k, R, ans;
	FIN;
	FOUT;
	cin>>T;
	int c = 1;
	while(T--)
	{
		ans = 0;
		cin>>R>>k>>N;
		REP( i, N )	{	nextPos[i] = cost[i] = -1;	}
		REP( i, N )	cin>>g[i];
		pos = 0;
		REP( i, R )
		{
			if( nextPos[pos] != -1 ){	pos = nextPos[pos];	ans+=cost[pos]; continue;	}
			long long sum = 0;
			prevPos = pos;
			int count = 0;
			while(true)
			{	
				count++;
				if( count == N+1 ) break; 
				if( sum + g[pos] <= k )
				{
					sum+=g[pos];	pos=(pos+1)%N; 
				}
				else break;
			}
			cost[prevPos] = sum;
			ans+=sum;
			//cout << ans << " ";
		}
		cout << "Case #" << c << ": " << ans << endl;
		c++;
	}
}
