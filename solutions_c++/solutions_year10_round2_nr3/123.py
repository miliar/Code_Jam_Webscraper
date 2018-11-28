#include <iostream>
#include <cstdio>
#define MOD 100003
#define MAXN 510
using namespace std;
typedef long long lol;
lol npok[MAXN+1][MAXN+1];
lol dynamic[MAXN+1][MAXN+1];
int main() {
    int z;
    scanf("%d", &z);
    npok[0][0] = 1;
    for(int i=1; i<=MAXN; i++) {
	npok[i][0] = 1;
	npok[i][i] = 1;
	for(int j=1; j<=i; j++) {
	    npok[i][j] = (npok[i-1][j] + npok[i-1][j-1]) % MOD;
// 	    cout << npok[i][j] << ' ';
	}
// 	cout << endl;
    }
    for(int i=2; i<=MAXN; i++) { // jaka liczba
// 	cout << i << ": ";
	dynamic[i][1] = 1;
	for(int j=2; j<i; j++) { // ktora w ciagu
	    for(int k=1; k<j; k++) { // ktora w swoim ciagu jest szukana liczba
		dynamic[i][j] += dynamic[j][k] * npok[i-j-1][j-k-1];
		dynamic[i][j] %= MOD;
	    }
// 	    cout << dynamic[i][j] << ' ';
	}
// 	cout << endl;
    }
    for(int i=1; i<=z; i++) {
	lol n;
	scanf("%lld", &n);
	lol sol = 0;
	for(int j=0; j<=n; j++) {
	    sol += dynamic[n][j];
	    sol %= MOD;
	}
	printf("Case #%d: %lld\n", i, sol);
    }
    return 0;
}