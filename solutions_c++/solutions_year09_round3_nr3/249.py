#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;
#define MAXL 128
#define INF 0x7fffffff;

int P, Q;
int pos[MAXL];
bool flag[MAXL];
bool full[MAXL];
int res;

void dfs(int kth, int cost) {
	if (kth == Q) {
		if (cost < res)
			res = cost;
	} else {
		int i;
		for (i = 0; i < Q; ++i)
			if (flag[i] == true) {
				flag[i] = false;
				int key = pos[i];
				full[key] = false;
				int tmp = 0;
				int j;
				for (j = key - 1; j >= 1; --j) {
					if (full[j] == true)
						tmp++;
					else
						break;
				}
				for (j = key + 1; j <= P; ++j) {
					if (full[j] == true)
						tmp++;
					else
						break;	
				}
				dfs(kth + 1, cost + tmp);
				full[key] = true;
				flag[i] = true;	
			}	
	}
}

int main(int argc, char* argv[]) {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	
	int N;
	scanf("%d", &N);
	
	int cas;
	for (cas = 1; cas <= N; ++cas) {
		scanf("%d%d", &P, &Q);
		
		int i;
		for (i = 0; i < Q; ++i)
			scanf("%d", &pos[i]);
			
		memset(full, true, sizeof(full));
		memset(flag, true, sizeof(flag));
		
		res = INF;
		dfs(0, 0);
		
		printf("Case #%d: %d\n", cas, res);
	}	
	return EXIT_SUCCESS;
}
