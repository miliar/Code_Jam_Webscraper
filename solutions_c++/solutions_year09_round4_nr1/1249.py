#define LOCAL

#include <cstdio>
#include <cmath>
#include <cstring>

#include <memory>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

#include <cassert>

#define TASK "A"
#define PB(a) push_back(a)
#define MP(a, b) make_pair(a, b)

using namespace std;

typedef long long int64;
typedef vector <int> State;

int T;

map <State, int> dist;
set <State> mark;

State v, v0, newv;

int head, tail;

int n;

State q[100000];

const int MAXN = 10;

char a[MAXN][MAXN];

int p[MAXN];
             
int main() {
	#ifdef LOCAL
		freopen(TASK ".in", "rt", stdin);
		freopen(TASK ".out", "wt", stdout);
	#endif

	scanf("%d", &T);

	for (int cs = 1; cs <= T; cs++) {
		printf("Case #%d: ", cs);

		scanf("%d\n", &n);
		for (int i = 0; i < n; i++) {
			gets(a[i]);
			p[i] = -1;
			for (int j = 0; j < n; j++) {
				if (a[i][j] == '1') {
					p[i] = j;
				}
			}
		}

		mark.clear();
		dist.clear();

		v0.clear();
		for (int i = 0; i < n; i++) v0.PB(i);

		head = 1; tail = 2;

		q[head] = v0;
		mark.insert(v0);
		dist[v0] = 0;

		while (head < tail) {
			v = q[head++];

			bool ok = true;
			for (int i = 0; i < n && ok; i++) {
				if (p[v[i]] > i) {
					ok = false;
				}
			}

			if (ok) {
				printf("%d", dist[v]);
				//printf(" ");
				//for (int k = 0; k < n; k++) printf("%d.", v[k]);
				break;
			}

			for (int i = 0; i < n-1; i++) {
				newv = v;
				swap(newv[i], newv[i+1]);

				if (mark.find(newv) == mark.end()) {
					q[tail++] = newv;
					mark.insert(newv);
					dist[newv] = dist[v] + 1;
				}
			}
		}

		cout << endl;
	}

	return 0;
}

