#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <ctime>

using namespace std;

typedef vector <int> VI;
typedef vector <string> VS;

typedef struct _Point {
	long long nX;
	long long nY;

} Point;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,n,m) for(int i=(n);i<(m);++i)
#define LOOP for(;;)
#define zero(n) memset((n),0,sizeof(n))
#define PB push_back

string n2c(int n){string s;LOOP{s=(char)('0'+n%10)+s;if(n<10)break;n/=10;}return s;}

bool operator<(const _Point& left, const _Point& right){
	if ( left.nX == right.nX ) return left.nY < right.nY;
	return left.nX < right.nX;

}
bool operator>(const _Point& left, const _Point& right){
	if ( left.nX == right.nX ) return left.nY > right.nY;
	return left.nX > right.nX;

}


int main ( void )
{
	FILE *fp1, *fp2;
	int nc, n;
	unsigned long long a, b, c, d, x0, y0, m;
	vector <Point> pt;
	Point tpt, pt1, pt2, pt3, g;
	int cnt = 0;

	fp1 = fopen ( "input.txt", "r" );
	fp2 = fopen ( "output.txt", "w" );
	fscanf ( fp1, "%d\n", &nc );

	REP ( i, nc ) {
		fscanf ( fp1, "%d %lld %lld %lld %lld %lld %lld %lld\n", &n, &a, &b, &c, &d, &x0, &y0, &m );
		pt.clear ( );
		REP ( j, n ) {
			tpt.nX = x0; tpt.nY = y0;
			pt.push_back ( tpt );
			x0 = ( a * x0 + b ) % m;
			y0 = ( c * y0 + d ) % m;
			if ( x0 < 0 ) { 
				int a = a;

			}

		}
		REP ( j, n - 2 ) {
			FOR ( k, j + 1, n - 1 ) {
				FOR ( l, k + 1, n ) {
					pt1 = pt [ j ];
					pt2 = pt [ k ];
					pt3 = pt [ l ];
					if ( ( pt1.nX + pt2.nX + pt3.nX ) % 3 == 0 && ( pt1.nY + pt2.nY + pt3.nY ) % 3 == 0 )
						if ( pt1.nX + pt2.nX + pt3.nX >= 3 && pt1.nY + pt2.nY + pt3.nY >= 3 ) {
							cnt++;

						} else {
													cout << ( double )( pt1.nX + pt2.nX + pt3.nX ) / 3 << "," << ( double )( pt1.nY + pt2.nY + pt3.nY ) / 3 << endl;
						}


				}

			}

		}
		fprintf ( fp2, "Case #%d: %d\n", i + 1, cnt );
//		cout << "Case #" << i + 1 << ": " << cnt << endl;
		cnt = 0;

	}

	fclose ( fp1 );
	fclose ( fp2 );


	return 0;

}

