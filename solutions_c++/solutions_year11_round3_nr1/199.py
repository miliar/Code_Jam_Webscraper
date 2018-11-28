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
	freopen("Al.in","r",stdin);
	freopen("Al.out","w",stdout);
	char i[54][54];
	
	int TT;
	scanf("%d",&TT);
	ren (T,1,TT+1)
	{
		bool res=true;
		int r, c;
		RESET(i,0);
		
		scanf("%d%d",&r,&c);
		ren (y,0,r) scanf("%s",i[y]);
		
		ren (y,0,r)
		{
			ren (x,0,c) if (i[y][x] == '#')
			{
				if ((x==c-1) || (y==r-1) || (i[y+1][x+1]!='#') || (i[y][x+1]!='#') || (i[y+1][x]!='#'))
				{
					res=false;
					break;
				}
				else
				{
					i[y][x] = i[y+1][x+1] = '/';
					i[y+1][x] = i[y][x+1] = '\\';
				}
			}
			if (!res) break;
		}
		
		printf("Case #%d:\n",T);
		if (res)
		{
			ren (y,0,r) printf("%s\n",i[y]);
		}
		else printf("Impossible\n");
		
	}
	return 0;
}
