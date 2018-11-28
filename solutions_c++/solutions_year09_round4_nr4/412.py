#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;
const int MAXN =3;
#define REP(i,n) for(int i=0;i<(n);i++)

int x[MAXN];
int y[MAXN];
int r[MAXN];
int n;

void read(){
	scanf("%d",&n);
	REP(i,n){
		scanf("%d%d%d",&x[i],&y[i],&r[i]);
	}
	REP(i,3-n){
		x[i+n] = x[n-1];
		y[i+n] = y[n-1];
		r[i+n] = r[n-1];
	}
}

int sq(int x){
	return x*x;
}

double dist(int i1,int i2){
	return sqrtl(sq(x[i1]-x[i2])+sq(y[i1]-y[i2]));
}

double check(int i1,int i2,int i3){
	double res = max(double(r[i3]),(dist(i1,i2)+r[i1]+r[i2])/2);
	return res;
}

void compute(int cas){
	double res = min(check(0,1,2),min(check(0,2,1),check(2,1,0)));
	printf("Case #%d: %lf\n",cas+1,res);
}

int main(){
	int t;
	scanf("%d",&t);
	REP(i,t){
		read();
		compute(i);
	}
	return 0;
}


