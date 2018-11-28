#include <cstdio>
#include <cstdlib>
using namespace std;

void process() {
	int cx, cy, a;
	scanf("%d %d %d", &cx, &cy, &a);
	for (int x1 = 1; x1 <= cx; x1++)
		for (int y2 = 1; y2 <= cy; y2++)
			for (int x2 = 1; x2 <= cx; x2++)
				if ((x1*y2-a)%x2==0) {
					int y1 = (x1*y2 - a)/x2;
					if (0 <= y1 && y1 <= cy) {
						printf("0 0 %d %d %d %d\n", x1, y1, x2, y2);
						return;
					}
				}
	printf("IMPOSSIBLE\n");
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		process();
	}
}

