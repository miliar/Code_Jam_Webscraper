#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define forsn(i,s,n) for(int i=(s);i<(n);i++)
#define dforsn(i,s,n) for(int i=(n)-1;i>=(s);i--)
#define forn(i,n) forsn(i,0,(n))
#define dforn(i,n) dforsn(i,0,(n))

typedef long long int tint;

unsigned long long mask(int bits) {
	unsigned long long m = -1;
	return m >> (64 - bits);
}

int main() {
	tint T;
	cin >> T;
	forn(icase,T) {
		tint N, K;
		cin >> N >> K;
		cout << "Case #" << (icase+1) << ": " << ( ((K & mask(N)) == mask(N) ) ?"ON":"OFF") << endl;
	}
	return 0;
}
