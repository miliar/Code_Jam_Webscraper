#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int main() {
	int T;
	scanf("%d", &T);
	getchar(); // \n

	for (int cases = 1; cases <= T; cases++) {
		int num;
		vector <int> N;
		char c;

		N.push_back(0);
		while ((c = getchar()) != '\n' && c != EOF)
			N.push_back(c-'0');

		int size = N.size();
		int i;

		for (i = size-2; i >= 0; i--) {
			int minMax = i+1;
			for (int j = i+2; j < size; j++) {
				if (N[j] > N[i] && N[j] <= N[minMax])
					minMax = j;
			}

			if (N[minMax] > N[i]) {
				int aux = N[i];
				N[i] = N[minMax];
				N[minMax] = aux;
				break;
			}
		}

		printf("Case #%d: ", cases);
		bool leftZ = true;
		for (int j = 0; j <= i; j++) {
			if (leftZ && N[j] == 0) {
				N[j] = -1;
				continue;
			}
			leftZ = false;
			printf("%d", N[j]);
			N[j] = -1;
		}

		sort(N.begin(), N.end());

		for (int j = 0; j < size; j++) {
			if (N[j] == -1) continue;
			printf("%d", N[j]);
		}
		printf("\n");
	}

	return 0;
}
