#include<cstdio>
int x[1001];
int m;
int main()
{
	int n,ans;
	int a,b,c,d;
	scanf("%d",&m);
	for(int i=1;i<=m;i++)
	{
		ans=0;
		scanf("%d%d",&a,&b);
		for(int j=a;j<=b;j++)
		{
			n=1;
			c=j;
			while(c>=10)
			{
				c=c/10;
				n++;
			}
			c=j;
			while(1)
			{
				d=c%10;
				for(int q=1;q<n;q++) d=d*10;
				c=c/10+d;
				if(j!=c&&c<=b&&c>=a) ans++;
				if(c==j) break;
			}
		}
		ans=ans/2;
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
