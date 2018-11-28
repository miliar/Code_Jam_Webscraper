#include<iostream>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for (int t=1;t<=T;++t){
		int n,k;
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",t);
		if ((k%(1<<n))==((1<<n)-1)) printf("ON\n");else printf("OFF\n");
	}
}
