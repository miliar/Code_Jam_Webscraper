#include<stdio.h>
#include<math.h>
#include<algorithm>

using namespace std;

char num[1000];

int W,N,M,G;
double U[1000][2], D[1000][2];

int f(int s, long long n) {
	if(!num[s]) {
		long long x = sqrt(n)+0.5;
		if( x*x == n ) return 1;
		return 0;
	}
	if(num[s] == '?') {
		num[s] = '0';
		if( f(s+1,(n<<1)) ) return 1;
		num[s] = '1';
		if( f(s+1,(n<<1)|1) ) return 1;
		num[s] = '?';
	} else {
		return f(s+1,(n<<1)|(num[s]=='1'));
	}
	return 0;
}

void solve(int t) {
	scanf("%s",num);
	f(0,0);
	printf("Case #%d: %s\n",t,num);
}

int main() {
	int t,T;
	double sec, tot;
	scanf("%d",&T);
	for(t=1;t<=T;t++) solve(t);
	return 0;
}
