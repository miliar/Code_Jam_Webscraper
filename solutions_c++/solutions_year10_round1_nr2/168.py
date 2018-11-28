#include <iostream>
#include <math.h>
using namespace std;
const int maxint=2000000000;
int n,i,j,k,vd,vi,m,cases,ncase,best;
int a[110][260],va[260];
int dis[260][260];
int getmin(int x, int y)
{
	return ((x<y)?x:y);
}
int main()
{
	for (i=0; i<256; i++)
		for (j=0; j<256; j++)
			dis[i][j] = abs(i-j);
	freopen("B-large.in.txt","r",stdin);
	freopen("B-large.out.txt","w",stdout);
	cin >> cases;
	for (ncase=1; ncase<=cases; ncase++)
	{
		cin >> vd >> vi >> m >> n;
		for (i=1; i<=n; i++)
			for (j=0; j<=256; j++)
				a[i][j] = maxint;
		for (i=1; i<=n; i++)
			cin >> va[i];
		for (j=0; j<=255; j++)
			a[1][j] = dis[j][va[1]];
		a[1][256] = vd;
		for (i=2; i<=n; i++)
		{
			for (j=0; j<=255; j++)
			{
				a[i][j] = a[i-1][256];
				for (k=0; k<=255; k++)
				{
					if (dis[k][j]==0)
						a[i][j] = getmin(a[i][j],a[i-1][k]);
					else
					{
						if (m>0)
							a[i][j] = getmin(a[i][j],a[i-1][k]+((dis[k][j]-1)/m)*vi);
					}
				}
				a[i][j] = a[i][j]+dis[j][va[i]];
			}
			for (j=0; j<=256; j++)
				a[i][j] = getmin(a[i][j],a[i-1][j]+vd);
		}
		best = maxint;
		for (j=0; j<=256; j++)
			if (a[n][j]<best)
				best = a[n][j];
		cout << "Case #" << ncase << ": " << best << endl;
	}
	return 0;
}