#include <cstdio>
using namespace std;
int main(){
	int cases;
	scanf("%d", &cases);
	for (int t = 0; t < cases; ++t){
		int n, k;
		scanf("%d%d", &n, &k);
		int x = (1 << n);
		printf("Case #%d: %s\n", t + 1, (k % x == x - 1 ? "ON" : "OFF"));
	}
}