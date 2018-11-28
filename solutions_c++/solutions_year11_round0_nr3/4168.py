#include<cstdio>
#include<algorithm>
#include<cmath>

using namespace std;

#define GI ({int t;scanf("%d",&t); t;})
#define FOR(i,a,b) for(typeof(a) i = a;i != b;++i)
#define ss(x) printf(#x" = %d\n",x)

typedef long long LL;

LL pile[10001];
LL fxor[10001];
LL rxor[10001];
LL lsum[10001];
LL rsum[10001];

int main() {
int t = GI;

for(int tt = 0;tt < t;++tt){
	int N = GI;	
	FOR(i,0,N)
		pile[i] = GI;

	sort(pile, pile + N);
	
	fxor[0] = pile[0];
	FOR(i,1,N)
		fxor[i] = fxor[i-1] ^ pile[i];
	
	rxor[N-1] = pile[N-1];
	for(int i = N - 2;i >= 0;i--)
		rxor[i] = rxor[i+1] ^ pile[i];

	lsum[0] = pile[0];
	FOR(i,1,N)
		lsum[i] = pile[i] + lsum[i-1];

	rsum[N-1] = pile[N-1];
	for(int i = N-2;i >=0 ;i --)
		rsum[i] = pile[i] + rsum[i+1];
		
	LL maxi = 0;
	FOR(i,1,N){
		if(fxor[i-1] == rxor[i]){
			maxi = max(maxi, lsum[i-1]);
			maxi = max(maxi, rsum[i]);
		}		
	}
	
	if(maxi == 0)
		printf("Case #%d: NO\n",tt+1);
	else
		printf("Case #%d: %lld\n",tt+1,maxi);
}

return 0;
}



