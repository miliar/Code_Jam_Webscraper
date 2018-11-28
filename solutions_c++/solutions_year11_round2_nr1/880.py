#include <cstdio>
#include <map>

using namespace std;

int main()
{
	map<int, int> WG;
	map<int, int> TG;

	map<int, double> WP;
	map<int, double> OWP;
	map<int, double> OOWP;
	
	int t;
	int n, i, j, k;
	int count0, count1;
	char str[101][101];

	scanf ("%d", &t);

	for ( k = 1; k <= t; k++ ) {
		scanf ("%d", &n);

		for ( j = 0; j < n; j++ ) {

			count0 = count1 = 0;

			scanf ("%s", str[j]);
			
			for ( i = 0; i < n; i++ ) {
				if ( str[j][i] == '0' )
					count0++;
				if ( str[j][i] == '1' )
					count1++;
			}
			
			WG[j] = count1;
			TG[j] = count0 + count1;
	
			WP[j] = (double)WG[j] / (double)TG[j];
		}

		for ( j = 0; j < n; j++ ) {
			double tp = 0.0;
			int c = 0;

			for ( i = 0; i < n; i++ ) {
				if ( str[j][i] == '0' || str[j][i] == '1' ) {
					tp += (double)(WG[i] - (str[i][j] == '1')) / (double)(TG[i] - 1);
					c++;
				}
			}

			OWP[j] = tp / c;
		}

		printf ("Case #%d:\n", k);

		for ( j = 0; j < n; j++ ) {
			double tp = 0.0;
			int c = 0;

			for ( i = 0; i < n; i++ ) {
				if ( str[j][i] == '0' || str[j][i] == '1' ) {
					tp += OWP[i];
					c++;
				}
			}

			OOWP[j] = tp / c;

			printf ("%.12g\n", (0.25 * WP[j]) + (0.5 * OWP[j]) + (0.25 * OOWP[j]));
		}
	}	
}
