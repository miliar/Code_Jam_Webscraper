#include <iostream>

using namespace std;


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=1; tt<=ts; ++tt) {
		int n, k;
		scanf ("%d%d", &n, &k);
		n = (1 << n) - 1;
		printf ("Case #%d: %s\n", tt, (k&n)==n ? "ON" : "OFF");
	}

}

