#include <iostream>
#include <cstring>
using namespace std;

const int MaxN = 60;
const int Dx[] = {1, 0, 1, 1};
const int Dy[] = {0, 1, -1, 1};

int TCase, N, K, Map[MaxN][MaxN];
char S[MaxN];

bool Check(int s) {
	for (int i = 1; i <= N; ++i)
		for (int j = 1; j <= N; ++j)
			for (int k = 0; k < 4; ++k) {
				int x = i, y = j, t;
				for (t = 1; t <= K; ++t) {
					if (Map[x][y] != s) break;
					x += Dx[k], y += Dy[k];
				}
				if (t > K) return 1;
			}
	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TCase);
	for (int Case = 1; Case <= TCase; ++Case) {
		scanf("%d%d\n", &N, &K);
		memset(Map, 0, sizeof(Map));
		for (int i = 1; i <= N; ++i) {
			gets(S);
			int k = N;
			for (int j = N - 1; j >= 0; --j)
				if (S[j] == 'B') Map[i][k--] = 1;
				else if (S[j] == 'R') Map[i][k--] = 2;
		}
		bool B = Check(1), R = Check(2);
		if (B && R) printf("Case #%d: Both\n", Case);
		else if (B) printf("Case #%d: Blue\n", Case);
		else if (R) printf("Case #%d: Red\n", Case);
		else printf("Case #%d: Neither\n", Case);
	}
	return 0;
}
