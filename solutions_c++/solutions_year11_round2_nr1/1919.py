#include<cstdio>
#include<string.h>
using namespace std;

int T, N, wins[101], loses[101];
double WP[101], OWP[101], OOWP[101], RTI[101];
char table[101][101];

void init()
{
	for(int i = 0; i < N; i++)
	{
		wins[i] = 0;
		loses[i] = 0;
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&T);
	for(int cases = 1; cases <= T; cases++)
	{
		scanf("%d", &N);
		init();
		int i, j;

		for(i = 0; i < N; i++)
		{
			char str[101];
			scanf("%s",str);
			strcpy(table[i], str);
		}

		for(i = 0; i < N; i++)
		{
			for(j = 0; j < N; j++)
			{
				if(i==j)
					continue;
				if(table[i][j] == '1')
				{
					wins[i]++;
				}
				else if(table[i][j] == '0')
				{
					loses[i]++;
				}
			}
		}

		/*
		for(i = 0; i < N; i++)
		{
			printf("wins: %d loses: %d\n", wins[i], loses[i]);
		}
		*/
		/*for(i = 0; i < N; i++)
		{
			printf("%s", table[i]);
			printf("\n");
		}*/
		for(i = 0; i < N; i++)
		{
			WP[i] = 1.0*wins[i]/(wins[i]+loses[i]);
		}

		for(i = 0; i < N; i++)
		{
			double sum = 0;
			int opps = 0;
			for(j = 0; j < N; j++)
			{
				if(i == j)
					continue;
				if(table[i][j] == '1')
				{
					sum += 1.0*wins[j]/(wins[j]+loses[j] - 1);
					opps++;
				}
				else if(table[i][j] == '0')
				{
					sum += 1.0*(wins[j]-1)/(wins[j]+loses[j] - 1);
					opps++;
				}
			}
			OWP[i] = sum/opps;
		}

		for(i = 0; i < N; i++)
		{
			double sum = 0;
			int opps = 0;
			for(j = 0; j < N; j++)
			{
				if(i == j)
					continue;
				if(table[i][j] == '1')
				{
					sum += OWP[j];
					opps++;
				}
				else if(table[i][j] == '0')
				{
					sum += OWP[j];
					opps++;
				}
			}
			OOWP[i] = sum/opps;
		}

		printf("Case #%d:\n", cases);

		for(i = 0; i < N; i++)
		{
			RTI[i] = 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i];
			printf("%.7lf\n", RTI[i]);
		}
	}
	return 0;
}

		

