#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>

using namespace std;

int dbg;

string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}

int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}

vector<int> readVI() {
	int n;
	scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}

double dist(int x0, int y0, int x1, int y1) {
	return sqrt((x0-x1)*(x0-x1) + (y0-y1)*(y0-y1));
}

double solveIt(vector<int> &x, vector<int> &y, vector<int> &r) {
	if (r.size() == 1) return r[0];
	if (r.size() == 2) return r[0] < r[1] ? r[1] : r[0];

	double mnmx = 1e100;
	double rj = dist(x[0], y[0], x[1], y[1])+r[0]+r[1];
	if (r[2]*2 > rj) rj = r[2]*2;
	if (rj < mnmx) mnmx = rj;

	rj = dist(x[0], y[0], x[2], y[2])+r[0]+r[2];
	if (r[1]*2 > rj) rj = r[1]*2;
	if (rj < mnmx) mnmx = rj;

	rj = dist(x[2], y[2], x[1], y[1])+r[2]+r[1];
	if (r[0]*2 > rj) rj = r[0]*2;
	if (rj < mnmx) mnmx = rj;

	return mnmx/2;
}

int main(int argc, char ** /*argv*/) {
	dbg = argc;
	int CCT = readIntLine();
	for (int cn = 1; cn <= CCT; cn++) {
		int N;
		scanf("%d ", &N);
		vector<int> X(N), Y(N), R(N);
		for (int i = 0; i < N; i++) scanf("%d %d %d", &X[i], &Y[i], &R[i]);

		double res = solveIt(X, Y, R);
		printf("Case #%d: %0.15lf\n", cn, res);
	}
	return 0;
}

