#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


main()
{
	int T,N,K,CASE=0;
	int i,j,k,p;

	int grid[105][105];

	double rpi[105];

	double wp[105];
	double owp[105];
	double oowp[105];

	char buf[1000];

	double t1,t2,t3,t4;

	int win,loss,total;

//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);

//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);


	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%d",&N);

		for(i=0; i<N; i++)
		{
			rpi[i] = 0.0;
			wp[i] = 0.0;
			owp[i] = 0.0;
			oowp[i] = 0.0;

			for(j=0; j<N; j++)
			{
				grid[i][j] = 0;
			}
		}

		for(i=0; i<N; i++)
		{
			scanf("%s",buf);

			for(j=0; j<N; j++)
			{
				if(buf[j] == '1')
				{
					grid[i][j] = 1;
				}
				else if(buf[j] == '0')
				{
					grid[i][j] = 0;
				}
				else if(buf[j] == '.')
				{
					grid[i][j] = -1;
				}
			}
		}

		for(i=0; i<N; i++)
		{
			//wp
			for(j=0,win=loss=0; j<N; j++)
				if(grid[i][j] == 1)
					win++;
				else if(grid[i][j] == 0)
					loss++;

			wp[i] = (double)win/(double)(win+loss);


			//owp
			t1 = 0.0;
			t2 = win+loss;
			for(j=0; j<N; j++)
				if(j != i && grid[i][j] != -1)
				{
					for(k=0,win=loss=0; k<N; k++)
					{
						if(k != i)
						{
							if(grid[j][k] == 1)
								win++;
							else if(grid[j][k] == 0)
								loss++;
						}
					}
					t1 = t1 + ((double)win/(double)(win+loss));
				}

			t1 = t1/t2;
			owp[i] = t1;
		}

		for(i=0; i<N; i++)
		{
			//oowp
			t1 = 0.0;

			for(j=0,win=loss=0; j<N; j++)
			{
				if(grid[i][j] == 1)
					win++;
				else if(grid[i][j] == 0)
					loss++;

				if(grid[i][j] != -1)
					t1 += owp[j];
			}

			t1 = t1/(double)(win+loss);
			oowp[i] = t1;
		}

		for(i=0; i<N; i++)
		{
			rpi[i] = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
		}


		printf("Case #%d:\n",CASE);

		for(i=0; i<N; i++)
		{
			printf("%f\n",rpi[i]);
		}

	}




}