#include<stdio.h>
#include<string.h>

int best0[31];
int best1[31];

int solve() {
	int N,S,P,ret=0,x;
	scanf("%d%d%d",&N,&S,&P);
	while(N--) {
		scanf("%d",&x);
		if(best0[x]>=P)ret++;
		else if(best1[x]>=P&&S>0){ret++;S--;}
	}
	return ret;
}

void maz(int &a,int b) {
	if(b>a)a=b;
}

void build() {
	int a,b,c,s;
	memset(best0,0xff,sizeof(best0));
	memset(best1,0xff,sizeof(best1));
	for(a=0;a<=10;a++) {
		for(b=a;b<=10&&b-a<=2;b++) {
			for(c=b;c<=10&&c-a<=2;c++) {
				s=a+b+c;
				if(c!=a+2)maz(best0[s],c);
				else maz(best1[s],c);
			}
		}
	}
}

int main() {
	int T,S;
	build();
	scanf("%d",&T);
	for(S=1;S<=T;S++)printf("Case #%d: %d\n",S,solve());
	return 0;
}
