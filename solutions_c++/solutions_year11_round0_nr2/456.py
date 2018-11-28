#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <iostream>
#include <sstream>

using namespace std;

typedef long long i64;
typedef unsigned long u32;
template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T sqr(const T &a) {
	return a * a;
}
char r[200];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int itest = 1; itest <= T; itest++) {
		printf("Case #%d: ", itest);
		vector<vector<int> > mp(26, vector<int>(26, -1));
		vector<vector<bool> > er(26, vector<bool>(26, 0));
		int nr;
		scanf("%d", &nr);
		for (int i = 0; i < nr; i++) {
			char s[4];
			scanf("%s", s);
			int v1 = s[0] - 'A', v2 = s[1] - 'A', t = s[2] - 'A';
			mp[v1][v2] = t;
			mp[v2][v1] = t;
		}
		int nc;
		scanf("%d", &nc);
		for (int i = 0; i < nc; i++) {
			char s[3];
			scanf("%s", s);
			int v1 = s[0] - 'A', v2 = s[1] - 'A';
			er[v1][v2] = 1;
			er[v2][v1] = 1;
		}
		int n;
		scanf("%d", &n);
		string a;
		cin >> a;
		int u = 0;
		for (int i = 0; i < n; i++) {
			r[u++] = a[i];
			int z = mp[r[u - 1] - 'A'][r[u - 2] - 'A'];
			if (u >= 2 && z != -1) {
				u--;
				r[u - 1] = z + 'A';
			} else if (u >= 2) {
				for (int j = 0; j < (u - 1); j++) {
					if (er[r[j] - 'A'][r[u - 1] - 'A']) {
						u = 0;
					}
				}
			}
		}
		printf("[");
		for (int i = 0; i < u; i++) {
			if (i) printf(", ");
			printf("%c", r[i]);
		}
		printf("]\n");
	}
	return 0;
}
