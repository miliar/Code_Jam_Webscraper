#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

#define MAX 600

#define EPS 1e-6

long long int mx[MAX][MAX];
long long int my[MAX][MAX];
long long int s[MAX][MAX];
int mat[MAX][MAX];

int main()
{
		int n,m;
		int d;
		int t,ccnt;

		scanf("%d",&t);

		for(ccnt=1;ccnt<=t;++ccnt)
		{
				scanf("%d %d %d",&n,&m,&d);
				int i,j,k;

				for(i=1;i<=n;++i)
						for(j=1;j<=m;++j)
						{
								scanf("%1d",&mat[i][j]);
								mat[i][j]+=1;
						}

				for(i=0;i<=n;++i)
						for(j=0;j<=m;++j)
								mx[i][j]=my[i][j]=s[i][j]=0;

				for(i=1;i<=n;++i) for(j=1;j<=m;++j)
				{
						mx[i][j]=mx[i-1][j]+mx[i][j-1]-mx[i-1][j-1]+mat[i][j]*i;
						my[i][j]=my[i-1][j]+my[i][j-1]-my[i-1][j-1]+mat[i][j]*j;
						s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+mat[i][j];
				}

				for(k=min(n,m);k>2;--k)
				{
						for(i=1;i<=n-k+1;++i) for(j=1;j<=m-k+1;++j)
						{
								double xcm = mx[i+k-1][j+k-1]-mx[i-1][j+k-1]-mx[i+k-1][j-1]+mx[i-1][j-1];
								double ycm = my[i+k-1][j+k-1]-my[i-1][j+k-1]-my[i+k-1][j-1]+my[i-1][j-1];
								xcm -= (mat[i][j+k-1]+mat[i][j])*i + (mat[i+k-1][j]+mat[i+k-1][j+k-1])*(i+k-1);
								ycm -= (mat[i][j]+mat[i+k-1][j])*j + (mat[i][j+k-1]+mat[i+k-1][j+k-1])*(j+k-1);
								double soma = s[i+k-1][j+k-1]-s[i-1][j+k-1]-s[i+k-1][j-1]+s[i-1][j-1];
								soma -=mat[i][j]+mat[i+k-1][j] + mat[i][j+k-1]+mat[i+k-1][j+k-1];

								xcm = xcm/soma;
								ycm = ycm/soma;
								if (fabs(xcm-i-(k-1)/(double)2) < EPS &&
								    fabs(ycm-j-(k-1)/(double)2) < EPS)
										goto sucesso;
						}
				}

sucesso:
				if(k<3)
						printf("Case #%d: IMPOSSIBLE\n",ccnt);
				else
						printf("Case #%d: %d\n",ccnt,k);

		}
		return 0;
}






