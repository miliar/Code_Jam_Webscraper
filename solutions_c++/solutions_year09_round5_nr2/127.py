#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int n, P;
int ct[100][27];
__int64 ret[15];
char str[1000], word[100][100], tt[100];
__int64 queue[10000000];
map<__int64, int> mp[11];

void solve() {
	int i, j, k = 0, tq, t, r;
	int ind[4];
	for (i = 0; i < strlen(tt); i++) {
		ind[k++] = tt[i] - 'a';
	}
	for (j = k; j < 4; j++) ind[j] = 26;
	int p, q;
	__int64 tmp, nt, pw, pp, rr;
	queue[p = q = 0] = 0;
	mp[0][0] = 1;
	for (i = 1; i <= P; i++) {
		tq = q;
		mp[i].clear();
		for (; p <= tq; p++) {
			tmp = queue[p];
			t = mp[i - 1][tmp];
			for (j = 0; j < n; j++) {
				nt = tmp;
				pw = 1;
				for (r = 0; r < 4; r++) {
					nt += ct[j][ind[r]] * pw;
					pw *= 5001;
				}
				rr = 1;
				pp = nt;
				for (r = 0; r < k; r++) {
					rr *= pp % 5001;
					pp /= 5001;
				}
				ret[i] = (ret[i] + rr * t) % 10009;
				if (mp[i].find(nt) == mp[i].end()) {
					queue[++q] = nt;
					mp[i][nt] = t;
				}
				else {
					mp[i][nt] += t;
				}
			}
		}
	}
}

int main() {
	int i, j, k;
	int TT, testcases;
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &testcases);
	for (TT = 1; TT <= testcases; TT++) {
		scanf("%s%d", str, &P);
		scanf("%d", &n);
		memset(ret, 0, sizeof(ret));
		memset(ct, 0, sizeof(ct));
		for (i = 0; i < n; i++) {
			scanf("%s", word[i]);
			for (j = 0; j < strlen(word[i]); j++) {
				ct[i][word[i][j] - 'a']++;
			}
		}
		k = 0;
		for (i = 0; i < strlen(str); i++) {
			if (str[i] == '+') {
				tt[k] = 0;
				solve();
				k = 0;
			}
			else {
				tt[k++] = str[i];
			}
		}
		tt[k] = 0;
		solve();
		printf("Case #%d:", TT);
		for (i = 1; i <= P; i++) printf(" %I64d", ret[i]);
		printf("\n");
	}
	return 0;
}
