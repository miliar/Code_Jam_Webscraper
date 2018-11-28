#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <math.h>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <fstream>
#include <cstdio>

using namespace std;

typedef vector <int> VI;
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(i, a, b) for (int i = (a); i <= (b); ++i)
#define PB push_back
#define ALL(x) x.begin(),x.end()

char strin[10000];

int main()
{
	int n;
	int A, B, C, D, x0, y0, M;
	freopen("A_small.txt", "rt", stdin);
	ofstream out("A_small.out");
	int T, j;
	vector <long long> iX, iY;
	gets(strin);
	sscanf(strin, "%d", &T);
	for (j = 1; j <= T; j++) {
		int rez = 0;
		iX.clear(); iY.clear();
		gets(strin);
		sscanf(strin, "%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		cout << n << " " << A << " " << B << " " << C << " " << D << " " << x0 << " " << y0 << " " << M << endl;
		long long X = x0, Y = y0;
		for (int i = 0; i < n; i++) {
			iX.PB(X);
			iY.PB(Y);
			X = (((long long)A) * X + B) % M;
			Y = (((long long)C) * Y + D) % M;
		}
		for (int m = 0; m < n; m++)
			for (int p = m + 1; p < n; p++)
				for (int o = p + 1; o < n; o++) {
					long long auxX = iX[m] + iX[p] + iX[o];
					long long auxY = iY[m] + iY[p] + iY[o];
					if (((auxX % 3) == 0) && ((auxY % 3) == 0)) rez++;
				}
		out << "Case #" << j << ": " << rez << endl;
	}
	return 0;
}
