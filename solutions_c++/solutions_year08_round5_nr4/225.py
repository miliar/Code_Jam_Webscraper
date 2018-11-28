#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

const int maxn = 1000;
const double eps = 1e-10;
const double pi = 2.0*acos(0.0);
const int INF = 1000000000;
const int mod = 10007;
#define sqr(a) ((a)*(a))
#define nul(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))

int dp[maxn][maxn];
bool was[maxn][maxn];
bool bad[maxn][maxn];
int h,w,r;

void init(){
	nul(was);
	nul(bad);
	scanf("%d%d%d",&h,&w,&r);
	int i,x,y;
	for (i = 0 ; i<r ; i++){
		scanf("%d%d",&x,&y);
		bad[x][y] = true;
	}
}

int rec(int x, int y){
	if (was[x][y])
		return dp[x][y];
	if (x==1 && y==1){
		return dp[x][y] = 1;
	}
	was[x][y] = true;
	int i,j,res = 0;
	for (i = 1 ; i<=x ; i++){
		for (j = 1 ; j<=y ; j++){
			if (sqr(i-x)+sqr(j-y)==5 && !bad[i][j]){
				res = (res+rec(i,j))%mod;
			}
		}
	}
	return dp[x][y] = res;
}

void solve(){
	printf("%d",rec(h,w));
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int i;
	for (i = 1 ; i<=t ; i++){
		printf("Case #%d: ",i);
		init();
		solve();
		printf("\n");
	}
	return 0;
}