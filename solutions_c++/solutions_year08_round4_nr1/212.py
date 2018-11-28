#include <cstdio>
#define MAXN 10000
#define INFINITy 1000000000

int n, V;

int g[MAXN], c[MAXN], val[MAXN][2];

int min(int a, int b){
	return (a<b?a:b);
}

int main(){
	freopen("boolean.in", "rt", stdin);
	freopen("boolean.out", "wt", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		scanf("%d%d", &n, &V);
		for (int i = 0; i < n; i++) val[i][0] = val[i][1] = INFINITy;
		for (int i = 0; i < (n-1)/2; i++)
			scanf("%d %d", &g[i], &c[i]);
		for (int i = (n-1)/2; i < n; i++){
			int ee;
			scanf("%d", &ee);
			val[i][ee] = 0;
		}
		for (int i = (n-3)/2; i >= 0; i--){
			int v1[2], v2[2], v[2][2];
			v1[0] = val[i*2+1][0];
			v1[1] = val[i*2+1][1];
			v2[0] = val[i*2+2][0];
			v2[1] = val[i*2+2][1];
//			printf("%d %d %d %d\n", v1[0],v1[1],v2[0],v2[1]);
			v[0][0] = v[1][0] = v[0][1] = v[1][1] = INFINITy;

			//0 - OR
			//1 - AND

			//[OR\AND][FALSE..TRUE];

			v[0][0] <?= v1[0]+v2[0];

			v[0][1] <?= v1[1]+v2[1];
			v[0][1] <?= v1[0]+v2[1];
			v[0][1] <?= v1[1]+v2[0];

			v[1][0] <?= v1[0]+v2[0];
			v[1][0] <?= v1[0]+v2[1];
			v[1][0] <?= v1[1]+v2[0];

			v[1][1] <?= v1[1]+v2[1];

			if (g[i]==0){//or
				val[i][0] = v[0][0];
				val[i][1] = v[0][1];
				if (c[i]){
					val[i][0] <?= v[1][0]+1;
					val[i][1] <?= v[1][1]+1;
				}
			}
			else{
				val[i][0] = v[1][0];
				val[i][1] = v[1][1];
				if (c[i]){
					val[i][0] <?= v[0][0]+1;
					val[i][1] <?= v[0][1]+1;
				}
			}
		}

		printf("Case #%d: ", t);
		if (val[0][V]>100000) printf("IMPOSSIBLE\n"); else printf("%d\n", val[0][V]);

//		for (int i = 0; i < n; i++) printf("%d %d\n", val[i][0], val[i][1]);
//		printf("\n\n\n");

	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
