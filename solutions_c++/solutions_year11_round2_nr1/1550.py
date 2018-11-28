// May 21, 2011
// Author :: MIB


#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>


using namespace std;

const int MAX = 101;

char board[MAX][MAX];

int WP[MAX][2];
double OWP[MAX];
double OOWP[MAX];

int main(void)
{
	freopen ("C:\\Documents and Settings\\Mainul\\My Documents\\Downloads\\Codejam\\input\\A-large.in", "rt", stdin);
	freopen ("C:\\Documents and Settings\\Mainul\\My Documents\\Downloads\\Codejam\\output\\A-large.out", "wt", stdout);

	int t, T;
	int N, M;
	int i, j;

	scanf(" %d",&T);
	
	for(t=1; t<=T; t++)
	{
		scanf(" %d ", &N);

		for(i=0; i<N; i++) {
			gets(board[i]);
		}

		// memset(WP, 0, sizeof(WP));

		// WP
		for(i=0; i<N; i++) {
			WP[i][0] = 0;
			WP[i][1] = 0;
			
			for(j=0; j<N; j++) {
				
				if(board[i][j] == '0' || board[i][j] == '1')
				{
					WP[i][0]++;
					
					if(board[i][j] == '1')
						WP[i][1]++;
				}
			}

			// printf("%d / %d\n", WP[i][1], WP[i][0] );
		}


		// OWP
		int lob, hor, count;
		for(i=0; i<N; i++) {
			
			OWP[i] = 0;
			count = 0;

			for(j=0; j<N; j++) {
				
				if(board[i][j] != '.')
				{
					lob = WP[j][1];

					if(board[j][i] == '1')
						lob = WP[j][1] - 1;

					hor = WP[j][0] - 1;

					if(hor != 0)
						OWP[i] += (double)lob / (double)hor;
					count++;
				}
			}

			if(count != 0)
				OWP[i] = (double)OWP[i] / (double)count;
			// printf("%lf\n" ,OWP[i]);
		}


		printf( "Case #%d:\n", t);

		// OOWP
		for(i=0; i<N; i++) {

			OOWP[i] = 0;
			count = 0;

			for(j=0; j<N; j++) {

				if(board[i][j] != '.')
				{
					OOWP[i] += OWP[j];
					count++;
				}
			}

			
			if(count != 0)
				OOWP[i] = (double)OOWP[i] / (double)count;
			// printf("%lf\n" ,OOWP[i]);

			double RPI = 0;

			if(WP[i][0] > 0)
				RPI += 0.25 * ((double)WP[i][1] / (double)WP[i][0]);
			RPI += 0.50 * OWP[i];
			RPI += 0.25 * OOWP[i];
			printf("%0.10lf\n" ,RPI);
		}


	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
