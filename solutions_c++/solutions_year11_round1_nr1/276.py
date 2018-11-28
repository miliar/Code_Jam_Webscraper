#include <cstdio>
#include <string>
#include <map>
#include <vector>
#include <cmath>
using namespace std;

int gcd(int a, int b) {
	while(b) {
		a = a%b;
		swap(a, b);
	}
	return a;
}

bool func(int N, int PD, int PG) {
	int UD = 100 / gcd(100, PD);
	if(N<UD) {
		return false;
	}
	if(PD!=100 && PG==100 || PD!=0 && PG==0) {
		return false;
	}
	return true;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t=0; t<T; ++t) {
		long long N;
		int PD, PG;
		scanf("%lld%d%d", &N, &PD, &PG);
		printf("Case #%d: %s\n", t+1, func(N<1000 ? N : 1000, PD, PG) ? "Possible" : "Broken");
	}
	return 0;
}
