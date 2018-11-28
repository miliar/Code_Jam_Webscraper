#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)

typedef long long int64;
typedef pair <int, int> pii;
typedef pair <double, double> point;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

template <class T> T sqr (T x) {return x * x;}

double W;
int n, m, G;
vector <point> L, R, L1, R1;

vector <point> update (vector <point> A, vector <point> B) {
	vector <point> res;
	int lf = 0;
	res.pb (A[lf]);
	forn (i, B.size()) {
		while ((lf+2 < I A.size()) && (B[i].x > A[lf+1].x)) {
			lf ++;
			res.pb (A[lf]);
		}	
		double X = B[i].x;
		double Y = A[lf].y + (A[lf+1].y - A[lf].y) / (A[lf+1].x - A[lf].x) * (X - A[lf].x);
		res.pb (mp (X, Y));
	}
	res.pb (A[lf+1]);
	return res;
}

double f (point p1, point p2) {
	return fabs ((p2.x - p1.x) * (p1.y + p2.y) / 2.); 
}

void calcacla () {
	cin >> W >> n >> m >> G;
	L.resize (n);
	R.resize (m);
	forn (i, n)
		cin >> L[i].x >> L[i].y;
	forn (i, m)
		cin >> R[i].x >> R[i].y;
	L1 = update (L, R);
	R1 = update (R, L);
	L = L1;
	R = R1;
	n = L.size();
	forn (i, n)
		R[i].y -= L[i].y;
	double S = 0;
	forn (i, n-1)
		S += f(R[i], R[i+1]);
	S /= (double)G;
	int P = 0;
	point PR = R[0];
	forn (i, G-1) {
		double CS = 0;
		while (CS + f(PR, R[P]) < S + eps) {
			CS += f(PR, R[P]);
			PR = R[P];
			P ++;
		}
		double lf = PR.x;
		double rg = R[P].x;
		forn (j, 100) {
			double mx = (lf + rg) / 2;
			double my = PR.y + (R[P].y - PR.y) / (R[P].x - PR.x) * (mx - PR.x);
			double ds = f (PR, mp (mx, my));
			if (CS + ds > S)
				rg = mx;
			else
				lf = mx;
		}
		double mx = (lf + rg) / 2;
		double my = PR.y + (R[P].y - PR.y) / (R[P].x - PR.x) * (mx - PR.x);
		PR = mp (mx, my);
		printf ("%.9lf\n", PR.x);
	}
}

int main ()
{
//	freopen ("input.txt", "r", stdin);
//	freopen ("output.txt", "w", stdout);
	int tt;
	cin >> tt;
	forn (ii, tt) {
		printf ("Case #%d: \n", ii+1);
		calcacla ();
	}
	
	return 0;
}
