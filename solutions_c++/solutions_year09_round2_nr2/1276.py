#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

typedef long long ll;

ll next( ll n ) {
	ll m = n;
	int a[10] = {0};
	while(m>0) { a[m%10]++; m /= 10; }
	for(ll i=n+1;;++i) {
		m = i;
		int b[10] = {0};
		while(m>0) { b[m%10]++; m /= 10; }
		int j;
		for(j=1;j<=9;++j) if(a[j]!=b[j]) break;
		if(j>9) return i;
	}
	return -1;
}

int main() {
	int tn;
	cin >> tn;
	for(int cc=1;cc<=tn;++cc) {
		ll n;
		cin >> n;
		printf("Case #%d: %I64d\n", cc, next(n));
	}
}

