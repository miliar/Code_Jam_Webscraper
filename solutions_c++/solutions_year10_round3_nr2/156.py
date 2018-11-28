#include <cstdio>
#include <algorithm>
using namespace std;

int res(int num) {
	int x = 0;
	while (num>0) {
		num--;
		num = (num+1)/2;
		x++;
	}
	return x;
}

int test() {
	long long l,p,c;
	scanf("%lld%lld%lld", &l, &p, &c);
	int a=0,b=0;
	long long g = l;
	while (g*c < p) { g *= c; a++; }
	g = p;
	while (l*c < g) { g = (g+c-1)/c; b++; }
	return min(res(a),res(b));
}

main() {
	int z;
	scanf("%d", &z);
	for (int i=0;i<z;i++) {
		printf("Case #%d: %d\n", i+1, test());
	}
}

