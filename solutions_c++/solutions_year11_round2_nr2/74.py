#include<cstdio>
#include<algorithm>
using namespace std;

#define NMAX 1000000
int n,D,x[NMAX];

double abs(double x) {
	return x>=0?x:-x;
}

bool test(double t) {
	int i; double prev=-1e100;
	for(i=0;i<n;i++) {
		double bound=prev+D;
		if(x[i]>=bound) {
			prev=max(bound,x[i]-t);
		} else {
			if(x[i]+t<bound)return false;
			prev=bound;
		}
	}
	return true;
}

double fix(double x) {
	long long i=x;
	double x2=i+0.5,x3=i+1,x4=i+1.5,x5=i-0.5,x6=i-1,x7=i-1.5;
	double o=i;
	if(abs(x2-x)<abs(o-x))o=x2;
	if(abs(x3-x)<abs(o-x))o=x3;
	if(abs(x4-x)<abs(o-x))o=x4;
	if(abs(x5-x)<abs(o-x))o=x5;
	if(abs(x6-x)<abs(o-x))o=x6;
	if(abs(x7-x)<abs(o-x))o=x7;
fprintf(stderr,"%.8f vs %.8f\n",x,o);
	return o;
}

double solve() {
	double ret,L,R,M;
	R=1;
	while(!test(R))R*=2;
	L=0;
	while(R-L>1e-4) {
		M=(L+R)/2;
		if(test(M))R=M;
		else L=M;
	}
	ret=(L+R)/2;
	return fix(ret);
}

void input() {
	int m,x,y;
	n=0;
	scanf("%d%d",&m,&D);
	while(m--) {
		scanf("%d%d",&x,&y);
		while(y--)::x[n++]=x;
	}
}

int main() {
	int T,S;
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		input();
		printf("Case #%d: %.8f\n",S,solve());
	}
	return 0;
}
