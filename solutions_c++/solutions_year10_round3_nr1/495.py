#include<cstdio>

const int maxn=1000+10;
int a[maxn],b[maxn];
int n,res,test;

int main()
{
	scanf("%d",&test);
	for (int t=1;t<=test;t++)
	{
		scanf("%d",&n);
		for (int i=0;i<n;i++) scanf("%d%d",&a[i],&b[i]);
		res=0;
		for (int i=0;i<n;i++)
		for (int j=0;j<i;j++)
			res+=((a[i]<a[j] && b[i]>b[j]) || (a[i]>a[j] && b[i]<b[j]));
		printf("Case #%d: %d\n",t,res);
	}
}
