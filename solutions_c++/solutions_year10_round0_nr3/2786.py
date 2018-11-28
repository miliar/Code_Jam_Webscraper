# include <stdio.h>
int Q[4005];
int epr[100000005];
int ini[4005];
int sf,inc,gr,t,in,i,j,ok,Euro,h,round;
int n[55],k[55],r[55];


int main ()
{
	freopen ("input.in","r",stdin);
	freopen ("input.out","w",stdout);
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d%d%d",&r[i],&k[i],&n[i]);
		Euro=0; 
		round=0;
		inc=0; sf=n[i]-1;
		for(j=0;j<n[i];j++)
			{scanf("%d",&Q[j]);ini[j]=Q[j];}
		for (j=1;j<=r[i];j++)
		{
			inc=0;
			sf=n[i]-1;
			in=0;
			gr=0;
			while (in+Q[inc]<=k[i]&&gr<n[i])
			{
				in+=Q[inc];
				gr++;
				sf++; Q[sf]=Q[inc]; inc++;
			}
			ok=0;
			for (h=inc;h<=sf;h++)
			{
				Q[h-inc]=Q[h];
				if (Q[h-inc]!=ini[h-inc])
					ok=1;
			}
			Euro+=in;
			if (ok)
			{
				round++;
				epr[round]=Euro;
			}
			else
			{
				round++;
				Euro=Euro*(r[i]/round)+epr[r[i]%round];
				j=r[i]+1;
			}
		}
		printf ("Case #%d: %d\n",i,Euro);
	}
	return 0;
}