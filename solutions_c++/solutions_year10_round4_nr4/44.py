#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main( void )
{
	int C;
	cin >> C;
	for( int CC = 1; CC <= C; CC ++ ){
		int N, M;
		cin >> N >> M;
		double PX[N], PY[N];
		for( int i = 0; i < N; i ++ )
			cin >> PX[i] >> PY[i];

		printf( "Case #%d:", CC );
		for( int j = 0; j < M; j ++ ){
			double qx, qy;
			cin >> qx >> qy;

			long double ri[N];
			long double thi[N];
			for( int i = 0; i < N; i ++ ){
				long double yy = PY[i]-qy;
				long double xx = PX[i]-qx;
				thi[i] = atan2l( yy, xx );
				ri[i] = sqrtl( yy*yy + xx*xx );
			}

			long double r = 0;
			const long double dth = (M_PI * 2.0) / (1<<21);
			for( long double th = -M_PI; th <= M_PI; th += dth ){
				long double R = 1e20;
				for( int i = 0; i < N; i ++ ){
					long double th2 = th - thi[i];
					long double r = 2.0 * ri[i] * cosl(th2);
					R = min( R, r );
					if( R <= 0 ) break;
				}
				if( R > 0 )
					r += R * R;
			}
			r *= 0.5 * dth;
			printf( " %.10lf", (double)r );
		}
		printf( "\n" );
	}
	return 0;
}
