#include <stdio.h>
#include <string.h>

typedef long long LL;
const int oo = 0x7fffffff;
int r,a[1024+1][11],cost[1024+1][11];
LL dp[1024+1][11][11];
int max(int x,int y){return x>y?x:y;}
int dfs(int s,int d,int c){
//	printf("get %d %d %d with %d\n",s,d,c,a[s][d]);
	if (d == 0){
		if (c >= a[s][d]) return 0;
		return -2;
	}
	int &r = dp[s][d][c];
	if (r != -1) return r;
	if (c >= a[s][d]) return r = 0;
	int r1,r2,c1,c2;
	c1 = dfs(s*2-1,d-1,c+1),c2 = dfs(s*2,d-1,c+1);
	if (c1 >= 0 && c2 >= 0)
		r1 = c1+c2+cost[s][d];
	else
		r1 = oo;
	c1 = dfs(s*2-1,d-1,c),c2 = dfs(s*2,d-1,c);
	if (c1 >= 0 && c2 >= 0)
		r2 = c1+c2;
	else
		r2 = oo;
	r = r1 < r2?r1:r2;
	if (r == oo) r = -2;
//	printf("get %d %d %d : %d(%d) %d => %d\n",s,d,c,r1,cost[s][d],r2,r);
	return r;
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,P,t,n,i,j,hi;
	scanf("%d",&T);
	for (t = 1;t <= T;t++){
		scanf("%d",&P);
		n = 1 << P;
		for (i = 1;i <= n;i++){
			scanf("%d",&a[i][0]);
			a[i][0] = P-a[i][0];
		}
		for (i = 1;i <= P;i++){
			hi = 1 << (P-i);
			for (j = 1;j <= hi;j++)
				a[j][i] = max(a[j*2-1][i-1],a[j*2][i-1]);
		}
		//for (i = 0;i <= P;i++){
		//	hi = 1 << (P-i);
		//	for (j = 1;j <= hi;j++)
		//		printf("%d ",a[j][i]);
		//	puts("");
		//}
		for (i = 1;i <= P;i++){
			hi = 1 << (P-i);
			for (j = 1;j <= hi;j++)
				scanf("%d",&cost[j][i]);
		}
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %lld\n",t,dfs(1,P,0));
	}
	fclose(stdout);
}
