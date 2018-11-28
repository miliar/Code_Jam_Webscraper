#include <stdio.h>
#define N 110
double d[N], w[N], r[N];
char m[N][N];
int main()
{
	int i, j, k, l, h, n, t, ts;
	double a, s;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d", &n), i=0; i<n; scanf("%s", m[i]), i++);
		for(s=0, i=0; i<n; i++)
		{
			for(w[i]=0, d[i]=0, k=0, j=0; j<n; j++)
				if(m[i][j]!='.')
				{
					w[i]+=m[i][j]=='1';
					for(a=0, h=0, l=0; l<n; l++)
						if(l!=i && m[j][l]!='.')
						{
							a+=m[j][l]=='1';
							h++;
						}
					if(h>0) d[i]+=a/h;
					k++;
				}
			if(k>0) { w[i]/=k; d[i]/=k; }
		}
		for(i=0; i<n; i++)
		{
			for(r[i]=0, k=0, j=0; j<n; j++)
				if(m[i][j]!='.') { r[i]+=d[j]; k++; }
			if(k>0) r[i]/=k;
		}
		for(printf("Case #%d:\n", t+1), i=0; i<n; printf("%.13lf\n", w[i]*0.25+d[i]*0.5+r[i]*0.25), i++);
	}
	return 0;
}