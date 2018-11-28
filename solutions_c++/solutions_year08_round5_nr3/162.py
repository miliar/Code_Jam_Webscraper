#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VInt;

#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(i = (a) - 1; i >= (b); --i)
#define CLEAR(a, b) memset(a, b, sizeof(a))
#define SIZE(a) int((a).size())
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair

int m[20];
int ok[1024];
int okcnt[1024];
int R,C,K;
int dp[20][1024];

int s2i(char *s){
	int i,l,res;
	l=strlen(s);
	res=0;
	for (i=0;i<l;i++) if (s[i]=='x') res|=(1<<i);
	return res;
}

int getBit(int b){
	int res=0;
	while (b){
		if (b&1) res++;
		b>>=1;
	}
	return res;
}

void solve(int cas){
	int r,i,j,ii,jj;
	int res=0;
	char s[20];
	scanf("%d%d",&R,&C);
	for (i=0;i<R;i++){
		scanf("%s",s);
		m[i]=s2i(s);
	}
	K=0;
	for (i=(1<<C)-1;i>=0;i--){
		if (i&(i<<1)) continue;
		ok[K]=i;
		okcnt[K]=getBit(i);
		K++;
	}
	memset(dp,-1,sizeof(dp));
	dp[0][K-1]=0;
	for (r=0;r<R;r++){
//		printf("mr=%d\n",m[r]);
		for (i=0;i<K;i++){
			ii=ok[i];
			if (ii&m[r]) continue;
			for (j=0;j<K;j++){
				jj=ok[j];
				if (ii&(jj>>1)) continue;
				if (ii&(jj<<1)) continue;
				if (dp[r][j]==-1) continue;
				dp[r+1][i]=max(dp[r+1][i],dp[r][j]+okcnt[i]);
				res=max(res,dp[r+1][i]);
			}
//			printf("dp[%d][%d]=%d\n",r+1,ii,dp[r+1][i]);
		}
	}
	printf("Case #%d: %d\n",cas,res);
}

int main(){
	int t,cas;
	scanf("%d",&t);
	for (cas=1;cas<=t;cas++)
		solve(cas);
    return 0;
}
