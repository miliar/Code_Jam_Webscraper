#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

vector<string> tokenize(string s, string delim=" ") {
	vector<string> res;
	while (s.size()) {
		int i = s.find(delim);
		if (i == -1) {
			res.push_back(s);
			s = "";
			break;
		}
		string t = s.substr(0, i);
		if (t.length())	res.push_back(t);
		s = s.substr(i + delim.length());
	}
	return res;
}


#define MAX_N 8
bool conn[MAX_N][MAX_N];
bool conn2[MAX_N][MAX_N];
bool finalconn[MAX_N][MAX_N];
int N;
bool used[MAX_N];
int reftab[MAX_N];
bool doit(int lev) {
	int i, j;
	if (lev == N) {
		/*for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++) {
				printf("%d ", conn[i][j]);
			}
			printf("\n");
		}
		for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++) {
				printf("%d ", conn2[reftab[i]][reftab[j]]);
			}
			printf("\n");
		}*/
		for (i = 0; i < N; i++) {
			for (j = 0; j < N; j++) {
				if (!conn[i][j] && conn2[reftab[i]][reftab[j]]) {
					return false;
				}
			}
		}
		return true;
	}

	for (i = 0; i < N; i++) {
		if (used[i]) continue;
		//printf("lev %d = %d\n", lev, i);
		used[i] = true;
		reftab[lev] = i;
		if (doit(lev+1)) {
			used[i] = false;
			//printf("lev %d returns true\n", lev);
			return true;
		}
		used[i] = false;
	}
	//printf("lev %d returns false\n", lev);
	return false;
}

int main() {
	int NTc;
	scanf("%d", &NTc);
	int i, j, k, m, n;
	for (int tc = 0; tc < NTc; tc++) {
		printf("Case #%d: ", tc+1);
		memset(conn, 0, sizeof(conn));
		memset(conn2, 0, sizeof(conn));
		scanf("%d", &N);
		for (j = 0; j < N-1; j++) {
			scanf("%d %d", &m, &n);
			m--; n--;
			conn[m][n] = conn[n][m] = true;
		}
		scanf("%d", &i);
		for (j = 0; j < i-1; j++) {
			scanf("%d %d", &m, &n);
			m--; n--;
			conn2[m][n] = conn2[n][m] = true;
		}
		if (doit(0)) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}
	}
	return 0;
}