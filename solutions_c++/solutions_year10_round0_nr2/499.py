#include <iostream>
#include <string>
#include <cstdio>
using namespace std;
long long num[10];
long long gcd(long long a,long long b){
	if(b==0)
		return a;
	else return gcd(b,a%b);
}
long long getabs(long long a){
	return a>0?a:(-a);
}
int main(){
	freopen("B-small-attempt0.in","rb",stdin);
	freopen("B-small-attempt0.out","wb",stdout);
	int ca,t=0,n;
	int i;
	scanf("%d",&ca);
	while(ca--){
		t++;
		scanf("%d",&n);

		long long abc;
		for(i=0;i<n;i++)
			scanf("%lld",&num[i]);
		abc=getabs(num[1]-num[0]);
		for(i=0;i<n;i++){
			abc=gcd(abc,getabs(num[(i+1)%n]-num[i]));
		}

		long long res;
		if(num[0]%abc==0)
			res=0;
		else res=(num[0]/abc+(long long)1)*abc-num[0];
		printf("Case #%d: %lld\n",t,res);
	}
	return 0;
}