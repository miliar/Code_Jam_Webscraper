#include<stdio.h>
using namespace std;
int t,n,check,min,tot,x;
int main(){
	scanf("%d",&t);
	for(int I=1;I<=t;++I){
		scanf("%d",&n);
		tot = 0;
		check = 0;
		min = 1<<30;
		for(int i=0;i<n;++i){
			scanf("%d",&x);
			tot +=x;
			min = (min<x)? min:x;
			check ^= x;
		}
		
		if(check == 0) printf("Case #%d: %d\n",I,tot-min);
		else printf("Case #%d: NO\n",I);
	}
	return 0;
}
