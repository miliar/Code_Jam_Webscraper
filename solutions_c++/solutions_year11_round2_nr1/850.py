
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define  max(x, y)  ((x)>(y)?(x):(y))
#define  abs(x)   ((x)<0?-(x):(x))

char buf[1024];

typedef  long long  int64;


// int _tmain(int argc, _TCHAR* argv[])
int main()
{
	gets(buf);
	int ncase = atoi(buf);
//	printf("%d\n", ncase);
  
	for(int i=1; i<=ncase; i++)
	{
		char  sched[200][200];
		int  N = 0;

		int  Ans = 0;
		scanf("%d", &N);

		for(int j=0; j<N; j++)
		{
			scanf("%s", sched[j]);
		}

		double WP[100];
		double WP2[100][100];
		double OWP[100];
		double OOWP[100];
		double RPI[100];

		for(int j=0; j<N; j++)
		{
			int  cnt = 0;
			int  win = 0;
			for(int k=0; k<N; k++)
			{
				if ( sched[j][k] == '1' )
					win ++;
				if ( sched[j][k] != '.' )
					cnt ++;
			}
			WP[j] = ((double)win)/((double)cnt);
		}

		for(int l=0; l<N; l++)
		{
			for(int j=0; j<N; j++)
			{
				if ( j == l )
					continue;
				int  cnt = 0;
				int  win = 0;
				for(int k=0; k<N; k++)
				{
					if ( k == l )
						continue;
					if ( sched[j][k] == '1' )
						win ++;
					if ( sched[j][k] != '.' )
						cnt ++;
				}
				WP2[j][l] = ((double)win)/((double)cnt);
			}
		}

		for(int j=0; j<N; j++)
		{
			double  owp = 0.0;
			int  cnt = 0;
			for(int k=0; k<N; k++)
			{
				if ( sched[j][k] == '.' )
					continue;
				owp += WP2[k][j];
				cnt ++;
			}
			OWP[j] = owp/cnt;
		}

		for(int j=0; j<N; j++)
		{
			double  oowp = 0.0;
			int  cnt = 0;
			for(int k=0; k<N; k++)
			{
				if ( sched[j][k] == '.' )
					continue;
				oowp += OWP[k];
				cnt ++;
			}
			OOWP[j] = oowp/cnt;
		}

		for(int j=0; j<N; j++)
		{
			RPI[j] = 0.25*WP[j] + 0.5*OWP[j] + 0.25*OOWP[j];
		}

		printf("Case #%d:\n", i);
		for(int j=0; j<N; j++)
			printf("%.12g\n", RPI[j] );
	}
  
	return  0;  
}

