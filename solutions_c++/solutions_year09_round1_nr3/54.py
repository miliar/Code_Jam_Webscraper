#include<stdio.h>
#include<string.h>
#include<memory.h>
int n, m;
__int64 c[64][64];
double d[64];
double w[64][64];
double p[64];
int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	int i, j;
	for(i=0;i<=50;i++)
	{
		c[i][0]=c[i][i]=1;
		for(j=1;j<i;j++) c[i][j]=c[i-1][j-1]+c[i-1][j];
	}
	int t, tc;
	fscanf(fp, "%d", &tc);
	for(t=1;t<=tc;t++)
	{
		fscanf(fp, "%d%d", &n, &m);
		memset(d, 0, sizeof(d));
		memset(w, 0, sizeof(w));
		memset(p, 0, sizeof(p));
		for(i=0;i<n;i++)
		{
			for(j=0;j<=m;j++)
				w[i][i+j]=(double)(c[i][m-j])*(double)(c[n-i][j])/(double)(c[n][m]);
			for(j=1;j<=m;j++) w[i][i+j]/=(1.0-w[i][i]);
		}
		p[0]=1.0;
		for(i=0;i<n;i++)
		{
			for(j=1;j<=m;j++)
			{
				p[i+j]+=p[i]*w[i][i+j];
			}
		}
		for(i=1;i<=n;i++)
		{
			if(!p[i]) continue;
			for(j=1;j<=m && j<=i;j++) d[i]+=p[i-j]*w[i-j][i]*(d[i-j]+1.0/(1.0-w[i-j][i-j]));
			d[i]/=p[i];
		}
		fprintf(ofp, "Case #%d: %.7lf\n", t, d[n]);
	}
	return 0;
}
