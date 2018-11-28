#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<iostream>
#include<sstream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cctype>
#include<string>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<climits>
#include<complex>
#define mp make_pair
#define pb push_back
#define all(x) (x.begin(),x.end())
using namespace std;
const double eps=1e-8;
int dblcmp(double d)
{
    if (fabs(d)<eps)return 0;
    return d>eps?1:-1;
}
char s[600][600];
int n,m,d;
int main()
{
	freopen("C:\\Users\\daizhy\\Documents\\output.txt","w",stdout);
	int i,j,k,l,cas,cc=0;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d%d%d",&n,&m,&d);
		
		for (i=0;i<n;i++)
		{
			scanf("%s",s[i]);
		}
		int ans=min(n,m);
		double dx,dy;
		for (;ans>=3;ans--)
		{
			for (i=0;i+ans<=n;i++)
			{
				for (j=0;j+ans<=m;j++)
				{
					int ex=i+ans;
					int ey=j+ans;
					int x=0;
					int y=0;
					//if (ans%2==0)
					{
						dx=i*1.0+ans/2.0-0.5;
						dy=j*1.0+ans/2.0-0.5;
					}
					double tx=0,ty=0;
					for (k=0;k<n;k++)
					{
						for (l=0;l<n;l++)
						{
							if (k<i||k>=ex||l<j||l>=ey)continue;
							if (k==i&&l==j)continue;
							if (k==i&&l==ey-1)continue;
							if (k==ex-1&&l==j)continue;
							if (k==ex-1&&l==ey-1)continue;
							tx+=(k*1.0-dx)*(s[k][l]-'0');
							ty+=(l*1.0-dy)*(s[k][l]-'0');
						}
					}
					if (dblcmp(0-tx))continue;
					if (dblcmp(0-ty))continue;
					goto fuck;		
				}
			}
		}
		fuck:
		printf("Case #%d: ",++cc);
		if (ans<3)puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}
