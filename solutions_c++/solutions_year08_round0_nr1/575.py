#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const long maxm = 1010;
const long maxn = 1010;
const long maxlen = 210;

char machine[maxm+1][maxlen+1],engine[maxn+1][maxlen+1];
long yh[maxm+1][maxn+1],f[maxm+1][maxn+1],m,n,result;
bool ky[maxm+1][maxn+1];

FILE *fin=fopen("a.in","r"),
	*fout=fopen("a.out","w");

void init()
{
	long i,j;
	char s[maxlen+1];
	fscanf(fin,"%ld",&n);
	fgets(s,maxlen,fin);
	for (i=1; i<=n; i++)
	{
		fgets(s,maxlen,fin);
		j=strlen(s);
		if (s[j-1]=='\n')
			s[j-1]='\0';
		strcpy(machine[i],s);
	}
	fscanf(fin,"%ld",&m);
	fgets(s,maxlen,fin);
	for (i=1; i<=m; i++)
	{
		fgets(s,maxlen,fin);
		j=strlen(s);
		if (s[j-1]=='\n')
			s[j-1]='\0';
		strcpy(engine[i],s);
	}
}

void calc_yh(long i)
{
	long j,zx,zx2;
	zx=zx2=-1;
	for (j=1; j<=n; j++)
		if ((zx==-1)||(f[i][j]<zx))
		{
			zx2=zx;
			zx=f[i][j];
		}
		else if ((zx2==-1)||(f[i][j]<zx2))
			zx2=f[i][j];
	for (j=1; j<=n; j++)
		if (f[i][j]==zx)
			yh[i][j]=zx2;
		else yh[i][j]=zx;
}

void work()
{
	long i,j,k;
	for (i=1; i<=m; i++)
		for (j=1; j<=n; j++)
			if (strcmp(engine[i],machine[j]) == 0)
				ky[i][j]=false;
			else ky[i][j]=true;

	for (i=1; i<=n; i++)
		if (ky[1][i])
			f[1][i]=0;
		else f[1][i]=-1; //cannot do it

	calc_yh(1);

	for (i=2; i<=m; i++)
	{
		for (j=1; j<=n; j++)
		{
			f[i][j]=-1;
			if ((ky[i][j])&&(f[i-1][j]!=-1))
				f[i][j]=f[i-1][j];
			if (yh[i-1][j]!=-1)
				if ((f[i][j]==-1)||(yh[i-1][j]+1<f[i][j]))
					f[i][j]=yh[i-1][j]+1;
		}
		calc_yh(i);
	}
}

void output()
{
	long i;
	result = -1;
	for (i=1; i<=n; i++)
		if (f[m][i]!=-1)
			if ((result==-1)||(f[m][i]<result))
				result=f[m][i];

}

int main()
{
	long i,t;
	fscanf(fin,"%ld",&t);
	for (i=1; i<=t; i++)
	{
		init();
		work();
		output();
		fprintf(fout,"Case #%ld: %ld\n",i,result);
	}
	fclose(fin);
	fclose(fout);
	return 0;
}