# include <stdio.h>

int n,k,i,put,t,ok,j;

int main ()
{
	freopen ("snapper.in","r",stdin);
	freopen ("snapper.out","w",stdout);
	scanf ("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&k);
		ok=1;
		if (k==0)
			ok=0;
		else
		{
			put=1;
			for (j=1;j<=n;j++)
				put*=2;
			put-=1;
			if (k<put)
				ok=0;
			else
			{
				k-=put;
				put++;
				if (k%put!=0)
					ok=0;
			}
		}
		if (!ok)
		printf ("Case #%d: OFF\n",i);
		else printf ("Case #%d: ON\n",i);
	}
	return 0;
}