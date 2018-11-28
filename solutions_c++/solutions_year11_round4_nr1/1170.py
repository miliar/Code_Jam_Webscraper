#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <memory.h>
using namespace std;

#define fi first
#define sc second
#define cs c_str
#define mp make_pair
#define pb push_back
#define ALL(c) (c).begin(), (c).end()
#define RALL(c) (c).rbegin(), (c).rend()
#define RESET(a,b) memset( (a), b, sizeof(a) )
#define ren(a,b,c) for (int a=b; a<c; ++a)
#define renl(a,b,c) for (ll a=b; a<c; ++a)
#define red(a,b,c) for (int a=b; a>=c; --a)
#define redl(a,b,c) for (ll a=b; a>=c; --a)
#define repi(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)

const double eps = 1e-9;
typedef long long ll;
typedef pair <int,int> pii;

//lintaor1's template

#define FIN "A-large.in"
#define FOT "A-large.out"

struct way
{
	int a, b, v1, v2;
	bool operator< (const way &b) const
	{ return ((double)v2 / v1) < ((double)b.v2 / b.v1); }
};

int main()
{
	freopen(FIN,"r",stdin);
	freopen(FOT,"w",stdout);
	
	int TT;
	scanf("%d",&TT);
	ren (T,1,TT+1)
	{
		double res=0.0;
		vector <way> v;
		vector <pii> lho;
		
		int X, s, r, n, a, b, c, sz;
		double t;
		
		scanf("%d%d%d%lf%d",&X,&s,&r,&t,&n);
		ren (x,0,n)
		{
			scanf("%d%d%d",&a,&b,&c);
			v.pb( (way){a,b,c+s,c+r} );
			lho.pb(mp(a,b));
		}
		
		lho.pb(mp( 0,0 ));
		lho.pb(mp( X,X ));
		sort(ALL(lho));
		sz = lho.size();
		ren (x,1,sz)
			if (lho[x-1].sc < lho[x].fi) v.pb( (way){lho[x-1].sc,lho[x].fi,s,r} );
		
		sort(RALL(v));
		sz = v.size();
		ren (x,0,sz)
		{
			int ds = v[x].b-v[x].a;
			
			//printf("%d %d %d %d   %.6lf %d   %.6lf\n",v[x].a,v[x].b,v[x].v1,v[x].v2,t,ds,res);
			
			if ((double)ds / v[x].v2 > t)
			{
				res += t;
				res += ((double)ds - (t*v[x].v2)) / v[x].v1;
				t = 0.0;
			}
			else
			{
				res += (double)ds / v[x].v2;
				t -= (double)ds / v[x].v2;
			}
		}
		
		//--------------------------------------------------------------
		printf("Case #%d: ",T);
		printf("%.6lf\n",res);
	}
	return 0;
}
