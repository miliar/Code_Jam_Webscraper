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

int i[30];

int main()
{
	//freopen("C-small.in","r",stdin);
	//freopen("C-small.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	ren (N,1,T+1)
	{
		int n, res=-1, sea, pat1, pat2;
		RESET(i,0);
		
		scanf("%d",&n);
		ren (x,0,n) scanf("%d",&i[x]);
		ren (x,1,(1<<n)-1)
		{
			sea=0;
			pat1=0;
			pat2=0;
			
			ren (y,0,n)
				if ((x)&(1<<y)) sea+=i[y], pat1^=i[y]; else pat2^=i[y];
			
			if (pat1 == pat2) res = max( sea,res );
		}
		
		printf("Case #%d: ",N);
		if (res == -1) printf("NO\n"); else printf("%d\n",res);
	}
	return 0;
}
