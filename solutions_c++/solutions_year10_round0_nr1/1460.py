#include<iostream>
#include<cstdio>
using namespace std;
main(){
	int t,n,k;
	cin>>t;
	for(int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		scanf("%d%d",&n,&k);
		if((k+1)%(1<<n))
		    puts("OFF");
		else
			puts("ON");
	}
	return 0;
}
