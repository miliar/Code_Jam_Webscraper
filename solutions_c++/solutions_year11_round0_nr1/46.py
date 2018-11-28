#include<cstdio>

#define NMAX 100

int n,p[NMAX];

int abs(int x) {
	return x>=0?x:-x;
}

int max(int a,int b) {
	return a>=b?a:b;
}

int solve() {
	int op=1,ot=0,bp=1,bt=0;
	int i,p;
	for(i=0;i<n;i++) {
		p=(::p[i]>>1);
		if(!(::p[i]&1)) {
			// O
			ot=max(ot+abs(op-p),bt)+1;
			op=p;
		} else {
			// B
			bt=max(bt+abs(bp-p),ot)+1;
			bp=p;
		}
	}
	return max(ot,bt);
}

void input() {
	int i,p; char c;
	scanf("%d",&n);
	for(i=0;i<n;i++) {
		scanf(" %c%d",&c,&p);
		::p[i]=((p<<1)|(c=='O'?0:1));
	}
}

int main() {
	int T,i;
	scanf("%d",&T);
	for(i=1;i<=T;i++) {
		input();
		printf("Case #%d: %d\n",i,solve());
	}
	return 0;
}
