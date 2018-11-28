#include <cstdio>
#include <memory>

const int N = 1024 * 10;
const int INF = 1 << 30;
struct State{
	int val, gate, change;
	int cnt[2];
}s[N];
int M, V;

int calc(int gate, int u, int extra = 0){
	int l = u * 2, r = u * 2 + 1;
	if(gate == 1){	// and
		int min = INF;
		if(s[l].cnt[0] != -1 && s[r].cnt[0] != -1) min <?= s[l].cnt[0] + s[r].cnt[0];
		if(s[l].cnt[0] != -1 && s[r].cnt[1] != -1) min <?= s[l].cnt[0] + s[r].cnt[1];
		if(s[l].cnt[1] != -1 && s[r].cnt[0] != -1) min <?= s[l].cnt[1] + s[r].cnt[0];
		if(min != INF){
			if(s[u].cnt[0] == -1 || min + extra < s[u].cnt[0]) s[u].cnt[0] = min + extra;
		}
		min = INF;
		if(s[l].cnt[1] != -1 && s[r].cnt[1] != -1) min <?= s[l].cnt[1] + s[r].cnt[1];
		if(min != INF){
			if(s[u].cnt[1] == -1 || min + extra < s[u].cnt[1]) s[u].cnt[1] = min + extra;
		}
	}else{	// or
		int min = INF;
		if(s[l].cnt[0] != -1 && s[r].cnt[0] != -1) min <?= s[l].cnt[0] + s[r].cnt[0];
		if(min != INF){
			if(s[u].cnt[0] == -1 || min + extra < s[u].cnt[0]) s[u].cnt[0] = min + extra;
		}
		min = INF;
		if(s[l].cnt[1] != -1 && s[r].cnt[1] != -1) min <?= s[l].cnt[1] + s[r].cnt[1];
		if(s[l].cnt[0] != -1 && s[r].cnt[1] != -1) min <?= s[l].cnt[0] + s[r].cnt[1];
		if(s[l].cnt[1] != -1 && s[r].cnt[0] != -1) min <?= s[l].cnt[1] + s[r].cnt[0];
		if(min != INF){
			if(s[u].cnt[1] == -1 || min + extra < s[u].cnt[1]) s[u].cnt[1] = min + extra;
		}
	}
}

void dfs(int u){
	if(u <= M / 2){		// inner	
		dfs(u * 2);
		dfs(u * 2 + 1);
		calc(s[u].gate, u);
		if(s[u].change) calc(!s[u].gate, u, 1);
	}else{				// leaf
		s[u].cnt[s[u].val] = 0;
	}
}

int main(){
	int nCase;
	scanf("%d", &nCase);
	for(int ca = 1; ca <= nCase; ++ca){
		scanf("%d %d", &M, &V);
		memset(s, -1, sizeof(s));
		for(int i = 1; i <= M; ++i){
			if(i <= M / 2){
				scanf("%d %d", &s[i].gate, &s[i].change);
			}else{
				scanf("%d", &s[i].val);
			}
		}
		dfs(1);
		printf("Case #%d: ", ca);
		if(s[1].cnt[V] != -1) printf("%d\n", s[1].cnt[V]);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
