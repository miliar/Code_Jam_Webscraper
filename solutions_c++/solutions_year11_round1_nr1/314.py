#include <cstdio>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[]) {
    int T;
	scanf("%d", &T);
	
	for (int i = 1; i <= T; i++) {
		int N, D, G;
		scanf("%d%d%d", &N, &D, &G);
		int FACD = 100;
		if (G == 100 && D != 100) {
			printf("Case #%d: Broken\n", i);
			continue;
		}
		if (G == 0 && D != 0) {
			printf("Case #%d: Broken\n", i);
			continue;
		}
		if (D % 4 == 0) FACD /= 4;
		else if (D % 2 == 0) FACD /= 2;
		if (D % 25 == 0) FACD /= 25;
		else if (D % 5 == 0) FACD /= 5;
		if (FACD > N) {
			printf("Case #%d: Broken\n", i);
			continue;
		} else {
			printf("Case #%d: Possible\n", i);
		}
	}

    return 0;
}
