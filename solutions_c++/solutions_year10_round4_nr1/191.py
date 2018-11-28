#include <iostream>

#define INF 1000000000

using namespace std;

int A[150][150];

int main() {
	freopen("a-large.in", "r", stdin);
	freopen("a-large-out.txt", "w", stdout);
	int tt, ttt, i, j, k, K, u, v, uu, vv, radius;
	scanf("%d", &tt);
	for(ttt = 1; ttt <= tt; ttt++) {
		scanf("%d", &K);
		memset(A, -1, sizeof(A));
		for(i = 0; i < K; i++) {
			for(j = K - 1 - i, k = 0; k < i + 1; j += 2, k++) {
				scanf("%d", &A[i][j]);
			}
		}
		for(i = 1; i < K; i++) {
			for(j = i, k = 0; k < K - i; j += 2, k++) {
				scanf("%d", &A[K - 1 + i][j]);
			}
		}
		
		radius = INF;
		for(i = 0; i < K * 2 - 1; i++) {
			for(j = 0; j < K * 2 - 1; j++) {
				for(u = 0; u < 2 * K - 1; u++) {
					for(v = 0; v < 2 * K - 1; v++) {
						if (A[u][v] == -1) continue;
						uu = 2 * i - u;
						vv = 2 * j - v;
						if (0 <= uu && uu < K * 2 - 1 
							&& A[uu][v] != -1 && A[uu][v] != A[u][v]) break;
						if (0 <= vv && vv < K * 2 - 1 
							&& A[u][vv] != -1 && A[u][vv] != A[u][v]) break;
					}
					if (v < 2 * K - 1) break;
				}
				if (u == 2 * K - 1) {
					radius = min(radius, 
						max(
							abs(K - 1 - i) + max(j + 1, 2 * K - 1 - j),
							abs(K - 1 - j) + max(i + 1, 2 * K - 1 - i)
						)
					);				
//					radius = min(radius, max(max(i, j) + 1, 2 * K - 1 - min(i, j)));
//					cout << i << " " << j << " " << max(max(i, j) + 1, 2 * K - 1 - min(i, j)) << endl;
				}
			}
		}
		j = 0;
		for(i = K + 1; i <= radius; i++)
			j += i * 2 - 1;
		printf("Case #%d: %d\n", ttt, j);
	}
//	system("pause");
	return 0;
}
