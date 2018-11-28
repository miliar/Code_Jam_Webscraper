#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

#define INF 1023456789

#define modp(x) (((x)%P+P)%P)

typedef long long ll;

bool prm[1000010];
#define M 1000000

main(){
	for(ll i=2;i<=M;i++)prm[i]=true;
	for(ll i=2;i<=M;i++){
		if(prm[i])for(ll j=2*i;j<=M;j+=i)prm[j]=false;
	}
	int datasuu;
	scanf("%d ",&datasuu);
	for(int casenum=1;casenum<=datasuu;casenum++){
		printf("Case #%d: ",casenum);
		
		ll n;
		scanf("%lld",&n);
		if(n==1)puts("0");
		if(n==2)puts("1");
		if(n==3)puts("1");
		if(n>=4){
			ll ans=1;
			for(ll i=2;i*i<=n&&i<=M;i++){
				if(prm[i]){
					ll p=1;
					ll j;
					for(j=0;;j++){
						p*=i;
						if(p>n)break;
					}
					//printf("%lld^%lld\n",i,j);
					ans+=j-1;
				}
			}
			printf("%lld\n",ans);
		}
	}
}