#include <cstdio>
#include <algorithm>
#include <cstring>
#include <numeric>
using namespace std;
typedef long long ll;

const int maxp = 1000000 + 1;
int pr[maxp/2];
int np;
bool isp[maxp + 1];

void init(){
	fill(isp,isp + maxp + 1,true);
	isp[0] = isp[1] = 0;
	for(int i = 2;i<=maxp;i++){
		if(isp[i])
			pr[np++] = i;
		for(int j = 0;j<np && (ll)pr[j] * i <= maxp;j++){
			isp[i * pr[j]] = false;
			if(i % pr[j]==0)break;
		}
	}
}


int main(){
	int tc;
	scanf("%d",&tc);
	init();
	for(int tt=1 ;tt<=tc;tt++){
		printf("Case #%d: ",tt);	
		ll n;
		scanf("%lld",&n);
		ll ans = n==1 ? 0:1;
		for(int i = 0;i<np;i++)if(pr[i] <= n){
			ll tn = n;
			while(tn/=pr[i])ans++;
			ans--;
		}else break;
		printf("%lld\n",ans);
	}
	return 0;
}
