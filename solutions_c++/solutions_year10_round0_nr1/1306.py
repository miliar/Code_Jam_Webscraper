#include<stdio.h>
using namespace std;
int t,n,k;
int main(){
	scanf("%d\n",&t);
	for(int i=1;i<=t;++i){
		scanf("%d%d",&n,&k);
		if((((1<<n)-1) & k) == (1<<n)-1) printf("Case #%d: ON\n",i);
		else printf("Case #%d: OFF\n",i);
	}
	return 0;
}
