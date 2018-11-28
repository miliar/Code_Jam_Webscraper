#include<cstdio>
int x[1001];
int m;
int main()
{
	int n,s,p,ans,bns;
	int a,b;
	scanf("%d",&m);
	for(int i=1;i<=m;i++)
	{
		ans=0;
		bns=0;
		scanf("%d%d%d",&n,&s,&p);
		a=3*p-2;
		b=3*p-4;
		if(b<0) b=100000;
		for(int j=0;j<n;j++) 
		{
			scanf("%d",&x[j]);
			if(x[j]>=a) ans++;
			if(x[j]<a&&x[j]>=b) bns++;
		}
		if(s>=bns) ans=ans+bns;
		else ans=ans+s;
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
