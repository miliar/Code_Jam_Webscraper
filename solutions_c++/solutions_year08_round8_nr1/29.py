#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <numeric>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
#define ss stringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vii vector<pii>
#define vs vector<string>
#define LD long double

using namespace std;

int X[3], Y[3];
int Xt[3], Yt[3];
//LD t;
LD A[2][2], B[2];
/*
void findT() {
	LD d1 = sqrt((X[0] - X[1])*(X[0] - X[1]) + (Y[0] - Y[1])*(Y[0] - Y[1]));
	LD d2 = sqrt((Xt[0] - Xt[1])*(Xt[0] - Xt[1]) + (Yt[0] - Yt[1])*(Yt[0] - Yt[1]));
	t = d2/d1;
}
*/
int solve(int x1, int y1, int xt1, int x2, int y2, int xt2, int x3, int y3, int xt3, int ind) {
	x2 -= x1;
	y2 -= y1;
	x3 -= x1;
	y3 -= y1;
	xt2 -= xt1;
	xt3 -= xt1;
	int det = x2 * y3 - y2 * x3;
	int B0 = xt2 * y3 - xt3 * y2;
	if(det == 0 && B0) return -1;
	int B1 = xt2 * x3 - xt3 * x2;
	if(det == 0 && B1) return -1;
	if(det == 0) return 0;
	LD z = 0.0;
	A[ind][0] = B0/(det + z);
	A[ind][1] = B1/(-det + z);
	B[ind] = xt1 - A[ind][0] * x1 - A[ind][1] * y1;
	return 1;
}

void solveCase(int Case) {
	memset(A, 0, sizeof(A));
	memset(B, 0, sizeof(B));
	fr(i, 3) cin >> X[i] >> Y[i];
	fr(i, 3) cin >> Xt[i] >> Yt[i];
//	findT();
	int f = solve(X[0], Y[0], Xt[0], X[1], Y[1], Xt[1], X[2], Y[2], Xt[2], 0);
	int s = solve(X[0], Y[0], Yt[0], X[1], Y[1], Yt[1], X[2], Y[2], Yt[2], 1);
//	cout << A[0][0] << ' ' << A[0][1] << ' ' << B[0] << endl;
//	cout << A[1][0] << ' ' << A[1][1] << ' ' << B[1] << endl;
	cout << "Case #" << Case << ": ";
	if(f == -1 || s == -1) {
		cout << "No Solution" << endl;
		return;
	}
//	fr(i, 2) fr(j, 2) A[i][j] *= t;
//	fr(i, 2) B[i] *= t;
	if(!f && !s) {
		cout << "cia1" << endl;
		A[0][0] = 2;
		A[0][1] = 0;
		A[1][0] = 0;
		A[1][1] = 2;
		B[0] = Xt[0] - A[0][0] * X[0] - A[0][1] * Y[0];
		B[1] = Xt[1] - A[1][0] * X[1] - A[1][1] * Y[1]; 
	}
	if(!f && s) {
		cout << "cia2" << endl;
		if(fabs(A[1][1]) > 1e-9) A[0][0] = 2;
		else A[0][1] = 2;
		B[0] = Xt[0] - A[0][0] * X[0] - A[0][1] * Y[0];
	}
	if(f && !s) {
		cout << "cia3" << endl;
		if(fabs(A[0][0]) > 1e-9) A[1][1] = 2;
		else A[1][0] = 2;
		B[1] = Xt[1] - A[1][0] * X[1] - A[1][1] * Y[1]; 
	}
	A[0][0] -= 1;
	A[1][1] -= 1;
	LD B1 = -B[0];
	LD B2 = -B[1];
	LD det = A[0][0] * A[1][1] - A[0][1] * A[1][0];
	LD x = (B1 * A[1][1] - B2 * A[0][1]) / det;
	LD y = (B2 * A[0][0] - B1 * A[1][0]) / det;
	printf("%.6f %.6f\n", (float)x, (float)y);
}

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int tests;
	cin >> tests;
	for(int i = 0; i < tests; i++) solveCase(i + 1);
	return 0;
}
