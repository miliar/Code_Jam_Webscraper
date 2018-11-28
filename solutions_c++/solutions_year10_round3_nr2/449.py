#include <stdio.h>

void solve(){
	int l,p,c,tmp,count=0;
	scanf("%d %d %d", &l, &p, &c);
	while(l*c < p){
		l*=c;
		count++;
	}
	l=0;
	while(count>0){
		count/=2;
		l++;
	}
	printf("%d\n", l);
}
int main(){
	int i,T;
	scanf("%d", &T);
	for(i=1;i<=T;i++){
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
