#include<stdio.h>
#include<stdlib.h>

#define MOD 1000000007
#define MAXN 1000000

int f(const void * a, const void * b) {
	return *(int*)a-*(int*)b;
}


int tree[MAXN], MaxVal;

int read(int idx){
	int sum = 0;
	while (idx > 0){
		sum += tree[idx];
		sum %= MOD;
		idx -= (idx & -idx);
	}
	return sum;
}

void update(int idx ,int val){
	while (idx <= MaxVal){
		tree[idx] += val;
		tree[idx] %= MOD;
		idx += (idx & -idx);
	}
}

int ar[MAXN], br[MAXN], dp[MAXN];
int A[MAXN];

int n, m, X, Y, Z;

int findV(int v) {
	int st=0,en=m-1,md;
	while(st<=en) {
		md = (st+en)/2;
		if(br[md]==v) return md;
		if(br[md]> v) en = md-1;
		else st=md+1;
	}
	return -1;
}

int main() {
	int t,T,i,j,k,ans;
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++) {
		scanf("%d %d %d %d %d", &n, &m, &X, &Y, &Z);
		for(i = 0;i<m;i++) {
			scanf("%d",A+i);
		}
		for(i = 0;i<n;i++) {
			ar[i] = br[i] = A[i % m];
			A[i % m] = ((__int64)X * A[i % m] + (__int64)Y * (i + 1)) % Z;
		}
		qsort(br,n,sizeof(int),f);
		k=0;
		for(i=1;i<n;i++) {
			if(br[k]!=br[i]) {
				br[++k] = br[i];
			}
			tree[i] = 0;
		}
		m = k+1;
		MaxVal = m;
		for(i=0;i<n;i++) {
			dp[i] = 1 + read(findV(ar[i]));
			update(findV(ar[i])+1,dp[i]);
		}
		ans=0;
		for(i=0;i<n;i++) {
			ans += dp[i];
			ans %= MOD;
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}