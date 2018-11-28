#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)

typedef long long LL;
struct point {
	LL x; LL y;
	bool operator != (const point &p) { return this->x != p.x || this->y != p.y; }
	bool operator == (const point &p) { return this->x == p.x && this->y == p.y; }
};

int main()
{
	int ncase;
	scanf( "%d", &ncase );

	FOR(tcase,1,ncase) {
		LL n, A, B, C, D, x0, y0, M;
		scanf( "%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &M );
		
		LL arr[3][3] = { 0 };

		LL x = x0, y = y0;
		arr[x%3][y%3]++;
		FOR(i,1,n-1) {
			x = (A * x + B) % M;
			y = (C * y + D) % M;
			arr[x%3][y%3]++;
		}
		
		LL ans = 0;
		FOR(i,0,8) FOR(j,i,8) FOR(k,j,8) {
			point a = (point){i/3, i%3};
			point b = (point){j/3, j%3};
			point c = (point){k/3, k%3};
			if ( (a.x + b.x + c.x) % 3 != 0 ) continue;
			if ( (a.y + b.y + c.y) % 3 != 0 ) continue;

			if ( a != b && a != c && b != c )
				ans += max(0LL, arr[a.x][a.y] * arr[b.x][b.y] * arr[c.x][c.y]);
			else if ( a == b && a != c )
				ans += max(0LL, arr[a.x][a.y] * (arr[a.x][a.y] - 1) * arr[c.x][c.y] / 2);
			else if ( a == c && a != b )
				ans += max(0LL, arr[a.x][a.y] * (arr[a.x][a.y] - 1) * arr[b.x][b.y] / 2);
			else if ( b == c && a != b )
				ans += max(0LL, arr[b.x][b.y] * (arr[b.x][b.y] - 1) * arr[a.x][a.y] / 2);
			else if ( a == b && a == c )
				ans += max(0LL, arr[a.x][a.y] * (arr[a.x][a.y] - 1) * (arr[a.x][a.y] - 2) / 6);
		}

		printf( "Case #%d: %lld\n", tcase, ans );
	}
	
	return 0;
}
