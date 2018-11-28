#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int maxn = 40100;
const int INF = 100000000;
const double eps = 1e-10;

#define nul(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))
#define sqr(a) ((a)*(a))

int dp[maxn][2];
bool was[maxn][2];
int v[maxn];
bool can[maxn];
bool type[maxn];

int n,need;

int rec(int tek, int val){
	if (was[tek][val]){
		return dp[tek][val];
	}
	was[tek][val] = true;
	if (tek>=(n+1)/2){
		if (val==v[tek])
			return dp[tek][val] = 0;
		else
			return dp[tek][val] = INF;
	}
	int t1,t2,res = INF;
	if (type[tek]==0){//or
		
		if (val==0){
			t1 = rec(tek*2,0);
			t2 = rec(tek*2+1,0);
			if (t1!=INF && t2!=INF){
				res = t1+t2;
			}
			if (can[tek]){
				res = min(res,min(t1,t2)+1);
			}
		} else{
			t1 = rec(tek*2,1);
			t2 = rec(tek*2+1,1);
			res = min(t1,t2);
			if (can[tek]){
				res = min(res,t1+t2+1);
			}
		}
	} else{
		if (val==0){
			t1 = rec(tek*2,0);
			t2 = rec(tek*2+1,0);
			res = min(res,min(t1,t2));
			if (can[tek]){
				res = min(res,t1+t2+1);
			}
		} else{
			t1 = rec(tek*2,1);
			t2 = rec(tek*2+1,1);
			res = min(res,t1+t2);
			if (can[tek]){
				res = min(res,min(t1,t2)+1);
			}
		}
	}
	return dp[tek][val] = res;
}

void init(){
	nul(was);
	scanf("%d%d",&n,&need);
	int i;
	for (i = 1 ; i<=(n-1)/2 ; i++){
		scanf("%d%d",&type[i],&can[i]);
	}
	for (i = (n+1)/2 ; i<=n ; i++){
		scanf("%d",&v[i]);
	}
}

void solve(){
	int res = rec(1,need);
	if (res==INF){
		printf("IMPOSSIBLE");
	} else
		printf("%d",res);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i;
	scanf("%d",&t);
	for (i = 0 ; i<t ; i++){
		printf("Case #%d: ",i+1);
		init();
		solve();
		printf("\n");
	}
	return 0;
}