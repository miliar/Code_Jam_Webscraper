#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <queue>

using namespace std;

int T, N, D;
int l[10000];
int d[10000];
int maxh[10000];

int main() {
	scanf("%d\n", &T);

	for (int nCase = 1; nCase <= T; nCase++) {
		scanf("%d\n", &N);
		
		for (int i = 0; i < N; i++) {
			scanf("%d %d\n", &d[i], &l[i]);
		}
		
		scanf("%d\n", &D);
		
		memset(maxh, -1, sizeof(maxh));
		
		maxh[0] = d[0];
		
		bool possible = false;
		
		for (int i = 0; i < N; i++) {
			if (maxh[i] == -1) continue;
			
			if (maxh[i] + d[i] >= D) {
				possible = true;
				break;
			}
			
			for (int j = i + 1; j < N && d[i] + maxh[i] >= d[j]; j++) {
				int landing = min(l[j], d[j] - d[i]);
				
				if (maxh[j] == -1 || maxh[j] < landing) {
					maxh[j] = landing;
				}
			}
		}
		
		printf("Case #%d: %s\n", nCase, possible ? "YES": "NO");
	}
}

