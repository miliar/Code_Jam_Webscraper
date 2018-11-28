#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int euclides(int a, int b) {
	if (a < b)
		euclides(b, a);
	if (b == 0)
		return a;
	return euclides(b, a%b);
}


int main() {
	int T;
	scanf("%d", &T);

	for (int caso = 1; caso <= T; caso++) {
		printf("Case #%d: ", caso);


		int N, L, H;
		scanf("%d %d %d", &N, &L, &H);

		vector <int> note(N);
		for (int i = 0; i < N; i++)
			scanf("%d", &note[i]);

		if (L == 1) {
			printf("1\n");
			continue;
		}

		/*int gdc = note[0];
		int lcm = 1;
		for (int i = 0; i < N; i++) {
			gdc = euclides(lcm, note[i]);
			lcm = lcm * note[i] / gdc;
		}

		int aux = lcm;
		while (lcm < L)
			lcm += aux;

		if (lcm > H)
			printf("NO\n");
		else
			printf("%d\n", lcm);*/

		bool OK;
		for (int i = L; i <= H; i++) {
			OK = true;
			for (int j = 0; OK && j < N; j++) {
				if (i % note[j] != 0 && note[j] % i != 0)
					OK = false;
			}

			if (OK) {
				printf("%d\n", i);
				break;
			}
		}

		if (!OK)
			printf("NO\n");
	}

	return 0;
}
