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
	//freopen("As.in","r",stdin);
	//freopen("As.out","w",stdout);
	
	pii WP[104];
	double OWP[104], OOWP[104];
	char i[104][104];
	
	int TT;
	scanf("%d",&TT);
	ren (T,1,TT+1)
	{
		int n;
		RESET(i,0);
		
		scanf("%d",&n);
		ren (x,0,n) scanf("%s",i[x]);
		
		RESET(WP,0);
		ren (x,0,n)
		{
			int f=0, s=0;
			ren (y,0,n)
			{
				((i[x][y] == '1') ? ++f : ((i[x][y] == '0') ? ++s : 0));
			}
			WP[x] = mp(f,s);
		}
		
		RESET(OWP,0);
		ren (x,0,n)
		{
			int m=0;
			ren (y,0,n) if (i[x][y] != '.')
			{
				++m;
				if (i[x][y]=='0') OWP[x] += (double)(WP[y].fi-1) / (WP[y].fi+WP[y].sc-1);
				else OWP[x] += (double)(WP[y].fi) / (WP[y].fi+WP[y].sc-1);
			}
			OWP[x] /= (double)m;
		}
		
		RESET(OOWP,0);
		ren (x,0,n)
		{
			int m=0;
			ren (y,0,n) if (i[x][y] != '.')
			{
				++m;
				OOWP[x] += OWP[y];
			}
			OOWP[x] /= (double)m;
		}
		
		printf("Case #%d:\n",T);
		ren (x,0,n) printf("%lf\n",0.25 * ((double)WP[x].fi/(WP[x].fi+WP[x].sc)) + 0.50 * OWP[x] + 0.25 * OOWP[x]);
	}
	return 0;
}
