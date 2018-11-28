#include <stdio.h>
#include <string.h>

int p;
int n;
int dat[1024]; // must see at least dat[i]
int price[12][1024]; // price
int dt[12][1024][12]; // (i,j) game, k games watched

int dfs(int i,int j,int k){
	if(i == p){
		if(k < dat[j]){
			return 100000 * 4096;
		}
		return 0;
	}
	if(dt[i][j][k] >= 0) return dt[i][j][k];
	int ans = 100000 * 4096;

	int tmp = dfs(i+1,j*2,k) + dfs(i+1,j*2+1,k);
	if(tmp < ans){
		ans = tmp;
	}
	tmp = dfs(i+1,j*2,k+1) + dfs(i+1,j*2+1,k+1) + price[i][j];
	if(tmp < ans){
		ans = tmp;
	}

	return (dt[i][j][k] = ans);
}

int main(){
	int testcase = 0;
	int T;
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	scanf("%d",&T);
	while(T-- > 0){
		int ans;
		int i,j;
		++ testcase;
		memset(dt,-1,sizeof(dt));
		scanf("%d",&p);
		n = (1<<p);
		for(i=0;i<n;i++){
			scanf("%d",&dat[i]);
			dat[i] = p-dat[i];
		}
		for(i=p-1;i>=0;i--){
			for(j=0;j<(1<<i);j++){
				scanf("%d",&price[i][j]);
			}
		}

		ans = dfs(0,0,0);

		printf("Case #%d: %d\n",testcase,ans);
	}
	return 0;
}
