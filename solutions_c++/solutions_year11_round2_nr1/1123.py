#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;
int mat[105][105];
int n;
double oppo[105],w[105],l[105],wp[105],owp[105],oowp[105];
void solve()
{
	scanf("%d",&n);
	for(int i = 1;i <= n;i++)
	{
		oppo[i] = 0.0;
		for(int j = 1;j <= n;j++)
		{
			char opt;
			scanf(" %c",&opt);
			switch(opt)
			{
				case '.':
					mat[i][j] = -1;
					//oppo[i] += 1;
					break;
				case '1':
					mat[i][j] = 1;
					oppo[i] += 1;
					break;
				case '0':
					mat[i][j] = 0;
					oppo[i] += 1;
					break;
			}
		}
	}
	double a[3] = {0.25,0.5,0.25};
	for(int i = 1;i <= n;i++)
	{
		w[i] = 0.0,l[i] = 0.0;
		for(int j = 1;j <= n;j++)
		{
			if(mat[i][j] == 0)
				l[i] += 1;
			else if(mat[i][j] == 1)
				w[i] += 1;
		}
		wp[i] = w[i] / oppo[i];
	}
	for(int i = 1;i <= n;i++)
	{
		double temp = 0.0;
		for(int j = 1;j <= n;j++)
		{
			if(mat[i][j] == 0)
				temp += (w[j] - 1) / (oppo[j] - 1);
			else if(mat[i][j] == 1)
				temp += w[j] / (oppo[j] - 1);
		}
		owp[i] = temp / oppo[i];
	}
	/*for(int i = 1;i <= n;i++)
	{
		printf("%d opp %lf win %lf wp %lf owp %lf oowp %lf\n",i,oppo[i],w[i],wp[i],owp[i],oowp[i]);
	}*/
	for(int i = 1;i <= n;i++)
	{
		double temp = 0.0;
		for(int j = 1;j <= n;j++)
		{
			if(mat[i][j] != -1)
				temp += owp[j];
		}
		oowp[i] = temp / oppo[i];
	}
	for(int i = 1;i <= n;i++)
		printf("%.10lf\n",a[0] * wp[i] + a[1] * owp[i] + a[2] * oowp[i]);
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i = 1;i <= t;i++)
	{
		printf("Case #%d:\n",i);
		solve();
	}
}
