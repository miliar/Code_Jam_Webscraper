#include <stdio.h>
#include <math.h>

#define min(a,b) ((a)>(b)?(b):(a))

int d[10000], l[10000];
int v[10000];
int D, N;

int dfs(int p, int h){
	if (d[p]+h >= D) 
		return 1;
	v[p] = h;
	for (int i = 0; i < N; i++){
		if (i < p && d[p]-h<=d[i] || i > p && d[p]+h>=d[i]){
			int h1 = min(abs(d[i]-d[p]), l[i]);
			if (v[i] < h1){
				if (dfs(i, h1)) return 1;
			}
		}
	}
	return 0;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int ttt = 1; ttt <= T; ttt++){
		scanf("%d", &N);
		for (int i =0 ; i < N; i++){
			scanf("%d%d", d+i, l+i);
			v[i] = 0;
		}
		scanf("%d", &D);
		if (dfs(0, d[0]))
			printf("Case #%d: %s\n", ttt, "YES");
		else
			printf("Case #%d: %s\n", ttt, "NO");
	}
	return 0;
}