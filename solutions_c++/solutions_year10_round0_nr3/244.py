#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std; 

long long T;
long long R, k, N, g[1008];
long long all = 0;
map<int, long long> maps;
long long getTo[1008];
long long atT[1008];
int ext[1008];
long long value[1008];
int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.txt", "w", stdout);

	scanf("%d", &T);
	int caseT = 1;
	while(T--) {
		scanf("%lld %lld %lld", &R, &k, &N);
		all = 0;
		for(int i = 0; i < N; ++i) {
			scanf("%lld", &g[i]);
			all += g[i];
			
		}
		long long ans = 0;
		if(all <= k) {
			ans = R *all;
			printf("Case #%d: %lld\n", caseT++, ans);
			continue;
		}

		for(int i = 0; i < N; ++i) {
			long long now = 0, nexts = (i + 1) % N;
			for(int j = i, t = 0; t < N; ++t, j = (j + 1) % N) {
				if(now + g[j] <= k) {
					now = now + g[j];
					nexts = (j + 1) % N;
				} else {
					break;
				}
			}
			getTo[i] = nexts;
			atT[i] = now;
		}
		int nxt = 0;

		//find Cir
		maps.clear();
		memset(ext, -1, sizeof(ext));

		for(int i = 0; i < R; ++i) {
			if(ext[nxt] == -1) {
				ext[nxt] = i;
				value[nxt] = ans;
				ans += atT[nxt];
				nxt = getTo[nxt];
			} else {
				//产生了循环节
				int loop = i - ext[nxt];
				long long add = ans - value[nxt];
				R = R - i;
				ans += add * (R /  loop);
				R = R % loop;
				for(int j = 0; j < R; ++j) {
					ans += atT[nxt];
					nxt = getTo[nxt];
				}
				break;
			}

		}
		printf("Case #%d: %lld\n", caseT++, ans);

	}
	return 0;
}