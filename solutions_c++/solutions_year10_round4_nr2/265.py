#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define BIT(X,B) (((X)>>(B))&1)
#define SET(X,B) ((X)|(1<<(B)))
#define CLR(X,B) ((X)&(~(1<<(B))))
#define REV(X,B) ((X)^(1<<(B)))

int dp[16][1<<11],n;
int m[1<<11],pr[1<<11];
const int Inf=0x3f3f3f3f;
int DP(int i,int j){
	if(i>=n) return j>=m[i-n]?0:Inf;
	int &res=dp[j][i];
	if(res!=-1) return res;
	res=min(DP(i*2,j+1)+DP(i*2+1,j+1)+pr[i],
	        DP(i*2,j)+DP(i*2+1,j));
	if(res>Inf) res=Inf;
	return res;
}
int main(){
	int TT;
	scanf("%d",&TT);
	for(int cas=1;cas<=TT;++cas){
		int P;
		scanf("%d",&P);
		n=(1<<P);
		for(int i=n-1;i>=0;--i){
			scanf("%d",m+i);
			m[i]=P-m[i];
		}
		for(int i=n-1;i>0;--i){
			scanf("%d",pr+i);
		}
		memset(dp,-1,sizeof(dp));
		printf("Case #%d: %d\n",cas,DP(1,0));
	}
	return 0;
}
