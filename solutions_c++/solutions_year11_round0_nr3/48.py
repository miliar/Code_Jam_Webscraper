#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long ll;
int main(){
	int runs, n;
	scanf("%d",&runs);
	for(int r = 1; r <= runs; r++){
		scanf("%d",&n);
		ll tmp = 1<<30, res = 0, N = 0;
		for(int i = 0; i < n; i++){
			ll val; scanf("%lld",&val);
			res = res xor val; N += val;
			tmp = min(tmp,val);
		}
		if (res == 0) printf("Case #%d: %lld\n",r,N-tmp);
		else printf("Case #%d: NO\n",r);
	}
return 0;
}
