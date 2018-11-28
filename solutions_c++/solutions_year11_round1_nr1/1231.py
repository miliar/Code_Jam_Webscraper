#include<stdio.h>
int gcd(int a,int b){
	int t; 
	while(a%b){
		t=a%b;
		a=b;
		b=t; 
	}
	return b; 
} 
int ch(int N,int D,int G){
	if(D==0){
		if(G==100)return 0;
		return 1; 
		} 
	if(D>0){
			if(G==0)return 0; 
		} 
	if(D<100&&G==100)return 0; 
	int x=gcd(D,100),y,z;
	y=100/x;
	D/=x;
	if(y>N)return 0;
	return 1; 
} 
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,N,D,G,t;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%d%d",&N,&D,&G);
		if(ch(N,D,G))printf("Case #%d: Possible\n",t);
		else  printf("Case #%d: Broken\n",t);
	} 
}
 
