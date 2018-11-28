#include <stdio.h>

static int played[256][256];
static int won[256][256];

static int sum_played[256], sum_won[256];
static double wp[256], owp[256], oowp[256], rpi[256];

int main(int argc, char *argv[])
{
	int T, N;
	int t, i, j;
	double sum;
	char c;

	scanf("%d", &T);

	for ( t = 1; t <= T; t++ ) {
		scanf("%d\n", &N);
		
		//memset(played, 0, sizeof(played));
		
		//memset(wp, 0, sizeof(wp));
		//memset(owp, 0, sizeof(owp));
		//memset(oowp, 0, sizeof(oowp));
		//memset(rpi, 0, sizeof(rpi));

		for ( i = 0; i < N; i++ ) {
			wp[i] = owp[i] = oowp[i] = rpi[i] = 0;
			sum_played[i] = 0;
			sum_won[i] = 0;
			for ( j = 0; j < N; j++ ) {
				scanf("%c", &c);

				switch ( c ) {
				case '0':
					played[i][j] = 1;
					won[i][j] = 0;
					sum_played[i]++;
					break;
				case '1':
					played[i][j] = 1;
					won[i][j] = 1;
					sum_won[i]++;
					sum_played[i]++;
					break;
				default:
					played[i][j] = 0;
					won[i][j] = 0;
				}
			}
			scanf("\n");
			wp[i] = (double)sum_won[i] / sum_played[i];
		} 
		
		for ( i = 0; i < N; i++ ) {
			sum = 0;
			for ( j = 0; j < N; j++ ) {
				if ( played[i][j] ) {
					sum += (double)(sum_won[j] - won[j][i]) / (sum_played[j] - played[j][i]);
				}
			}
			owp[i] = sum / sum_played[i];
		}
		
		printf("Case #%d:\n", t);

		for ( i = 0; i < N; i++ ) {
			sum = 0;
			for ( j = 0; j < N; j++ ) {
				if ( played[i][j] ) {
					sum += owp[j];
				}
			}
			oowp[i] = sum / sum_played[i];
			rpi[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf("%.12lf\n", rpi[i]);
		}
	}
	return 0;
}
