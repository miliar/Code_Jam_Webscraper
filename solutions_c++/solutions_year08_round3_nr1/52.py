#include<stdio.h>
#include<algorithm>
using namespace std;

int p,k,l;
int a[1001];

int cmp(int a,int b)
{
	return a>b;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int T1,T,i;
	scanf("%d",&T);
	for(T1=1;T1<=T;T1++)
	{
		scanf("%d%d%d",&p,&k,&l);
		
		for(i=1;i<=l;i++)
		{
			scanf("%d",&a[i]);
		}
		sort(a+1,a+1+l,cmp);
		
		__int64 ans=0;
		for(i=1;i<=l;i++)
		{
			int times=(i-1)/k+1;
			ans+=(__int64)a[i]*times;
		}
		printf("Case #%d: %I64d\n",T1,ans);
	}
	return 0;
}