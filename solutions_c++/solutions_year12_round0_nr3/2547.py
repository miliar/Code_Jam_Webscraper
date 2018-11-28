#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for(int a = b ; a < c ; ++a )
#define db(x) cerr << #x " == " << x << endl
#define _ << ", " <<
typedef long long ll;

int pot10[10], n;

int cont(int x, int b) {
	int r = 0;
	static int ar[30];
	fr(i,1,n) {
		int y = x/pot10[i] + x%pot10[i]*pot10[n-i];
		if( x < y && y < b ) ar[r++] = y;
	}
	sort(ar,ar+r);
	return unique(ar,ar+r)-ar;
}

int main() {
	pot10[0] = 1;
	fr(i,1,10) pot10[i] = pot10[i-1]*10;
	
	int caso = 1, t,a,b;
	scanf("%d", &t);
	while( t-- ) {
		scanf("%d%d", &a, &b);
		n = 0;
		while( pot10[n] <= a ) n++;
		b++;
		ll r = 0;
		fr(i,a,b) r+= cont(i,b);
		printf("Case #%d: %lld\n", caso++, r);
	}
	
	return 0;
}
