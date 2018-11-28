#include<iostream>
#include<cstdio>
#include<cstdlib>

void solve(){
	long long n,k;
	bool isOn;
	scanf("%lld%lld",&n,&k);

	isOn=( (k+1)%(1<<n) == 0);

	if(isOn){
		printf("ON\n");
	}
	else{
		printf("OFF\n");
	}	
}

main(){
	int i,t;
	scanf("%d",&t);

	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		solve();
	}
}
