//For Future
//By JFantasy

#include <cstdio>
#include <cstring>

const int maxn = 105;

char str[maxn][maxn];
int n;
double wp[maxn] , owp[maxn] , oowp[maxn];

int main() {
	int cas , T = 0;
	scanf( "%d" , &cas );
	while ( cas-- ) {
		memset( wp , 0 , sizeof(wp) );
		memset( owp , 0 , sizeof(owp) );
		memset( oowp , 0 , sizeof(oowp) );
		scanf( "%d" , &n );
		for ( int i = 0; i < n; i++ ) scanf( "%s" , str[i] );
		for ( int i = 0; i < n; i++ ) {
			int t1 = 0 , t2 = 0;
			for ( int j = 0; j < n; j++ ) {
				t1 += str[i][j] == '1';
				t2 += str[i][j] == '0';
			}
			wp[i] = double(t1)/double(t1+t2);
//			printf( "%lf\n" , wp[i] );
		}
		for ( int i = 0; i < n; i++ ) {
			int t = 0;
			for ( int j = 0; j < n; j++ ) {
				if ( str[i][j] == '.' ) continue;
				t++;
				int t1 = 0 , t2 = 0;
				for ( int h = 0; h < n; h++ ) {
					if ( i == h ) continue;
					t1 += str[j][h] == '1';
					t2 += str[j][h] == '0';
				}
				owp[i] += double(t1)/double(t1+t2);
			}
			if ( t ) owp[i] /= double(t);
//			printf( "%lf\n" , owp[i] );
		}
		for ( int i = 0; i < n; i++ ) {
			int t = 0;
			for ( int j = 0; j < n; j++ ) {
				if ( str[i][j] == '.' ) continue;
				t++;
				oowp[i] += owp[j];
			}
			if ( t ) oowp[i] /= double(t);
//			printf( "%lf\n" , oowp[i] );
		}
		printf( "Case #%d:\n" , ++T );
		for ( int i = 0; i < n; i++ ) printf( "%.12lf\n" , 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i] );
	}
	return 0;
}
