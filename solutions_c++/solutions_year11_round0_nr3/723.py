#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int main(){
	int h,i,j,k,l,m,t,n;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d",&n);
		k=0;m=0;l=1e9;
		for(i=0;i<n;i++){
			scanf("%d",&j);
			m+=j;l=l>j?j:l;
			k=k^j;
		}
		printf("Case #%d: ",h);
		if(k!=0)printf("NO\n");
		else printf("%d\n",m-l);
	}
	return 0;
}
