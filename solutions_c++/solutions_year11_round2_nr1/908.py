#include <cstdio>
#include <iostream>
using namespace std;

int main()
{
	FILE *fin=freopen ("p.in","r",stdin);
	FILE *fout=freopen ("p.out","w",stdout);

	int T,t;
	int n,i,j;
	char sch[110][110];
	int p[110],w[110];
	double x,wp[110],owp[110],oowp[110];

	fscanf (fin,"%d",&T);
	for(t=1;t<=T;t++)
	{
		fscanf (fin,"%d",&n);
		for(i=0;i<n;i++)
			fscanf(fin,"%s",sch[i]);

		for(i=0;i<n;i++)
		{
			p[i]=w[i]=0;
			for(j=0;j<n;j++)
			{
				if(sch[i][j]!='.')
					p[i]++;
				if(sch[i][j]=='1')
					w[i]++;
			}
			wp[i]=((double)w[i])/p[i];
		}

		for(i=0;i<n;i++)
		{
			owp[i]=0.0;
			for(j=0;j<n;j++)
			{
				if(sch[i][j]!='.')
				{
					if(sch[i][j]=='1')
						x=((double)w[j])/(p[j]-1);
					else
						x=((double)w[j]-1)/(p[j]-1);
					owp[i]+=x;
				}
			}
			owp[i]/=p[i];
		}
		for(i=0;i<n;i++)
		{
			oowp[i]=0.0;
			for(j=0;j<n;j++)
			{
				if(sch[i][j]!='.')
				{
					oowp[i]+=owp[j];
				}
			}
			oowp[i]/=p[i];
		}
		fprintf(fout,"Case #%d:\n",t);
		for(i=0;i<n;i++)
		{
			fprintf(fout,"%.8f\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
		}

	}
	return 0;
}