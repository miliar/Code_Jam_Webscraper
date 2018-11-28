#include<iostream>
#include<cstring>
using namespace std;
int p,n;
int need[1024];
int cost[1024];
int dp_table[1024][10];
int dp(int node,int remain){
	if(node>=n-1){
		node-=n-1;
		if(remain<need[node])
			return 0x1fffffff;
		return 0;
	}else if(dp_table[node][remain]==-1){
		dp_table[node][remain] = min(
			cost[node]+dp(node*2+1,remain+1)+dp(node*2+2,remain+1),
			dp(node*2+1,remain)+dp(node*2+2,remain)
		);
		if(remain>0)
			dp_table[node][remain] = min(
				dp_table[node][remain],
				dp(node,remain-1)
			);
	}
	if(dp_table[node][remain]>0x1fffffff)
		return 0x1fffffff;
	return dp_table[node][remain];
}
int main(){
	int t;
	cin>>t;
	for(int kk=1;kk<=t;++kk){
		memset(dp_table,-1,sizeof(dp_table));
		cin>>p;
		n=1<<p;
		for(int i=0;i<n;++i){
			cin>>need[i];
			need[i]=p-need[i];
		}
		for(int i=p-1;i>=0;--i)
			for(int j=0;j<(1<<i);++j)
				cin>>cost[(1<<i)+j-1];
		printf("Case #%d: %d\n",kk,dp(0,0));
	}
	return 0;
}
