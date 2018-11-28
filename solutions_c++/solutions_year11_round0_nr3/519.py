#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
const int MAXN = 1000010;
const int MAX = 0x7f7f7f7f;
int f[MAXN], g[MAXN];
int main(){
	int cases;
	scanf("%d", &cases);
	for (int tt = 0; tt < cases; ++tt){
		int n;
		scanf("%d", &n);
		vector<int> candy;
		int res = 0;
		int t = MAX;
		int total = 0;
		for (int i = 0; i < n; ++i){
			int x;
			scanf("%d", &x);
			candy.push_back(x);
			if (i == 0) res = candy[0]; else res ^= candy[i];
			if (x < t) t = x;
			total += x;
		}
		if (res == 0){
			printf("Case #%d: %d\n", tt + 1, total - t);
		} else {
			printf("Case #%d: %s\n", tt + 1, "NO");
		}
		/*
		memset(f, MAX, sizeof(f));
		f[0] = 0;
		memcpy(g, f, sizeof(g));
		for (int i = 0; i < n; ++i){
			for (int j = 0; j < MAXN; ++j){
				if (f[j] != MAX){
					if (j == 0 && candy[i] < g[candy[i]]){
						g[candy[i]] = candy[i];
						continue;
					}
					if (candy[i] + f[j] < g[j ^ candy[i]]){
						g[j ^ candy[i]] = candy[i] + f[j];
					}
				}
			}
			memcpy(f, g, sizeof(f));
		}
		if (f[total / 2] == MAX){
			printf("Case %d: %s\n", tt + 1, "NO");
		} else {
			printf("Case %d: %d\n", tt + 1, f[total / 2]);
		}*/
	}
	return 0;
}