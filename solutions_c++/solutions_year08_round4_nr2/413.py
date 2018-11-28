#include<iostream>
#include<cmath>
int area(int xx1,int xx2,int yy1,int yy2){
	return xx1*yy2-xx2*yy1;
}
void func(int n,int m,int a){
	int xx1,xx2,yy1,yy2;
	for(xx1=0;xx1<=n;xx1++){
		for(xx2=0;xx2<=n;xx2++){
			for(yy1=0;yy1<=m;yy1++){
				for(yy2=0;yy2<=m;yy2++){
					if(abs(area(xx1,xx2,yy1,yy2))==a){
						printf("0 0 %d %d %d %d\n",xx1,yy1,xx2,yy2);
						return;
					}
				}
			}
		}
	}
	printf("IMPOSSIBLE\n");
}
main(){
	int tt,t,n,m,a;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%d",&n);
		scanf("%d",&m);
		scanf("%d",&a);
		printf("Case #%d: ",tt);
		func(n,m,a);
	}
	return 0;
}
