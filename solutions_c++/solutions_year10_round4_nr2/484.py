#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstdio>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <deque>
#include <cmath>
#include <utility>

using namespace std;


typedef long long ll;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define DBG(x) cerr<<#x<<" = "<<x<<endl
#define DBGV(x) {cerr<<#x<<": "; for(int i=0;i<sz(c);i++) cerr<<x[i]<<" "; cerr<<endl;}
#define DBGA(x) {cerr<<#x<<": "; for(int i=0;i<int(sizeof(x)/sizeof(x[0]));i++) cerr<<x[i]<<" "; cerr<<endl;}

long long dp[1<<12][20];
const long long oo= 1000LL*1000LL*1000LL*1000LL*1000LL;


long long cost[1<<12];
long long solve(int v,int m){
	//
	//DBG(m);
	if(dp[v][m]!=-1) return dp[v][m];
	int i,j;
	int mini,minj;
	//DBG(v);
	//DBG(m);
	long long res=dp[v][m]=oo;
	mini=-1,minj=-1;
	for(i=0;i<=m;i++){
		for(j=0;j<=m;j++){
			res=min(res,solve(2*v,i)+solve(2*v+1,j));
		}
	}
	for(i=0;i<=m+1;i++){
		for(j=0;j<=m+1;j++){
			res=min(res,solve(2*v,i)+solve(2*v+1,j)+cost[v]);
		}
	}
	//cerr << "dp["<<v<<"]["<<m<<"]="<<res<<endl;
	return dp[v][m]=res;
}
int main(){
	assert(freopen("B.in","rt",stdin)==stdin);
	assert(freopen("B.out","wt",stdout)==stdout);
	int T,C,P;
	int m,s,j,i,k;
	scanf("%d",&T);
	for(C=1;C<=T;C++){
		scanf("%d",&P);
		//DBG(P);
		s=1<<P;
		memset(dp,-1,sizeof dp);
		for(;s<(1<<(P+1));s++){
			for(i=0;i<20;i++) dp[s][i]=oo;
			scanf("%d",&m);
			dp[s][P-m]=0;
		//	DBG(s);
		}
		vector< vector<int> > cc;
		cc.resize(P+1);
		for(i=1;i<=P;i++){
			cc[i].resize(1<<(P-i));
			for(j=0;j<(1<<(P-i));j++) scanf("%d",&cc[i][j]);
			//DBG(cc[i][j]);
		}
		k=1;
		for(i=P;i>=1;i--){
			for(j=0;j<(1<<(P-i));j++) cost[k++]=cc[i][j];
		}
		long long res=solve(1,0);
		cout << "Case #" << C << ": " << res << endl;
		//cout << res << endl;
	}
	return 0;
}
