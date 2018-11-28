#include <stdio.h>

int main() {

	int i, t;
	scanf("%d", &t);

	for ( i = 0; i < t; ++i ) {

		int n, j, k;
		scanf("%d", &n);

		int iwp[n];
		int jwp[n];
		long double wp[n];
		long double owp[n];
		long double oowp[n];

		for ( j = 0; j < n; ++j ) {

			iwp[j] = 0;
			jwp[j] = 0;
//			owp[j] = 0;
//			oowp[j] = 0;

		}

		int table[n][n];

		for ( j = 0; j < n; ++j ) {

			getchar();

			for ( k = 0; k < n; ++k )
				table[j][k] = getchar();

		}

		for ( j = 0; j < n; ++j )
			for ( k = 0; k < n; ++k )
				if ( table[j][k] == '1' )
					++iwp[j];
				else if ( table[j][k] == '0' )
					++jwp[j];

		for ( j = 0; j < n; ++j )
			wp[j] = (long double)iwp[j] / (iwp[j]+jwp[j]);

		for ( j = 0; j < n; ++j ) {

			long double o = 0;
			int count = 0;

			for ( k = 0; k < n; ++k ) {

				if ( j == k )
					continue;

				if ( table[j][k] != '.' ) {

					int aa = 1;

					if ( table[j][k] == '1' )
						aa = 0;

					o += (long double)(iwp[k] - aa) / (iwp[k]+jwp[k]-1);

//					printf("--- %d %d: +%LF\n", j, k, (long double)(iwp[k] - aa) / (iwp[k]+jwp[k]-aa));
//					o += wp[k];
					++count;

				}

			}

			owp[j] = o/count;

		}

		for ( j = 0; j < n; ++j ) {

			long double o = 0;
			int count = 0;

			for ( k = 0; k < n; ++k ) {

				if ( j == k )
					continue;

				if ( table[j][k] != '.' ) {

					o += owp[k];
					count++;

				}

			}

			oowp[j] = o / count;

		}

//		for ( j = 0; j < n; ++j )
//			printf("%d: %0.12LF %0.12LF %0.12LF\n", j, wp[j], owp[j], oowp[j]);

		printf("Case #%d:\n", i + 1);

		for ( j = 0; j < n; ++j )
			printf("%0.12LF\n", (0.25)*wp[j] + 0.5*owp[j] + 0.25*oowp[j]);

	}

	return 0;

}
