#include <stdio.h>
#include <memory.h>

int n;
char dat[1000][1000];

double wp[1000];
double owp[1000];
double oowp[1000];

int main()
{
	int t;
	FILE* fp=fopen("c:\\a-large.in","r"), *fp2=fopen("c:\\a-large.txt","w");
	fscanf(fp,"%d",&t);
	for (int T=1; T<=t; T++)
	{
		fscanf(fp,"%d",&n);
		for (int i=0; i<n; i++)
		{
			fscanf(fp,"%s",dat[i]);
		}

		for (int i=0; i<n; i++)
		{
			int total=0, win=0;
			for (int j=0; j<n; j++)
			{
				if (dat[i][j] == '1') total++, win++;
				else if (dat[i][j] == '0') total++;
			}
			wp[i] = (double)win / total;
		}

		for (int i=0; i<n; i++)
		{
			int total = 0;
			for (int j=0; j<n; j++)
			{
				if (dat[i][j] != '.')
				{
					int tot=0, win=0;
					total++;
					for (int k=0; k<n; k++)
					{
						if (k == i) continue;
						if (dat[j][k] == '1') tot++, win++;
						else if (dat[j][k] == '0') tot++;
					}
					owp[i] += (double)win / tot;
				}
			}
			owp[i] /= total;
		}

		for (int i=0; i<n; i++)
		{
			int total = 0;
			for (int j=0; j<n; j++)
			{
				if (dat[i][j] != '.')
				{
					total++;
					oowp[i] += owp[j];
				}
			}
			oowp[i] /= total;
		}
		fprintf(fp2,"Case #%d:\n", T);
		for (int i=0; i<n; i++)
		{
			fprintf(fp2,"%.6f\n", 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);
		}

		memset(owp,0,sizeof(owp));
		memset(oowp,0,sizeof(oowp));
	}
	return 0;
}