#include <stdio.h>
#include <memory.h>
#include <cstring>
#include <algorithm>
using namespace std;

int work(int a, int b) {
    int m, k, t;
	int ans = 0;

    for (int i = a; i < b; i++) {
        m = i;
        t = 1;
		while(m >= 10) {
			t *= 10;
			m /= 10;
		}
		k = m = i;
        while(m > 10) {
			k = k / 10 + t * (m % 10);
			if (k <= b && k > i && m % 10 != 0)       ans++;
   m /= 10;			
		}
	}
	return ans;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int cases;
    int a, b;
    
    scanf("%d", &cases);
    
	for (int p = 1; p <= cases; p++) {
        scanf("%d%d", &a, &b);
        printf("Case #%d: %d\n", p, work(a, b));
	}
	return 0;
}
	
