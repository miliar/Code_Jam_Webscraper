#include <cstdio>
#include <iostream>
using namespace std;

int s[1001][10];
int m[1001];
int t[1001];
int r[1001];

int dfs(int d) {
	if(r[d] != 0) return 0;
	r[d]++;
	for(int i = 0 ; i < m[d]; i++) {
		if(dfs(s[d][i]) == 0) return 0;
	}
	return 1;
}

int main() {
	int T, N, prob = 1;
	for (cin >> T; T--;) {
		bool y;
		cin >> N;
		for (int i = 1; i <= N; i++) {
			t[i] = 0;
			r[i] = 0;
		}


		for (int i = 1; i <= N; i++)
		{
			cin >> m[i];
			for(int j = 0; j < m[i]; j++) {
				cin >> s[i][j];
				t[s[i][j]]++;
			}
		}

		y = 1;
		for(int i = 1; i <= N; i++) {
			if(0 != t[i])
				continue;
			for(int ik = 1; ik <= N; ik++) r[ik] = 0;

			if(0 == dfs(i)) {
				y = 0;
				break;
			}
		}

		if(y)
			printf("Case #%d: No\n", prob++);
		else
			printf("Case #%d: Yes\n", prob++);
	}
}
