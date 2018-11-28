#include<cstdio>
long long d,pd,pg,t,n,ac;
int gcd(int x,int y){
	if (x%y==0) return y;
	else return gcd(y,x%y);
}
int main(){
	scanf("%d",&t);
	for (int z=1; z<=t; z++){
		  ac=1;
		  scanf("%d%d%d",&n,&pd,&pg);
		  if (pg==100&&pd!=100) ac=0;
		  if (pg==0&&pd!=0) ac=0;
		  else{
		  	  d=gcd(pd,100);
		  	  d=100/d;
		  	  if (n<d) ac=0;
		  }
		  if (ac) printf("Case #%d: Possible\n",z);
		  else printf("Case #%d: Broken\n",z);
	}
	return 0;
}
