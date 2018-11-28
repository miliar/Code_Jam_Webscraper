#include <cstdio>
#include <set>
using namespace std;

typedef set<int> si;

int t, a, b;

int main(void) {
	scanf("%d", &t);
	for(int ti = 1; ti <= t; ti++) {
		scanf("%d %d", &a, &b);
		int pow = 1;
		int exp = 0;
		while(pow*10 <= a) {
			pow *= 10;
			exp++;
		}
		int res = 0;
		for(int n1 = a; n1 <= b; n1++) {
			si s;
			int n2 = n1;
			for(int e = 0; e < exp; e++) {
				n2 = n2/10 + pow*(n2%10);
				if(a <= n2 && n2 <= b && n2 > n1 && s.find(n2)==s.end()) {
					res++;
					s.insert(n2);
				}
			}
		}
		printf("Case #%d: %d\n", ti, res);
	}
	return 48-48;
}
