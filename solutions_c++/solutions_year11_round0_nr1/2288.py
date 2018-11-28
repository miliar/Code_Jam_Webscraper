#include <iostream>
#include <vector>

using namespace std;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d\n", &tk);

    for (int tc = 1; tc <= tk; ++tc) {
    	int p1 = 1, t1 = 0;
    	int p2 = 1, t2 = 0;
		
		int n;
		cin >> n;

		while (n --> 0) {
			char c;
			int x;

			cin >> c >> x;

			if (c == 'O') {
				t1 = max(t1 + 1 + abs(p1 - x), t2 + 1);
				p1 = x;
			} else {
				t2 = max(t2 + 1 + abs(p2 - x), t1 + 1);
				p2 = x;
			}
		}


    	printf("Case #%d: %d\n", tc, max(t1, t2));
    }
	
	return 0;
}