#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const long maxn = 210;

FILE *fin=fopen("b.in","r"),
	*fout=fopen("b.out","w");

long lk[maxn+1],dd[maxn+1],g[maxn+1][maxn+1],
	lian[2][maxn+1],done[2][maxn+1],cz[maxn+1],
	ga,gb,n,turnaround,resulta,resultb;

void calc(char s[],long &qq)
{
	long t;
	t=(s[0]-'0')*10+s[1]-'0';
	t=t*60+(s[3]-'0')*10+s[4]-'0';
	qq=t;
}

void init()
{
	long i,j;
	char s[100];
	fscanf(fin,"%ld",&turnaround);
	fscanf(fin,"%ld%ld",&ga,&gb);
	n=0;
	for (i=1; i<=ga; i++)
	{	
		++n;
		fscanf(fin,"%s",s);
		calc(s,lk[n]);
		fscanf(fin,"%s",s);
		calc(s,dd[n]);
		cz[n]=1;
	}
	for (i=1; i<=gb; i++)
	{	
		++n;
		fscanf(fin,"%s",s);
		calc(s,lk[n]);
		fscanf(fin,"%s",s);
		calc(s,dd[n]);
		cz[n]=2;
	}

	for (i=1; i<=n; i++)
		for (j=1; j<=n; j++)
		{
			g[i][j]=0;
			if (cz[i]!=cz[j])
				if (dd[i]+turnaround<=lk[j])
					g[i][j]=1;
		}
}

long ky(long p)
{
	long i;
	if (done[0][p])
		return 0;
	done[0][p]=1;
	for (i=1; i<=n; i++)
		if ((g[p][i])&&(!lian[1][i]))
		{
			lian[0][p]=i;
			lian[1][i]=p;
			return 1;
		}
	for (i=1; i<=n; i++)
		if ((g[p][i])&&(!done[1][i]))
		{
			done[1][i]=1;
			if (ky(lian[1][i]))
			{
				lian[0][p]=i;
				lian[1][i]=p;
				return 1;
			}
		}
	return 0;
}

void work()
{
	long i,j;
	for (i=1; i<=n; i++)
		lian[0][i]=lian[1][i]=0;
	resulta=ga;
	resultb=gb;
	for (i=1; i<=n; i++)
		if (!lian[0][i])
		{
			for (j=1; j<=n; j++)
				done[0][j]=done[1][j]=0;
			ky(i);
		}
	for (i=1; i<=n; i++)
		if (lian[1][i])
		{
			if (i<=ga)
				--resulta;
			else --resultb;
		}	
}


int main()
{
	long i,t;
	fscanf(fin,"%ld",&t);
	for (i=1; i<=t; i++)
	{
		init();
		work();
		fprintf(fout,"Case #%ld: %ld %ld\n",i,resulta,resultb);
	}
	fclose(fout);
	fclose(fin);
	return 0;
}