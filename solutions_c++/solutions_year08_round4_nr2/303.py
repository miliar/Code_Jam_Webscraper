#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <map>

using namespace std;

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

int tri2area(int ax, int ay, int bx, int by, int cx, int cy) {
	return abs(cx*ay - ax*cy +
		ax*by - bx*ay +
		bx*cy - cx*by);
}

vector<int> solveIt(int A, int N, int M) {
	vector<int> res;


	int ax = 0, ay = 0;	
	for (int bx = 0; bx <= N; bx++) for (int by = 0; by <= M; by++)
	for (int cx = 0; cx <= N; cx++) for (int cy = 0; cy <= M; cy++)
		if (tri2area(ax, ay, bx, by, cx, cy) == A) {
			res.resize(6);
			res[0] = ax;
			res[1] = ay;
			res[2] = bx;
			res[3] = by;
			res[4] = cx;
			res[5] = cy;
			return res;
		}
	return res;
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		int N, M, A;
		scanf("%d %d %d ", &N, &M, &A);

		vector<int> res = solveIt(A, N, M);

		if (res.empty())
			printf("Case #%d: IMPOSSIBLE\n", cn);
		else
			printf("Case #%d: %d %d %d %d %d %d\n", cn,
				res[0], res[1], res[2], res[3], res[4], res[5]);
	}
	return 0;
}

