#include <iostream>
#include <cstdio>

#define floop(i,a,b) for(int i=(a);i<(b);i++)
#define rloop(i,a,b) for(int i=(a);i>=(b);i--)

int arr[2000];

void process(int testcase){
	int N,min=10000000,val=0;
	long long sum=0;
	scanf("%d",&N);
	floop(i,0,N){
		scanf("%d",(arr+i));
		min=(arr[i]<min)?arr[i]:min;
		sum+=arr[i];
		val=val^arr[i];
	}

	printf("Case #%d: ",testcase);

	if(val){
		printf("NO\n");
	}else{
		printf("%lld\n",sum-min);
	}
	
}

main(){
	int testcases;
	scanf("%d",&testcases);
	floop(i,0,testcases){
		process(i+1);
	}
}
