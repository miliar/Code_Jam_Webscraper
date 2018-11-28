#include<cstdio>

#define rep(i,n) for(int i=0;i<(n);i++)

using namespace std;

typedef long long ll;

int gcd(int a,int b){ return b?gcd(b,a%b):a; }

int main(){
	int T0; scanf("%d",&T0);
	for(int T=1;T<=T0;T++){
		ll n;
		int pd,pg; scanf("%lld%d%d",&n,&pd,&pg);

		bool res;
		if     (pg==  0) res=(pd==  0);
		else if(pg==100) res=(pd==100);
		else{
			if(n>=100) res=true;
			else{
				int g=gcd(pd,100);
				res=(100/g<=n);
			}
		}

		printf("Case #%d: %s\n",T,res?"Possible":"Broken");
	}

	return 0;
}
