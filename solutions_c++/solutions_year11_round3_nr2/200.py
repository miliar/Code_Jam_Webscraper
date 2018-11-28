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

inline bool cmp(const int &a, const int &b)
{
	return (a>b);
}

int main()
{
	freopen("Blar.in","r",stdin);
	freopen("Blar.out","w",stdout);
	
	int TT;
	scanf("%d",&TT);
	ren(T,1,TT+1)
	{
		bool blm = true;
		ll res=0LL, l, t, n, c, a;
		vector <ll> v;
		
		scanf("%lld%lld%lld%lld",&l,&t,&n,&c);
		ren (x,0,c)
		{
			scanf("%lld",&a);
			v.pb(a);
		}
		ren (x,c,n) v.pb( v[x%c] );
		
		ren (x,0,n) if (blm)
		{
			if (v[x]*2 <= t)
			{
				t -= v[x]*2LL;
				res += v[x]*2LL;
				v[x] = 0LL;
			}
			else
			{
				v[x] -= t/2LL;
				res += t;
				t = 0LL;
				blm = false;
				sort( v.begin()+x,v.end(),cmp );
				--x;
			}
			//printf("%lld %lld\n",v[x],res);
		}
		else
		{
			if (l>0LL)
			{
				res += v[x];
				--l;
			}
			else res += v[x]*2LL;
			//printf("%lld %lld\n",v[x],res);
		}
		
		printf("Case #%d: %lld\n",T,res);
	}
	return 0;
}
