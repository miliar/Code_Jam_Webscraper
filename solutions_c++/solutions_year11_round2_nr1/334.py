#include <cstdio>
#include <algorithm>
using namespace std;

int M[109][109];
int played[109];
int won[109];
double wp[109];
double owp[109];
double oowp[109];

int main()
{
	int T;
	scanf("%d", &T);
	for (int Ti = 1; Ti <= T; Ti++)
	{
		//input
		int N;
		scanf("%d ", &N);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
			{
				char c;
				scanf("%c ", &c);
				if (c == '.') M[i][j] = -1;
				else M[i][j] = (c - '0');
			}
		
		//played and won
		for (int i = 0; i < N; i++)
		{
			played[i] = 0;
			won[i] = 0;
			for (int j = 0; j < N; j++)
			{
				if (M[i][j] != -1) played[i]++;
				if (M[i][j] == +1) won[i]++;
			}
			wp[i] = 1.0 * won[i] / played[i];
		}
		
		//owp
		for (int i = 0; i < N; i++)
		{
			double sum = 0;
			for (int j = 0; j < N; j++)
				if (M[i][j] != -1)
				{
					//if i won, it's the wp of j
					if (M[i][j] == 1) sum += 1.0 * won[j] / (played[j] - 1);
					//else you have to recalculate
					else sum += 1.0 * (won[j] - 1) / (played[j] - 1);
				}
			
			owp[i] = 1.0 * sum / played[i];
		}
		
		//oowp
		for (int i = 0; i < N; i++)
		{
			double sum = 0;
			for (int j = 0; j < N; j++)
				if (M[i][j] != -1)
				  sum += owp[j];
			
			oowp[i] = 1.0 * sum / played[i];
		}
		
		printf("Case #%d:\n", Ti);
		for (int i = 0; i < N; i++)
			//printf("%f (%f, %f, %f)\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i], wp[i], owp[i], oowp[i]);
			printf("%f\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
	}
	return 0;
}