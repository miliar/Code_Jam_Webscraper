#include<stdio.h>
#include<algorithm>
using namespace std;
int a[50];
int ans,n;
int main()
{
	int _,t;
	char s[99];
	scanf("%d",&_);
	for(t=1; t<=_; t++)
	{
		scanf("%d",&n);
		for(int i=0; i<n; i++)
		{
			scanf("%s",s);
			for(a[i]=n-1; a[i] && s[a[i]]=='0'; a[i]--);
		}
		ans=0;
		for(int i=0,j; i<n; i++)
		{
			for(j=i; j<n; j++)
				if(a[j]<=i)
					break;
			ans+=j-i;
			for(int k=j; k>i; k--)
				swap(a[k],a[k-1]);
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
