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

ll gcd(ll a,ll b){
	return b?gcd(b,a%b):a;
}

main(){
	int datasuu;
	scanf("%d ",&datasuu);
	for(int casenum=1;casenum<=datasuu;casenum++){
		printf("Case #%d: ",casenum);
		
		ll n,pd,pg;
		scanf("%lld%lld%lld",&n,&pd,&pg);
		if(pg==0){
			if(pd==0)puts("Possible");
			else puts("Broken");
		}else if(pg==100){
			if(pd==100)puts("Possible");
			else puts("Broken");
		}else{
			ll mul=100/gcd(100,pd);
			if(mul<=n)puts("Possible");
			else puts("Broken");
		}
	}
}