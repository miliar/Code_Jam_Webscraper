#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int t,n,m,p[1010];

int main()
{
	m=1;
	p[1]=2;
	for (int j=3;j<=1000;j++)
	{
		bool b=true;
		for (int i=1;i<=m && p[i]*p[i]<=j && b;i++)
			if (j%p[i]==0) b=false;
		if (b)
		{
			m++;
			p[m]=j;
		}
	}
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%d",&t);
	for (int tt=1;tt<=t;tt++)
	{
		scanf("%d",&n);
		int mi=0,ma=1;
		for (int i=1;i<=m;i++)
			if (p[i]<=n)
			{
				mi++;
				int k=p[i];
				while (k<=n)
				{
					ma++;
					k*=p[i];
				}
			}
		if (n==1) ma=mi;
//		cout<<mi<<" "<<ma<<endl;
		printf("Case #%d: %d\n",tt,ma-mi);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

