#include<stdio.h>
#include<algorithm>
using namespace std;
long long a,b,c,n,C,sel;
long long fpb(long long a,long long b){
	if(b==0) return a;
	return fpb(b, a % b);
}
int main(){
	scanf("%lld",&C);
	for(int i=1;i<=C;++i){
		scanf("%lld",&n);
		scanf("%lld%lld",&b,&a);
		sel=abs(a-b);
		for(int j=2;j<n;++j){
			scanf("%lld",&b);
			sel=fpb(abs(a-b),sel);
			a=b;
		}
		printf("Case #%d: %lld\n",i,(sel-(a%sel))%sel);
	}
	return 0;
}
