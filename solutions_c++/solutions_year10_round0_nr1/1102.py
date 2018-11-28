#include <cstdio>

using namespace std;

void solve() {
	long long n, k;
	scanf("%lld %lld", &n, &k);
	long long ind=1;
	bool g=true;
	for(int i = 0;i<n;i++) {
		if((k&ind)==0) g=false;
		ind<<=1;
	}
	if(g) printf("ON\n");
	else printf("OFF\n");
}

int main() {
	int z;
	scanf("%d", &z);
	for(int i = 1;i<=z;i++) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
