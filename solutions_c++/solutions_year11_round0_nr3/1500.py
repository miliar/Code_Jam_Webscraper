#include<cstdio>
#include<algorithm>
using namespace std;

int T,test,n;
int a[11111];

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C2.out","w",stdout);
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: ",test);
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",&a[i]);
		sort(a,a+n);
		long long sum=0;
		int xxor=0;
		for(int i=n-1;i>0;i--)
		{
			sum+=a[i];
			xxor^=a[i];
		}
		if(xxor!=a[0])
			puts("NO");
		else
			printf("%I64d\n",sum);
	}
	return 0;
}

