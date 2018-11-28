#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <cstring>
using namespace std;

int tr[1<<12];
int price[1<<12];
int dp[1<<12][13];
int M[1<<12];
int p,tt;

inline int lson(int x){
	return (x<<1)|1;
}
inline int rson(int x){
	return (x<<1)+2;
}

int getdp(int depth,int v,int buyed){
	if(dp[v][buyed]>=0)return dp[v][buyed];
	if(buyed>=p-tr[v])return dp[v][buyed] = 0;
	if(p-depth+buyed==p-tr[v])
		return dp[v][buyed] = price[v] + getdp(depth+1,lson(v),buyed+1) + getdp(depth+1,rson(v),buyed+1);
	int best = price[v]  + getdp(depth+1,lson(v),buyed+1) + getdp(depth+1,rson(v),buyed+1);
	best = min(best,getdp(depth+1,lson(v),buyed) + getdp(depth+1,rson(v),buyed));
	return dp[v][buyed] = best;
}

int main(){
	int tc;
	cin>>tc;
	for(tt=1;tt<=tc;tt++){
		printf("Case #%d: ",tt);
		cin>>p;
		int i,j,base;
		for(i=0;i<(1<<p);i++){
			cin>>M[i];
		}
		for(i=p-1;i>=0;i--){
			base = (1<<i) - 1;
			for(j=0;j<(1<<i);j++)
				cin>>price[base+j];
		}	
		base = (1<<p) - 1;
		for(i=0;i<(1<<(p));i++){
			tr[base+i] = M[i];	
		}
		for(i=base-1;i>=0;i--){
			tr[i] = min(tr[lson(i)],tr[rson(i)]);	
		}
		memset(dp,-1,sizeof(dp));
		printf("%d\n",getdp(0,0,0));
	}

	return 0;
}
