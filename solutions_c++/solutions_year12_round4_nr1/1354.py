#include <cstdio>
#include <cstring>

inline int min(int a, int b){return a < b? a :b;}
inline int Abs(int a){return a > 0? a: -a;}

int N;
int D[10002], L[10002];
int T, t = 1;
int vst[10002][10002];
bool DFS(int from, int now, int len){
	//printf("%d %d %d\n", from, now, len);
	if(now == N + 1) return true;
	vst[from][now] = t;
	for(int i = 1; i <= N + 1; i++)
		if(now != i && Abs(D[i] - D[now]) <= len && vst[now][i] != t)
			if(DFS(now, i, min(L[i], Abs(D[i] - D[now]))))return true;
	return false;
}

 /*(*/
int main(){
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	
	scanf("%d", &T);
	for(t = 1; t <= T; t++){
		scanf("%d", &N);
		for(int i = 1; i <= N; i++)
			scanf("%d%d", &D[i], &L[i]);
		scanf("%d", &D[N + 1]);
		printf("Case #%d: %s\n", t, DFS(0, 1, D[1])? "YES": "NO");
	}
}
