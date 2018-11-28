#include<assert.h>
#include<stdio.h>
typedef double real;

const int AMAX=99999;

int A,B; real p[AMAX];

real solve() {
	int i; real ans=B+2,mul=1,tmp;
	for(i=0;;) {
		tmp=A+B+1-2*i+(1-mul)*(B+1);
		if(tmp<ans)ans=tmp;
		if(i==A)break;
		mul*=p[i++];
	}
	return ans;
}

void input() {
	scanf("%d%d",&A,&B);
	assert(1<=A&&A<B&&A<=AMAX);
	for(int i=0;i<A;i++)scanf("%lf",p+i);
}

int main() {
	int T,S;
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		input();
		printf("Case #%d: %.9f\n",S,solve());
	}
	return 0;
}
