#include <bits/stdc++.h>
using namespace std;

#define db(x) cerr << #x " == " << x << endl
#define _ <<", "<<
#define fr(a,b,c) for( int a = b ; a < c ; ++a )

int caso = 1;

double p[1<<20], q[1<<20];
int n,m;

bool read() {
	scanf("%d%d", &n, &m);
	fr(i,0,n) scanf("%lf", p+i);
	
	q[0] = 0;
	fr(i,0,n) q[i+1] = q[i] + (1-q[i])*(1-p[i]);
	
	double res = 2+m;
	
	fr(i,0,n+1) {
		res = min( (n-i + m-i + 1 + m + 1)*q[i] + (n-i+m-i+1)*(1-q[i]), res);
	}
	
	printf("Case #%d: %.6lf\n", caso++, res);
	
	return true;
}

int main() {
	int t = -1;
	scanf("%d", &t);
	while( t-- && read() );
	return 0;
}
