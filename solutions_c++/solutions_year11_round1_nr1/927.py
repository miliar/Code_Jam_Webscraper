#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

typedef unsigned long long u64;

inline int gcd( int a, int b ){
    while (b != 0){
		a %= b;
        swap(a, b);
    }
    return a;
}

int main(){
	int T;
	cin >> T;
	for( int t = 1; t <= T; ++t ){
		u64 N;
		int Pd, Pg;
		cin >> N >> Pd >> Pg;
		
		printf("Case #%d: ", t);
		if ((100/gcd(100,Pd) <= N) && !((Pg == 100 && Pd < 100) || (Pg == 0 && Pd > 0))) {
			printf("Possible\n");
		}
		else {
			printf("Broken\n");
		}
	}
}
