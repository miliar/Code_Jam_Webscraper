#include<cstdio>
#include<algorithm>
using namespace std;
typedef long long ll;

int t;
ll n,k;

bool check(int il,int x) {
	while(il--) {
		if(x%2==0) return false;
		x/=2;
	}
	return true;
}

int main() {
	scanf("%d",&t);
	for(int i = 1; i <= t; ++i) {
		scanf("%lld%lld",&n,&k);
		if(check(n,k)) printf("Case #%d: ON\n",i);
		else printf("Case #%d: OFF\n",i);
	}
}
