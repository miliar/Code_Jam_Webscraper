#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
int n;
int tot;
int main()
{
	int t;
	char mat[110][110];
	int venceu[110];
	int total[110];
	double wp[110][110], owp[110], oowp[110];
	scanf("%d",&t);
	for(int c = 0; c < t; c++)
	{
		memset(venceu, 0, sizeof(venceu));
		memset(total, 0, sizeof(total));
		scanf("%d",&n);
		for(int j = 0; j < n; j++)
		{
			scanf("%s",mat[j]);
		}
		int cont = 0, cont2 = 0;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(mat[i][j] != '.')
				{
					cont++;
					if(mat[i][j] == '1')
						cont2++;
				}
			}
			venceu[i] = cont2;
			total[i] = cont;
			wp[n][i] = (double)cont2/(double)cont;
			cont = cont2 = 0;
		}
		for(int k = 0; k < n; k++)
		{
			for(int i = 0; i < n; i++)
			{
				if(i == k)
					continue;
				for(int j = 0; j < n; j++)
				{
					if(j == k)
						continue;
					if(mat[i][j] != '.')
					{
						cont++;
						if(mat[i][j] == '1')
							cont2++;
					}
				}
				wp[k][i] = (double)cont2/(double)cont;
				cont = cont2 = 0;
			}
		}
		double tot = 0;
		cont = 0;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				if(i != j && mat[i][j] != '.')
				{
					tot += wp[i][j];
					cont++;
				}
			}
			tot /= cont;
			owp[i] = tot;
			tot = 0;
			cont = 0;
		}
		cont = 0;
		tot = 0;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < n; j++)
			{
				//if(mat[i][j] != '.')
				if(i != j && mat[i][j] != '.')
				{
					tot += owp[j];
					cont++;
				}
			}
			tot /= cont;
			oowp[i] = tot;
			tot = 0;
			cont = 0;
		}
		printf("Case #%d:\n",c+1);
		for(int i = 0; i < n; i++)
		{
			printf("%.7lf\n",wp[n][i]*0.25 + owp[i]*0.5 + oowp[i]*0.25);
		}
	}
	return 0;
}
