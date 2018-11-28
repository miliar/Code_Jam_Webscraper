#include<cstdio>
#include<cmath>
int l,p,c,t;
long double eps = 0.0000001;
int roundup(long double x){
	if(x-(long double)((int)x)>eps)
		return (int) x+1;
	else
		return (int) x;
}
int uu(int x){
	if (x<0)
		return 0;
	else
		return x;
}
inline long double log(int x, long double a){
	return log(a)/log((long double)x);
}
int main (){
    scanf("%d", &t);
    for(int q=1; q<=t; q++){
		scanf("%d%d%d",&l,&p,&c);
		printf("Case #%d: %d\n", q,uu(roundup(
					log(2,log(c,p)-log(c,l)))));
	}
}
