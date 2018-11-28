#include <cstdio>
using namespace std;
int test,sum,tmp,n,a[1005];

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	scanf("%d",&test);
	for (int kase=1;kase<=test;kase++)
	{
		printf("Case #%d: ",kase);
		sum=tmp=0;
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%d",&a[i]);
			tmp^=a[i];
			sum+=a[i];
		}
		if (tmp) printf("NO\n"); else
		{
			tmp=10000000;
			for (int i=1;i<=n;i++)
				if (a[i]<tmp) tmp=a[i];
			printf("%d\n",sum-tmp);
		}
	}
	
	return 0;
}
