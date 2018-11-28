#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;

int scores[105][1000][3];
int scores_count[105];

main()
{
	int T,N,S,p,CASE=0;
	int t[200];
	int i,j,k;
	int a,b,c,d;
	int s;

	int res;

	int triplet[105][3];



	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);


	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%d %d %d", &N, &S, &p);

		for(i=0; i<N; i++)
			scanf("%d", &t[i]);

		for(i=0; i<N; i++)
		{
			scores_count[i] = 0;

			for(a=0; a<=10; a++)
				for(b=0; b<=10; b++)
					for(c=0; c<=10; c++)
					{
						if(a+b+c == t[i] && abs(a-b) <= 2 && abs(a-c) <= 2 && abs(b-c) <= 2)
						{
							scores[i][ scores_count[i] ][0] = a;
							scores[i][ scores_count[i] ][1] = b;
							scores[i][ scores_count[i] ][2] = c;

							scores_count[i]++;
						}
					}

		}

		res = 0;

		if(N == 1)
		{
			for(i=0; i<scores_count[0]; i++)
			{
				triplet[0][0] = scores[0][i][0];
				triplet[0][1] = scores[0][i][1];
				triplet[0][2] = scores[0][i][2];

				s = 0;

				if(abs(triplet[0][0]-triplet[0][1]) == 2 || abs(triplet[0][0]-triplet[0][2]) == 2 || abs(triplet[0][1]-triplet[0][2]) == 2)
					s = 1;

				if(s == S && (triplet[0][0] >= p || triplet[0][1] >= p || triplet[0][2] >= p))
					res = 1;

			}

		}
		else if(N == 2)
		{
			for(i=0; i<scores_count[0]; i++)
			{
				triplet[0][0] = scores[0][i][0];
				triplet[0][1] = scores[0][i][1];
				triplet[0][2] = scores[0][i][2];

				for(j=0; j<scores_count[1]; j++)
				{
					triplet[1][0] = scores[1][j][0];
					triplet[1][1] = scores[1][j][1];
					triplet[1][2] = scores[1][j][2];

					s = 0;
		
					for(k=0; k<N; k++)
						if(abs(triplet[k][0]-triplet[k][1]) == 2 || abs(triplet[k][0]-triplet[k][2]) == 2 || abs(triplet[k][1]-triplet[k][2]) == 2)
							s++;

					d = 0;

					if(s == S)
					{
						for(k=0; k<N; k++)
							if(triplet[k][0] >= p || triplet[k][1] >= p || triplet[k][2] >= p)
								d++;
					}

					if(d > res)
						res = d;

				}



			}

		}
		else if(N == 3)
		{
			for(i=0; i<scores_count[0]; i++)
			{
				triplet[0][0] = scores[0][i][0];
				triplet[0][1] = scores[0][i][1];
				triplet[0][2] = scores[0][i][2];

				for(j=0; j<scores_count[1]; j++)
				{
					triplet[1][0] = scores[1][j][0];
					triplet[1][1] = scores[1][j][1];
					triplet[1][2] = scores[1][j][2];

					for(a=0; a<scores_count[2]; a++)
					{
						triplet[2][0] = scores[2][a][0];
						triplet[2][1] = scores[2][a][1];
						triplet[2][2] = scores[2][a][2];
						
						s = 0;

			
						for(k=0; k<N; k++)
							if(abs(triplet[k][0]-triplet[k][1]) == 2 || abs(triplet[k][0]-triplet[k][2]) == 2 || abs(triplet[k][1]-triplet[k][2]) == 2)
								s++;

						d = 0;

						if(s == S)
						{
							for(k=0; k<N; k++)
								if(triplet[k][0] >= p || triplet[k][1] >= p || triplet[k][2] >= p)
									d++;
						}

						if(d > res)
							res = d;
					
					}

				}



			}

		}



		printf("Case #%d: %d\n",CASE, res);

	}




}