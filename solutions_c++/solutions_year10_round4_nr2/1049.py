#include <stdio.h>

int getmin(int m[], int h, int t)
{
	int i,inc=0;
	if (h>=t) return 0;
	for (i=h; i<=t; i++)
	{
		if (m[i]>0)
		{
			m[i]--;
			inc=1;
		}
	}
	if (inc) return 1+getmin(m,h,(h+t)/2)+getmin(m,(h+t)/2+1,t);
	return 0;
}

int main()
{
	int t,p,cas,m[3999],i,j,pow[20];
	freopen("B-small-attempt2.in","r",stdin);
	freopen("b2.out","w",stdout);
	pow[0]=1;
	for (i=1; i<20; i++) pow[i]=pow[i-1]*2;
	scanf("%d",&t);
	for (cas=1; cas<=t; cas++)
	{
		scanf("%d",&p);
		for (i=p; i>=0; i--)
		{
			for (j=pow[i]-1; j<pow[i+1]-1; j++) scanf("%d",&m[j]);
		}
		for (j=pow[p]-1; j<pow[p+1]-1; j++) m[j]=p-m[j];
		printf("Case #%d: %d\n",cas,getmin(m,pow[p]-1,pow[p+1]-2));
	}
	return 0;
}

