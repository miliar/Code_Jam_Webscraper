#include<cstdio>
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

int main()
{
	int cas = 0;
	int t;
	scanf("%d",&t);
	while (t--)
	{
		LL n,a;
		int b;
		scanf("%lld %lld %d",&n,&a,&b);
		bool bisa=0;
		
		LL gg = __gcd(a,100LL);
		LL i = 100/gg;
		
			if (i<=n)
			{
				if (b==0 && a==0)
				{
					bisa = 1;
					//break;	
				}	
				if (b==100 && a==100)
				{
					bisa = 1;
					//break;
				}
				if (b!=100 && b!=0)
				{
					bisa = 1;
					//break;	
				}
			}	
			
		printf("Case #%d: ",++cas);
		printf(bisa ? "Possible\n" : "Broken\n");
	}
	return 0;
}
