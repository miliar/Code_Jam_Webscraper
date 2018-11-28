#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second 

#define N 100111
#define TYPE long long

pii a[N];

TYPE b[9];

int main () {
	int i, j, k, T;
	long long n, A, B, C, D, x0, y0, x, y, M;

	scanf("%d", &T);
	
	for (int cas = 1; cas <= T; cas++) {
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x0, &y0, &M );

		a[0] = MP( x0, y0 );
		x = x0, y = y0;
		for (i = 1; i < n; i++) {
			x = (A * x + B) % M;
			y = (C * y + D) % M;
			a[i] = MP( x,y );
		}

		mset(b,0);

		TYPE res = 0;

		for (i = 0; i < n; i++) b[ (a[i].X % 3) * 3 + a[i].Y % 3 ]++;

		for (i = 0; i < 9; i++) for (j = i; j < 9; j++) for (k = j; k < 9; k++) {
			TYPE xi = i / 3, yi = i % 3;
			TYPE xj = j / 3, yj = j % 3;
			TYPE xk = k / 3, yk = k % 3;
			if ( (xi+xj+xk) % 3 == 0 && (yi+yj+yk)%3 == 0 ) {
				if ( i == j && j == k ) res += b[i] * (b[i]-1) * (b[i]-2) / 6;
				else if (i == j) res += ( b[i] * (b[i]-1) / 2 ) * b[k];
				else if (j == k) res += ( b[j] * (b[j]-1) / 2 ) * b[i];
				else if (i == k) res += ( b[i] * (b[i]-1) / 2 ) * b[j];
				else res += b[i] * b[j] * b[k];
			}			
		}
		printf("Case #%d: %lld\n", cas, res);
	}

	return 0;
}