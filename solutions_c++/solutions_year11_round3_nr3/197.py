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
	freopen("Csmall.in","r",stdin);
	freopen("Csmall.out","w",stdout);
	
	int TT;
	scanf("%d",&TT);
	ren (T,1,TT+1)
	{
		int n, U, L, i, res=-1;
		vector <int> v;
		
		scanf("%d%d%d",&n,&L,&U);
		ren (x,0,n) scanf("%d",&i), v.pb(i);
		
		//sort(ALL(v));
		ren (x,L,U+1)
		{
			bool ok=true;
			repi (it,v)
			{
				if ((x % (*it) == 0) || ((*it) % x == 0)) continue; else
				{
					ok = false;
					break;
				}
			}
			if (ok)
			{
				res = x;
				break;
			}
		}
		
		printf("Case #%d: ",T);
		(res==-1) ? printf("NO\n") : printf("%d\n",res);
	}
	return 0;
}
