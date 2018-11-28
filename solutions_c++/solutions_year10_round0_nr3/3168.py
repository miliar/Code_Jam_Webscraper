
#include <cstdio>
#include <list>
using namespace std;

int numgroups[1010];
int numpeople[1010];

int N;
int groups[1010];

int k;
int R;

void preprocess() {
	for (int i = 0; i < N; i++) {
		int length = 0;
		int sum = 0;
		int index = i;
		while (sum + groups[index] <= k) {
			sum += groups[index];
			index = (index+1) % N;
			length++;
			if (index == i) break;
		}
		numgroups[i] = length;
		numpeople[i] = sum;
	}
}

int main() {
	
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		
		scanf("%d %d %d", &R, &k, &N);
		for (int j = 0; j < N; j++) scanf("%d", &groups[j]);

		preprocess();

		// Loop R times
		int profit = 0;
		int index = 0;
		for (int j = 0; j < R; j++) {
			profit += numpeople[index];
			index += numgroups[index];
			index = index % N;
		}

		// Print output
		printf("Case #%d: %d\n", i, profit);

	}

}

