#include <cstdio>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }
#define inf 0x3f3f3f3f

#define maxn 11000

using namespace std;

typedef long long int64;

typedef double real;

int gate[maxn], change[maxn];
int was[maxn][2];

int m, v;

int dfs(int curr, int what){
	if (change[curr] == -1){
	 	if (gate[curr] == what) return 0; else return inf;
	}	
	if (was[curr][what] != -1) return was[curr][what];
	if (change[curr] == 1){		
		if (gate[curr] == 0){
			if (what == 0){
				return was[curr][what] = min(min(dfs(2 * curr, 0), dfs(2 * curr + 1, 0)) + 1, dfs(2 * curr, 0) + dfs(2 * curr + 1, 0));
			}else return was[curr][what] = min(dfs(2 * curr, 1) + dfs(2 * curr + 1, 1) + 1, min(dfs(2 * curr, 1), dfs(2 * curr + 1, 1)));
		}else{
	 		if (what == 0){
		 	 	return was[curr][what] = min(dfs(2 * curr, 0) + dfs(2 * curr + 1, 0) + 1, min(dfs(2 * curr, 0), dfs(2 * curr + 1, 0)));
		 	}else{
	 		 	return was[curr][what] = min(min(dfs(2 * curr, 1), dfs(2 * curr + 1, 1)) + 1, dfs(2 * curr, 1) + dfs(2 * curr + 1, 1));
		 	}
		}
	}else{
		if (gate[curr] == 0){
			if (what == 0){
				return was[curr][what] = dfs(2 * curr, 0) + dfs(2 * curr + 1, 0);
			}else return was[curr][what] = min(dfs(2 * curr, 1), dfs(2 * curr + 1, 1));
		}else{
	 		if (what == 0){
		 	 	return was[curr][what] = min(dfs(2 * curr, 0), dfs(2 * curr + 1, 0));
		 	}else{
	 		 	return was[curr][what] = dfs(2 * curr, 1) + dfs(2 * curr + 1, 1);
		 	}
		}

	}
}

int main() {
	int ferlon;
	scanf("%d", &ferlon);
	int _;
	for (_ = 0; _ < ferlon; ++_){
		scanf("%d%d", &m, &v);
		int i;
		memset(change, -1, sizeof(change));
		memset(was, -1, sizeof(was));
		for (i = 1; i <= (m - 1) / 2; i++) scanf("%d%d", &gate[i], &change[i]);
		for (; i <= m; i++) scanf("%d", &gate[i]);
		int res = dfs(1, v);
		printf("Case #%d: ", _ + 1);
		if (res >= inf) printf("IMPOSSIBLE\n"); else printf("%d\n", res);
	}
	return 0;
}
