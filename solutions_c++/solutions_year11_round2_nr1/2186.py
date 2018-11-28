#include<cstdio>
#include<memory>

using namespace std;

int mas[101][101];
double WP[101];
double OWP[101];
double OOWP[101];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	int i, j, k;
	int N;
	char c;
	for(i = 0; i<T; i++)
	{
		scanf("%d", &N);
		memset(mas, 0, sizeof(mas));
		getchar();
		for(k = 0; k<N; k++)
		{
			for(j = 0; j<N; j++)
			{
				c = getchar();
				if(c == '.')
				{
					mas[k][j] = -1;
				}
				if(c == '1')
				{
					mas[k][j] = 1;
				}
				if(c == '0')
				{
					mas[k][j] = 0;
				}
			}
			getchar();
		}
		double games, wins;
		for(k = 0; k<N; k++)
		{
			games = 0;
			wins = 0;
			for(j = 0; j<N; j++)
			{
				if(mas[k][j] == 1)
				{
					games++;
					wins++;
				}
				if(mas[k][j] == 0)
				{
					games++;
				}
			}
			WP[k] = wins/games;
		}
		double count;
		double sum;
		int l;
		for(k = 0; k<N; k++)
		{
			count = 0;
			sum = 0;
			for(j = 0; j<N; j++)
			{
				wins = 0;
				games = 0;
				if(mas[k][j] != -1)
				{
					count++;
					for(l = 0; l<N; l++)
					{
						if(mas[j][l] == 1 && l!=k)
						{
							games++;
							wins++;
						}
						if(mas[j][l] == 0 && l!=k)
						{
							games++;
						}
					}
					sum+=wins/games;
				}
			}
			OWP[k] = sum/count;
		}
		count = 0;
		sum = 0;
		for(k = 0; k<N; k++)
		{
			count = 0;
			sum = 0;
			for(j = 0; j<N; j++)
			{
				if(mas[k][j] != -1)
				{
					count++;
					sum+=OWP[j];
				}
			}
			OOWP[k] = sum/count;
		}
		printf("Case #%d:\n", i+1);
		/*puts("WP");
		for(k = 0; k<N; k++)
		{
			printf("%lf ", WP[k]);
		}
		puts("");
		puts("OWP");
		for(k = 0; k<N; k++)
		{
			printf("%lf ", OWP[k]);
		}
		puts("");
		puts("OOWP");
		for(k = 0; k<N; k++)
		{
			printf("%lf ", OOWP[k]);
		}*/
		for(k = 0; k<N; k++)
		{
			printf("%lf\n", 0.25*WP[k]+0.5*OWP[k]+0.25*OOWP[k]);
		}
	}
	return 0;
}
	