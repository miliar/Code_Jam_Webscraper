#include <stdio.h>
#define MAXN 1000

char board[MAXN][MAXN];
double rpi[MAXN],owp[MAXN];
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,n,t;
	int i,j,k,d,m;
	double tmp;
	scanf("%d",&T);
	for (t = 1;t <= T;t++)
	{
		scanf("%d",&n);
		for (i = 0;i < n;i++)
			for (j = 0;j < n;j++)
				scanf(" %c",&board[i][j]);
		printf("Case #%d:\n",t);
		for (i = 0;i < n;i++)
		{
			d = m = 0;
			for(j = 0;j < n;j++){
				if(board[i][j] != '.')
					m++;
				if(board[i][j] == '1')
					d++;
			}
			rpi[i] = 0.25*d/m;
			tmp = 0;
			for (j = 0;j < n;j++)
			{
				if(board[i][j] == '.')continue;
				d = m = 0;
				for (k = 0;k < n;k++)
				{
					if(k == i)continue;
					if(board[j][k] != '.')
						m++;
					if(board[j][k] == '1')
						d++;
				}
				tmp += (d+0.0)/m;
			}
			m = 0;
			for (j = 0;j < n;j++)
				if(board[i][j] != '.')
					m++;
			owp[i] = tmp/m;
			rpi[i] += 0.5*tmp/m;
		}
		for(i = 0;i < n;i++){
			m = tmp = 0;
			for(j = 0;j < n;j++)
				if(board[i][j] != '.'){
					tmp += owp[j];
					m++;
				}
			rpi[i] += 0.25*tmp/m;
		}
		for(i = 0;i < n;i++)
			printf("%.10f\n",rpi[i]);
	}
	return 0;
}