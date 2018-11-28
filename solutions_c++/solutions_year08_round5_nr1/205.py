#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <deque>
#include <list>
#include <map>
#include <set>
using namespace std;
#define all(a) (a).begin(),(a).end()
#define mset(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define sz(a) a.size()
#define rep(i,n) for(i=0; i<n; i++)
#define forr(i,a,b) for(i=a; i<=b; i++)
#define ford(i,a,b) for(i=a; i>=b; i--)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define X first
#define Y second
typedef long long ll;
typedef vector<int> VI;

const int h=301, h2=2*h;
int U,N, i,j,k,n, l;
int a[h2][h2], x[40000],y[40000], p, d, sa,so;
char s[100];

int main()
{
	freopen("a-small.in","r",stdin);//large-small
	freopen("a-small.out","w",stdout);
	scanf("%d",&N);
	rep(U,N)
	{
		p=0; x[0]=y[0]=0; d=0; so=sa=0;
		scanf("%d",&n); mset(a,0);
		rep(i,n)
		{
			mset(s,0);
			scanf("%s %d",&s,&k);			
			rep(j,k)
			{
				l=0;
				while(s[l])
				{
					if(s[l]=='F')
					{
						switch (d)
						{
							case 0: { x[p+1]=x[p], y[p+1]=y[p]+1,
								a[x[p]+h][y[p]+h]|=8, a[x[p]+h-1][y[p]+h]|=2; break; }
							case 1: { x[p+1]=x[p]+1, y[p+1]=y[p], 
								a[x[p]+h][y[p]+h-1]|=1, a[x[p]+h][y[p]+h]|=4; break; }
							case 2: { x[p+1]=x[p], y[p+1]=y[p]-1,
								a[x[p+1]+h][y[p+1]+h]|=8, a[x[p+1]+h-1][y[p+1]+h]|=2; break; }
							case 3: { x[p+1]=x[p]-1, y[p+1]=y[p],
								a[x[p+1]+h][y[p+1]+h-1]|=1, a[x[p+1]+h][y[p+1]+h]|=4; break; }
						}
						sa+=(x[p+1]*y[p]-y[p+1]*x[p]);
						p++;
					}
					if(s[l]=='R') d=(d+1)%4;
					if(s[l]=='L') d=(d+3)%4;
					l++;
				}
			}
		}
		rep(i,h2)
		{
			rep(j,h2-1) if(a[i][j]&4) a[i][j+1]|=4;
			ford(j,h2-1,1) if(a[i][j]&1) a[i][j-1]|=1;
		}
		rep(j,h2)
		{
			rep(i,h2-1) if(a[i][j]&8) a[i+1][j]|=8;
			ford(i,h2-1,1) if(a[i][j]&2) a[i-1][j]|=2;
		}
		sa=abs(sa)/2; so=0;
		rep(i,h2) rep(j,h2)
			if((a[i][j]&1 && a[i][j]&4) || (a[i][j]&2 && a[i][j]&8)) so++;
//		rep(i,p+1) printf("%d %d\n",x[i],y[i]);
		printf("Case #%d: %d\n",U+1,so-sa);		
	}
	return 0;
}
