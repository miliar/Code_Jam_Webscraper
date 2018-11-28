#include<stdio.h>
#include<algorithm>
using namespace std;

const int INF=1000000;

struct Node {
	char tp, cg;
}nds[10000];

int M;
pair<int, int> dfs(int p) {
	if(p>(M-1)/2) {
		if(nds[p].tp==1) return make_pair<int, int>(INF, 0);
		else return make_pair<int, int>(0, INF);
	} else {
		pair<int, int> l=dfs(p*2), r=dfs(p*2+1);
		
		int a1=l.second+r.second, a0=min(l.first+min(r.first, r.second), min(l.first, l.second)+r.first);
		int o1=min(l.second+min(r.first, r.second), min(l.first, l.second)+r.second), o0=l.first+r.first;
		
		if(!nds[p].cg) {
			if(nds[p].tp==1) o1=o0=INF;
			else a1=a0=INF;
		}

		if(nds[p].tp==1) o1++, o0++;
		else a1++, a0++;

		return make_pair(min(min(a0, o0), INF), min(min(a1, o1), INF));
	}
}

int main() {
	int n;
	scanf("%d", &n);
	for(int cas=1;cas<=n;cas++) {
		int V;
		scanf("%d%d", &M, &V);
		int i;
		for(i=1;i<=(M-1)/2;i++) {
			int tp, cg;
			scanf("%d%d", &tp, &cg);
			nds[i].tp=tp; nds[i].cg=cg;
		}
		for(;i<=M;i++) {
			int v;
			scanf("%d", &v);
			nds[i].tp=v;
		}
		pair<int, int> res=dfs(1);
		printf("Case #%d: ", cas);
		if(V==1)
			if(res.second==INF) puts("IMPOSSIBLE");
			else printf("%d\n", res.second);
		else
			if(res.first==INF) puts("IMPOSSIBLE");
			else printf("%d\n", res.first);
	}
	return 0;
}