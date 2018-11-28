

#include<iostream>
using namespace std;

const int mod=10000;
int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int t,ca,i,j,k,n;
	scanf("%d",&t);
	int l,r,ll,rr;
	for(ca=1;ca<=t;ca++){
		scanf("%d",&n);l=3;r=1;
		for(i=2;i<=n;i++){ 
			ll=l*3+r*5;rr=l+3*r;l=ll;r=rr;l=l%mod;r=r%mod;
		}
		printf("Case #%d: %03d\n",ca,l*2%1000-1);
	}

	return 0;
}
