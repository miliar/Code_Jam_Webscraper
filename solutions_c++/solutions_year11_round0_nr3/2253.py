#include<stdio.h>
int a[1001];
main(){
	int i,j,k;
	int T,TT;
	int n,x,y,z;
	scanf("%d",&T);
	for(TT=1;TT<=T;TT++){
		scanf("%d",&n);
		x=y=0;
		z=1000000000;
		for(i=0;i<n;i++){
			scanf("%d",&a[i]);
			x^=a[i];
			y+=a[i];
			z<?=a[i];
		}
		if(x){
			printf("Case #%d: NO\n",TT);
		} else {
			printf("Case #%d: %d\n",TT,y-z);
		}
			
	}
}
