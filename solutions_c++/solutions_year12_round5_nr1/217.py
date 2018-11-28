#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl
#define sqr(x) ((x)*(x))

int tests,n,N;
int l[1010],p[1010],a[1010];


int main()
{
	freopen("a00.in","r",stdin);
	freopen("aa.out","w",stdout);
	
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		scanf("%d",&n);
		for (int i=0;i<n;i++) scanf("%d",l+i);
		for (int i=0;i<n;i++) scanf("%d",p+i);
		memset(a,0,sizeof a);
		printf("Case #%d:",test);
		for (int i=1;i<=n;i++)
		{
			int k = -1;
			for (int j=0;j<n;j++) if (a[j]==0)
			{
				if (k==-1 || p[j]>p[k])
					k = j;
			}
			a[k] = 1;
			printf(" %d",k);
		}
		printf("\n");
	}
	
	return 0;
}
