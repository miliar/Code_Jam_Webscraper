#include <stdio.h>

double RPI[1000];
double WP[1000];
double OWP[1000];
double OOWP[1000];
double WP_except[1000][1000];

void calc_WP_except(int map[][1000], int N)
{
    for(int k = 0; k < N; k++)
    {
    
	for(int i = 0; i < N; i++)
	{
	    double games = 0;
	    double wins = 0;

	    for(int j = 0; j < N; j++)
	    {
		if(map[i][j] == 1 && j != k)
		{
		    games++;
		    wins++;
		}
		if(map[i][j] == 0 && j != k)
		{
		    games++;
		}
	    }

	    WP_except[i][k] = wins / games;
	}
    }
}

void calc_WP(int map[][1000], int N)
{
    for(int i = 0; i < N; i++)
    {
	double games = 0;
	double wins = 0;

	for(int j = 0; j < N; j++)
	{
	    if(map[i][j] == 1)
	    {
		games++;
		wins++;
	    }
	    if(map[i][j] == 0)
	    {
		games++;
	    }
	}

	WP[i] = wins / games;
    }
}

void calc_OWP(int map[][1000], int N)
{
    for(int i = 0; i < N; i++)
    {
	double numgames = 0;
	double sum = 0;
	
	for(int j = 0; j < N; j++)
	{
	    if(map[i][j] == 1 || map[i][j] == 0)
	    {
		numgames++;
		sum += WP_except[j][i];
	    }
	}

	OWP[i] = sum / numgames;
    }
}

void calc_OOWP(int map[][1000], int N)
{
    for(int i = 0; i < N; i++)
    {
	double num = 0;
	double sum = 0;

	for(int j = 0; j < N; j++)
	{
	    if(map[i][j] == 1 || map[i][j] == 0)
	    {
		num++;
		sum += OWP[j];
	    }
	}

	OOWP[i] = sum / num;
    }
}

void calc_RPI(int map[][1000], int N)
{
    for(int i = 0; i < N; i++)
	RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
}

int main()
{
    int T, N;
    int map[1000][1000];
    
    scanf("%d", &T);

    for(int test = 1; test <= T; test++)
    {
	scanf("%d\n", &N);

	for(int i = 0; i < N; i++)
	{
	    for(int j = 0; j < N; j++)
	    {
		char c;
		scanf("%c", &c);
//		printf("c: %c", c);
		if(c == '1')
		    map[i][j] = 1;
		if(c == '0')
		    map[i][j] = 0;
		if(c == '.')
		    map[i][j] = -1;
	    }
	    scanf("\n");
	}

	calc_WP(map, N);
	calc_WP_except(map, N);
	calc_OWP(map, N);
	calc_OOWP(map, N);
	calc_RPI(map, N);

	printf("Case #%d:\n", test);

	for(int i = 0; i < N; i++)
	{
	    printf("%lf\n", RPI[i]);
	}
    }

    return 0;
}
