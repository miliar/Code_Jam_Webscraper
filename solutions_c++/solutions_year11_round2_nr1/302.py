#include <stdio.h>

char t[666][666];
int cases, n, g[666], w[666];
double wp[666], xwp[666][666], owp[666], oowp[666];

int main()
{
	scanf(" %d", &cases);
	for(int cs=1; cs<=cases; cs++)
	{
		scanf(" %d", &n);
		for(int i=0; i<n; i++)
			scanf(" %s", t[i]);

		for(int i=0; i<n; i++)
		{
			g[i]=w[i]=0;
			for(int j=0; j<n; j++)
			{
				if (t[i][j]!='.') g[i]++;
				if (t[i][j]=='1') w[i]++;
			}
		}
		for(int i=0; i<n; i++)
			wp[i]=double(w[i])/double(g[i]);
		for(int i=0; i<n; i++)
		{
			owp[i]=0;
			for(int j=0; j<n; j++)
			{
				xwp[j][i]=0;
				if (t[j][i]!='.')
					xwp[j][i]=double(w[j]-(!!(t[j][i]=='1')))/double(g[j]-1);
				owp[i]+=xwp[j][i];
			}
			owp[i]/=g[i];
		}
		for(int i=0; i<n; i++)
		{
			oowp[i]=0;
			for(int j=0; j<n; j++)
				if (t[i][j]!='.')
					oowp[i]+=owp[j];
			oowp[i]/=g[i];
		}
		
		printf("Case #%d:\n", cs);
		for(int i=0; i<n; i++)
		{
			printf("%.12g\n",
						 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]
						 );
		}
	}
}
