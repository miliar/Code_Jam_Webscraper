#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cmath>

int T;

int main()
{
	scanf("%d", &T);
	
	for(int i = 1; i <= T; i++)
	{
		int R, K, N;
		int groups[1000];
		int res[1000][2];

		for(int j = 0; j < 1000; j++)
		{
			res[j][0] = 0;
			res[j][1] = j;
		}

		unsigned long long euros = 0;
		
		scanf("%d%d%d", &R, &K, &N);
		
		for(int j = 0; j < N; j++)
		{
			scanf("%d", &groups[j]);
		}
		
		for(int debut = 0; debut < N; debut++)
		{
			int Krestant = K-groups[debut];
			if(Krestant <= 0)
			{
				if(Krestant == 0)
				{
					res[debut][0] += groups[debut];
				}
				res[debut][1] = (debut+(Krestant==0))%N;
				continue;
			}

			res[debut][0] += groups[debut];

			for(int fin = (debut+1)%N; fin != debut; fin=(fin+1)%N)
			{
				Krestant -= groups[fin];
				if(Krestant <= 0)
				{
					if(Krestant == 0)
					{
						res[debut][0] += groups[fin];
					}
					res[debut][1] = (fin+(Krestant==0))%N;
					break;
				}

				res[debut][0] += groups[fin];
			}
			
			//printf("debut : %d, euros => %d, next => %d\n",debut,res[debut][0], res[debut][1]);
		}

		int pos = 0;
		
		for(int j = 0; j < R; j++)
		{
			euros += res[pos][0];
			pos = res[pos][1];
		}
		
		printf("Case #%d: %llu\n", i, euros);
	}
}

