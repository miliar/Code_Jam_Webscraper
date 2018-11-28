#include<stdio.h>
#include<string.h>
int main()
{
	int i, j;
	char map[200][200];
	double WP[200];
	double OWP[200];
	double OOWP[200];
	int N;
	int k;
	int T;
	scanf("%d", &T);
	for ( int t = 1 ; t <= T ; t++ ) {
		memset(WP,0,sizeof(WP));
		memset(OWP,0,sizeof(OWP));
		memset(OOWP,0,sizeof(OOWP));
		scanf("%d", &N);
		for ( i = 0 ; i < N ; i++ ) {
			scanf("%s", map[i]);
		}
		
		for ( i = 0 ; i < N ; i++ ) {
			double RPI = 0;
			double s = 0.0;
			double w = 0.0;
			for ( j = 0 ; j < N ; j++ ) {
				if ( map[i][j] == '1' ) {
					w++;
					s++;
				}
				else if ( map[i][j] == '0' ) {
					s++;
				}
			}
			WP[i] = w/s;
		}

		for ( i = 0 ; i < N ; i++ ) {
			double count = 0;
			for ( j = 0 ; j < N ; j++ ) {
				if ( map[i][j] != '.' ) { 
					count++;
					double s = 0.0;
					double w = 0.0;
					for ( k = 0 ; k < N ; k++ ) {
						if ( k!=i ) {
							if ( map[j][k] == '1' ) {
								s++;
								w++;
							}
							else if ( map[j][k] == '0' ) {
								s++;
							}
						}
					}
					OWP[i] += w/s;
				}
			}
			OWP[i]/=count;
		}
		
		for ( i = 0 ; i < N ; i++ ) {
			double count = 0;
			for ( j = 0 ; j < N ; j++ ) {
				if ( map[i][j] != '.' ) { 
					count++;
					OOWP[i] += OWP[j];
				}
			}
			OOWP[i]/=count;
		}
		printf("Case #%d:\n", t);
		for ( i = 0 ; i < N ; i++ ) {
			printf("%.12lf\n", 0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
		}
	}
			
				
	
	return 0;
}