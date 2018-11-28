#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <memory.h>
using namespace std;
    
#define pb push_back
#define fi first
#define sc second
#define mp make_pair
#define cs c_str
#define ALL(c) (c).begin(), (c).end()
#define RALL(c) (c).rbegin(), (c).rend()
#define RESET(c,x) memset (c, x, sizeof (c))
#define ren(a,b,c) for (int a=b;a<c;a++)
#define red(a,b,c) for (int a=b;a>=c;a--)
#define repi(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define pqd(c) priority_queue <__typeof(c)>
#define pqi(c) priority_queue < __typeof(c),vector<__typeof(c)>,greater<__typeof(c)> >

const double eps = 1e-9;

typedef long long ll;
typedef pair <int,int> pii;

//lintaor1's template

int main()
{
	//freopen("Al.in","r",stdin);
	//freopen("Al.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	ren (TT,1,T+1)
	{
		bool res = true;
		ll n, Pd, Pg;
		
		scanf("%lld%lld%lld",&n,&Pd,&Pg);
		
		if ((Pg == 100) && (Pd != 100)) res = false;
		else if ((Pg == 0) && (Pd != 0)) res = false;
		else
		{
			ll den = 100LL;
			den /= __gcd( Pd,den );
			if (den > n) res = false;
		}
		
		printf("Case #%d: %s\n", TT, ((res) ? "Possible" : "Broken"));
	}
	return 0;
}
