#include <stdio.h>
#define FOR(i,a,b) for(i=(a);i<=(b);i++)

typedef long long ll;

int t,T;
int n,pd,pg;

int gcd(int a, int b){
	if (a<b) return gcd(b,a);
	if (b==0) return a;
	return gcd(b,a%b);
}

int process(){
	int wd,ds,wg,gs;
	if (pd==0){
		wd = 0;
		ds = 1;
	}
	else{
		if (100%gcd(pd,100)) return false;
		ds = 100/gcd(pd,100);
		wd = ds * pd / 100;
	}

	if (ds > n) return false;

	if (pg==0){
		wg = 0;
		gs = 1;
	}
	else{
		if (100%gcd(pg,100)) return false;
		gs = 100/gcd(pg,100);
		wg = gs * pg / 100;
	}

	if ( (pg == 0 && pd!=0) || (pg == 100 && pd!=100) ){
		return false;
	}
	return true;
}

int main(){
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A.out","wt",stdout);
	scanf("%d",&T);
	FOR(t,1,T){
		scanf("%d %d %d",&n,&pd,&pg);
		bool possible = false;
		possible = process();
		printf("Case #%d: %s\n",t,possible ? "Possible" : "Broken");
	}
	return 0;
}