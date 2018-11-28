#include <stdio.h>
#include <math.h>
#include <string.h>
#include <vector>
#include <queue>
#include <algorithm>
#include <stdlib.h>

using namespace std;

#define min(a,b) ((a)>(b)?(b):(a))
#define max(a,b) ((a)>(b)?(a):(b))

#define INF 1000000
#define maxn 1000

int n;
long long a[maxn];
long long b[maxn];


void init(){
	scanf("%d",&n);
	int i;
	for (i=0;i<n;i++)
		scanf("%lld",&a[i]);
	for (i=0;i<n;i++)
		scanf("%lld",&b[i]);
	sort(a,a+n);
	sort(b,b+n);
}

void solve(){
	long long res=0;
	int i;
	for (i=0;i<n;i++){
		res+=a[i]*b[n-i-1];
	}
	printf("%lld\n",res);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ntest,i;
	scanf("%d",&ntest);
	for (i=1;i<=ntest;i++){
		init();
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}