#include <stdio.h>
#include <algorithm>
using namespace std;
int a[10];
int b[10];
bool cmp(int x,int y)
{
	return x>y;
}
int gcd(int x,int y)
{
	return !y?x:gcd(y,x%y);
} 
int main()
{
	int T;
	scanf("%d",&T);
	for(int k=1;k<=T;k++)
	{
		int n;
		scanf("%d",&n);
		int i,j,p;
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		sort(a,a+n,cmp);
		int cnt=0;
		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				b[cnt++]=a[i]-a[j];
			}
		}
		int t=b[0];
		for(i=1;i<n*(n-1)/2;i++)
		{
			t=gcd(t,b[i]);
		}
		if(a[n*(n-1)/2-1]%t==0)
			p=t;
		else
			p=a[n*(n-1)/2-1]%t;
		printf("Case #%d: %d\n",k,t-p);
	}
	return 0;
}

