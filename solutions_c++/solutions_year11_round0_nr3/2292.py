#include <iostream>

using namespace std;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d\n", &tk);

    for (int tc = 1; tc <= tk; ++tc) {
    	printf("Case #%d: ", tc);
    	int n;
    	int x = 0, m = 9999999, s = 0;

    	scanf("%d", &n);
    	while (n --> 0) {
    		int y;
    		scanf("%d", &y);

    		x ^= y;
    		m = min(m, y);
    		s += y;
    	}
    	if (x == 0) {
    		printf("%d\n", s - m);
    	} else {
    		puts("NO");
    	}
    }
	
	return 0;
}