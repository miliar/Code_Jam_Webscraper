#include<cstdio>
#include<iostream>

using namespace std;

int main(){
	int t,n,k;
	cin>>t;
	for(int i=1;i<=t;++i){
		scanf("%d%d",&n,&k);
		if((k+1)%(1<<n)==0)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}
