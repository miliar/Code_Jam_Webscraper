#include<stdio.h>
#include<stdlib.h>
int LCM(int a,int b){
	int q;
	if(b>a){
		q=a;
		a=b;
		b=q;
	}
	if(b==0) return a;
	do{
		q=a-(a/b)*b;
		a=b;
		b=q;
	}while(q);
	return a;
}
int LCM(int* N,int n){
	int i;
	int lcm;
	lcm=N[0];
	for(i=1;i<n;i++) lcm=LCM(lcm,N[i]);
	return lcm;
}
void warning(){
	int c,lcm,N[1000],diff[999];
	int i;
	scanf("%i",&c);
	scanf("%i",&N[0]);
	for(i=1;i<c;i++){
		scanf("%i",&N[i]);
		diff[i-1]=abs(N[i]-N[0]);
	}
	lcm=LCM(diff,c-1);
	if(N[0]%lcm) printf("%i",(N[0]/lcm+1)*lcm-N[0]);
	else printf("0");
}
int main(){
	int n;
	int i;
	scanf("%i",&n);
	for(i=0;i<n;i++){
		printf("Case #%i: ",i+1);
		warning();
		printf("\n");
	}
	return 0;
}
