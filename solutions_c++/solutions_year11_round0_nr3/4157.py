#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
int a[1005];
int main()
{
	freopen("D:\\C-large.in","r",stdin);
	freopen("D:\\C-large.out","w",stdout);
	int flag=1,T,n,i,t,s;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",flag++);
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i]);
		}
		t=a[0];
		for(i=1;i<n;i++)
			t=(t^a[i]);
		if(t!=0)
			printf("NO\n");
		else
		{
			t=1000002;
			s=0;
			for(i=0;i<n;i++)
			{
				if(t>a[i]) t=a[i];
				s+=a[i];
			}
			printf("%d\n",s-t);
		}
	}
	return 0;
}