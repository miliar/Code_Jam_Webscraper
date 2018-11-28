#include <iostream> 
#include <vector> 
#include <cstdio> 
#include <cstring> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <string> 
#include <sstream> 
#include <ctime> 
#include <cmath> 

using namespace std; 

int T, primes[1000005];

int isprime(int b) {
	if (primes[b] != -1) return primes[b];
	for (int i = 2; i*i <= b; i++) {
		if (b % i == 0) return (primes[b] = 0);
	}
	return (primes[b] = 1);
}

int main() { 
	memset(primes, -1, sizeof primes);
	
	FILE *fin = fopen("test.txt", "r");  
	FILE *fout = fopen("testans.txt", "w");
	
	fscanf(fin, "%d", &T);
	
	for (int z = 1; z <= T; z++) {
		long long N;
		fscanf(fin, "%lld", &N);
		int ans = 1;
		if (N == 1) ans = 0;
		for (int i = 2; (long long)i*i <= N; i++) {
			if (!isprime(i)) continue;
			long long k = (long long)i;
			while (k*i <= N) {k *= i; ans++;}
		}
		fprintf(fout, "Case #%d: %d\n", z, ans);
		//printf("Case #%d: %d\n", z, ans);
	}
	
	
	
	
	//cin.get();
	
    return 0;
}

