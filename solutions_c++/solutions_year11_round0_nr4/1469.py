#include <stdio.h>
#include <algorithm>
using namespace std;
const int maxn=10100;
int a[maxn],b[maxn];
int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
			b[i]=a[i];
		}
		sort(a,a+n);
		double ans=0;
		for(int i=0;i<n;i++)
		if(a[i]!=b[i])ans+=1;
		printf("Case #%d: %.6f\n",cas,ans);
	}	
}
