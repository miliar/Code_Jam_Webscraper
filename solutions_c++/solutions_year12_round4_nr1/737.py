#include<cstdio>
#include<algorithm>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

void solve(){
	int n; scanf("%d",&n);
	int x[10000],len[10000];
	rep(i,n) scanf("%d%d",x+i,len+i);
	int goal; scanf("%d",&goal);

	int dp[10000]={}; // 蔦 i をベースにしたとき、最大でどこまで遠くにいけるか
	dp[0]=2*x[0];
	rep(i,n){
		for(int j=i+1;j<n;j++){
			if(x[j]>dp[i]) break;
			dp[j]=max(dp[j],x[j]+min(len[j],x[j]-x[i]));
		}
	}
	puts(*max_element(dp,dp+n)>=goal?"YES":"NO");
}

int main(){
	int T; scanf("%d",&T);
	for(int t=1;t<=T;t++) printf("Case #%d: ",t), solve();
	return 0;
}
