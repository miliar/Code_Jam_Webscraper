#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for(int a = b ; a < c ; ++a )
#define db(x) cerr << #x " == " << x << endl
#define _ << ", " <<
typedef long long ll;

int caso = 1;
int val[200];

int maior[100], maior2[100];

void read() {
	int n,s,p;
	scanf("%d%d%d", &n, &s, &p);
	fr(i,0,n) scanf("%d", val+i);
	
	sort(val,val+n);
	reverse(val,val+n);
	int r = 0;
	fr(i,0,n) {
		if( maior[ val[i] ] >= p ) r++;
		else { // a a a+2 = v
			if( maior2[ val[i] ] >= p && s ) r++, s--;
		}
	}
	printf("Case #%d: %d\n", caso++, r);
}

int main() {

	memset(maior,0,sizeof maior);
	memset(maior2,0,sizeof maior2);
	fr(i,0,11) fr(j,0,11) fr(k,0,11) {
		if( abs(i-j) <= 1 && abs(i-k) <= 1 && abs(j-k) <= 1 ) {
			maior[i+j+k] = max(maior[i+j+k], max(i,max(j,k)));
		}
		if( abs(i-j) <= 2 && abs(i-k) <= 2 && abs(j-k) <= 2 ) {
			maior2[i+j+k] = max(maior2[i+j+k], max(i,max(j,k)));
		}
	}

	int t = -1;
	scanf("%d", &t);
	while( t-- ) read();
	
	return 0;
}
