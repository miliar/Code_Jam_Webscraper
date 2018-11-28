#include<cstdio>
#include<cstring>

char c[110][110];
int cor[110];
int total[110];
double A[110];
double B[110];
double C[110];
int main()
{
//	freopen("1.txt" , "r" , stdin);
//	freopen("2.txt" , "w" , stdout);
	int t;
	scanf("%d" , &t);
	int ii = 0;
	while(t--)
	{
		ii++;
		int n;
		scanf("%d" , &n);
		int i , j;
		for(i = 0;i < n;i++)
			scanf("%s" , &c[i]);
		for(i = 0;i < n;i++)
		{
			cor[i] = total[i] = 0;
			for(j = 0;j < n;j++)
			{
				if(c[i][j] == '1') cor[i]++;
				if(c[i][j] != '.') total[i]++;
			}
		}
		memset(A , 0 , sizeof(A));
		memset(B , 0 , sizeof(B));
		memset(C , 0 , sizeof(C));
		for(i = 0;i < n;i++)
		{
			A[i] = (double)cor[i] / total[i];
		}
		for(j = 0;j < n;j++)
		{
			int cal = 0;
			for(i = 0;i < n;i++)
			{
				if(c[i][j] == '0')
					B[j] += (double)cor[i] / (total[i] - 1);
				if(c[i][j] == '1')
					B[j] += (double)(cor[i] - 1) / (total[i] - 1);
				if(c[i][j] != '.')
					cal++;
			}
			B[j] /= cal;
		}
		for(i = 0;i < n;i++)
		{
			int cal = 0;
			for(j = 0;j < n;j++)
			{
				if(c[i][j] != '.')
				{
					C[i] += B[j];
					cal++;
				}
			}
			C[i] /= cal;
		}
		printf("Case #%d:\n" , ii);
		for(i = 0;i < n;i++)
		{
			printf("%.12lf\n" , 0.25 * A[i] + 0.5 * B[i] + 0.25 * C[i]);
		}
	}
	return 0;
}