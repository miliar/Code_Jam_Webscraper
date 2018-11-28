#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int main(){
	int time=0, t, pd, pg, gcd, ans;
	long long n;
	scanf("%d", &t);
	while(t--){
		scanf("%I64d%d%d", &n, &pd, &pg);
		ans=0;
		gcd=__gcd(100, pd);
		if(100/gcd<=n){
			if(pg==100){
				if(pd==100) ans=1;
			}
			else if(pg==0){
				if(pd==0) ans=1;
			}
			else ans=1;
		}
		printf("Case #%d: %s\n", ++time, ans?"Possible":"Broken");
	}
    return 0;
}
