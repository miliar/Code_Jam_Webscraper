#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <iostream>
#define INF 1000000007
#define EPS 0.000000001
using namespace std;

int t,n,m,i,j,x,k,p;
bool l;
int a[10001],b[10001],c[10001];

int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(int T=1;T<=t;T++)
	{
		l=false;
		printf("Case #%d: ",T);
		scanf("%d",&n);
		for(i=1;i<=n;i++)
			scanf("%d%d",&a[i],&b[i]);
		a[0] = 0; b[0] = 0; n++;
		scanf("%d",&m);
		memset(c,-1,10001*4);
		c[1] = 0;
		for(i=1;i<n;i++)
			if(c[i]>=0)
			{
				j = c[i];
				p = min(a[i]-a[j],b[i]);
				if(p>=m-a[i])
				{
					l = true;
					break;
				}
				for(k=i+1;k<n && a[k]-a[i]<=p;k++)
					if(c[k] == -1)
						c[k] = i;
			}
		if(l)
			printf("YES\n"); else
			printf("NO\n");
	}
	return 0;
}