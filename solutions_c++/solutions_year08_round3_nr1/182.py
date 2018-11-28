#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int maxn = 110;

const double eps = 1e-10;

#define nul(a) memset(a,0,sizeof(a))

long long f[maxn];
int p,k,l;
/*long long dp[maxn][maxn][maxn],INF;
bool was[maxn][maxn][maxn];*/
 
void init(){
//	INF = 1000000000;
//	INF*=INF;
	scanf("%d%d%d",&p,&k,&l);
	int i;
	for (i =0  ; i<l ; i++){
		scanf("%lld",&f[i]);
	}
//	nul(was);
}
/*
long long rec(int let, int tekk,int kpos){
	if (tekk==k && let<l){
		return dp[let][tekk][kpos] = INF;
	}
	if (let==l){
		return dp[let][tekk][kpos] = 0;
	}
	if (was[let][tekk][kpos])
		return dp[let][tekk][kpos];
	int i;
	was[let][tekk][kpos] = true;
	if (kpos==p-1){
		return dp[let][tekk][kpos] = min(f[let]*(kpos+1)+rec(let+1,tekk+1,0),rec(let,tekk+1,0));
	} else{
		return dp[let][tekk][kpos] = min(f[let]*(kpos+1)+rec(let+1,tekk,kpos+1),rec(let,tekk+1,0));
	}
}
*/

void solve(){
	//long long res = rec(0,0,0);
	long long res = 0;
	sort(f,f+l);
	int i;
	int tekk = 0;
	int tekpos = 1;
	for (i = l-1 ; i>=0 ; i--){
		res+=f[i]*tekpos;
		tekk++;
		if (tekk==k){
			tekk = 0;
			tekpos++;
		}
	}
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