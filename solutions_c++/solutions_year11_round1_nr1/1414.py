#include <iostream>

using namespace std;

int main() {
	int T, N, Pd, Pg;
	int tcase = 1;
	
	freopen("freecell.in", "r", stdin);
	freopen("freecell.out", "w", stdout);
	
	scanf("%d", &T);
	for(int i = 0; i < T; ++i)
	{
		bool found = false;
		scanf("%d %d %d", &N, &Pd, &Pg);
		for (int h = 1; h <= N; ++h) {
			if ((h*Pd) % 100 == 0) {
				found = true;
				break;
			}
		}
		if (found) {
			if ((Pg == 100 && Pd != 100) || (Pg == 0 && Pd != 0)) {
				found = false;
			}
		}
		printf("Case #%d: %s\n", tcase++, found ? "Possible" : "Broken");
	}
}