#include <cstdio>
#include <cstring>
#include <queue>
#include <map>
using namespace std;

const int MAX = 55;
const int INF = 0x3f3f3f3f;


int r, c, f;

struct T {
	int i, j, f;
	int C;
	char cave[MAX][MAX];
	T(int i, int j, int f, int C, char _cave[MAX][MAX]) : i(i), j(j), f(f), C(C) {
		memcpy(cave, _cave, sizeof cave);
	}
	bool operator<(const T& other) const {
		if (C != other.C) return C > other.C;
		if (i!=other.i) return i < other.i;
		if (j!=other.j) return j < other.j;
		return memcmp(cave,other.cave,sizeof cave)<0;
	}
	void print() {
		printf("--- %d %d %d %d ---\n", i,j,f,C);
		for (int i = 0; i < r; ++i) puts(cave[i]);
		puts("");
	}
};

char cave[MAX][MAX];
map<T,int> memo;

bool verify(int i, int j, char cave[MAX][MAX]) {
	if (j > 0) {
		if (cave[i][j-1]=='.') return true;
	}
	if (j < c-1) {
		if (cave[i][j+1]=='.') return true;
	}
	return false;
}

int main() {
	int n_tests;

	scanf("%d", &n_tests);
	for (int test = 1; test <= n_tests; ++test) {
		scanf("%d %d %d", &r, &c, &f);

		memset(cave,'.',sizeof cave);
		for (int i = 0; i < r; ++i) {
			scanf("%s", cave[i]);
		}

		memo.clear();
		priority_queue<T> q;

		q.push(T(0,0,0,0, cave));
		memo[T(0,0,0,0,cave)] = 0;

		int res = INF;
		while (!q.empty()) {
			T t = q.top(); q.pop();

			//t.print();

			if (t.f > f) continue;

			if (t.i == r - 1) {
				res = min(res,t.C);
				break;
			}

			if (t.cave[t.i+1][t.j] == '.') {
				t.f++;
				t.i++;
				q.push(t);
				continue;
			}

			t.f = 0;

			if (verify(t.i,t.j, t.cave)) {
				//puts("asdf");
				if (t.j+1<c && t.cave[t.i+1][t.j+1] == '#' && t.cave[t.i][t.j+1] == '.') {
					T tt = t;
					tt.cave[t.i+1][t.j+1] = '.';
					//tt.i++;
					//tt.j++;
					tt.f++;
					tt.C++;
					q.push(tt);
				}
				if (t.j-1>=0 && t.cave[t.i+1][t.j-1] == '#' && t.cave[t.i][t.j-1] == '.') {
					T tt = t;
					tt.cave[t.i+1][t.j-1] = '.';
					//tt.i++;
					//tt.j--;
					tt.f++;
					tt.C++;
					q.push(tt);
				}
			}

			int C = 0;
			for (int j = t.j-1; j >= 0; --j) {
				if (t.cave[t.i][j] != '.') break;
				T tt = t;
				tt.j = j;
				tt.C += C;
				if (memo.find(tt) == memo.end()) {
					memo[tt] = tt.C;
					q.push(tt);
				}
				if (t.cave[t.i+1][j] == '.') break;
			}
			C = 0;
			for (int j = t.j+1; j < c; ++j) {
				if (t.cave[t.i][j] != '.') break;
				T tt = t;
				tt.j = j;
				tt.C += C;
				if (memo.find(tt) == memo.end()) {
					memo[tt] = tt.C;
					q.push(tt);
				}
				if (t.cave[t.i+1][j] == '.') break;
			}
		}

		if (res == INF)
			printf("Case #%d: No\n", test);
		else
			printf("Case #%d: Yes %d\n", test, res);
	}

	return 0;
}
