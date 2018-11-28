#include <cstdio>
#include <cstring>

#define MODULO 100003

typedef long long llong;

llong modPow(llong a, llong x, llong p) {
    //calculates a^x mod p in logarithmic time.
    llong res = 1;
    while(x > 0) {
        if( x % 2 != 0) {
            res = (res * a) % p;
        }
        a = (a * a) % p;
        x /= 2;
    }
    return res;
}

llong modInverse(llong a, llong p) {
    //calculates the modular multiplicative of a mod m.
    //(assuming p is prime).
    return modPow(a, p-2, p);
}

llong modBinomial(llong n, llong k, llong p) {
	if (n < k)
		return 0;
// calculates C(n,k) mod p (assuming p is prime).
	if (n - k < k)
		k = n - k;

    llong numerator = 1; // n * (n-1) * ... * (n-k+1)
    for (int i=0; i<k; i++) {
        numerator = (numerator * (n-i) ) % p;
    }
    
    llong denominator = 1; // k!
    for (int i=1; i<=k; i++) {
        denominator = (denominator * i) % p;
    }
    
    // numerator / denominator mod p.
    return ( numerator* modInverse(denominator,p) ) % p;
}

int main() {
	
	llong C[501][501];
	memset(C, 0, sizeof(C));
	
	for (int n = 2; n <= 500; n++) {
		
		C[n][n - 1] = C[n][1] = 1;
		
		for (int i = 2; i < n - 1; i++) {
			
			for (int j = 1; j < n; j++) {
				C[n][i] += C[i][j] * modBinomial(n - i - 1, i - j - 1, MODULO);
				C[n][i] %= MODULO;
			}
			
		}
	}
	
	/*for (int i = 2; i <= 6; i++) {
		for (int j = 1; j <= 6; j++)
			printf(" %d", C[i][j]);
		printf("\n");
	}*/
	
	int n, cases;
	
	scanf("%d", &cases);
	for (int test = 1; test <= cases; test++) {
		scanf("%d", &n);
		
		int total = 0;
		for (int i = 0; i < n; i++)
			total += (int) C[n][i];
		
		printf("Case #%d: %d\n", test, total % MODULO);
	}
	
	return 0;
	
}
