#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int maxn = 10000;
const int INF = 1000000000;
const double eps = 1e-10;

#define nul(a) memset(a,0,sizeof(a))

int yk = 0;
long long n,m,X,Y,Z;
long long a[maxn];
const int module = 1000000007;
long long A[maxn];

void init(){
	scanf("%lld%lld%lld%lld%lld",&n,&m,&X,&Y,&Z);
	int i;
	nul(A);
	for (i = 0 ; i<m ; i++){
		scanf("%d",&A[i]);
	}
	yk =0;
	for (i = 0 ; i<n ; i++){
		a[yk++] = A[i%m];
		A[i%m] = (X*A[i%m]+Y*(i+1))%Z;
	}
}

long long dp[maxn];

void solve(){
	dp[0] = 1;
	int i;
	long long res = 1;
	for (i = 1 ; i<n ; i++){
		int j;
		dp[i] = 1;
		for (j = i-1 ; j>=0 ; j--){
			if (a[i]>a[j]){
				dp[i]+=dp[j];
				dp[i]%=module;
			}
		}
		res+=dp[i]%module;
	}
	res%=module;
	printf("%lld",res);
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