#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <string>

using namespace std;

char buf[1 << 16];

#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define mp make_pair

#define CMAX 1111
#define QMAX 1111

#define INF int(1E+9)

int A[CMAX][QMAX];

void solve(int tst) {
	int nc, nq;
	scanf("%d", &nc);		
	gets(buf);

	map<string, int> num;					
	int id = 0;

	vector<int> c(nc);

	forn (i, nc) {
		gets(buf);

		string s(buf);
		if (num.count(s))
			c[i] = num[s];
		else
			c[i] = num[s] = id++;
	}

	scanf("%d", &nq);		
	gets(buf);

	vector<int> q(nq);

	forn (i, nq) {
		gets(buf);

		string s(buf);
		if (num.count(s))
			q[i] = num[s];
		else
			q[i] = num[s] = id++;
	}

	forn (i, nc + 1)
		forn (j, nq + 1)
			A[i][j] = INF;

	forn (i, nc) {
		A[i][0] = 0;
	}

	forn (j, nq)
		forn (i, nc)
			if (A[i][j] < INF) {
				if (c[i] != q[j])
					A[i][j + 1] = min(A[i][j + 1], A[i][j]);
				forn (k, nc)
					if (c[k] != q[j])
						A[k][j + 1] = min(A[k][j + 1], A[i][j] + 1);
			}

	int ans = INF;
	forn (i, nc)
		ans = min(ans, A[i][nq]);	      

	printf("Case #%d: %d\n", tst, ans);
}

int main() {

	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);

	int t;
	scanf("%d", &t);

	forn (i, t) solve(i + 1);

	return 0;
}