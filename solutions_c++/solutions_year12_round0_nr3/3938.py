#include <stdio.h>
#include <set>

using namespace std;

#define MAX_N 2000010

int dim[MAX_N];

int concat(int x, int y) {
	return x * dim[y] + y;
}

int main() {

	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);

	for (int i = 0; i < MAX_N; i++)
		for (int j = 1;; j *= 10)
			if (j > i) {
            	dim[i] = j;
				break;
			}

	int T;
	scanf("%d", &T);

	for (int i = 1; i <= T; i++) {
		int a, b, sol = 0;
		scanf("%d %d", &a, &b);

		for (int j = a; j <= b; j++) {
			set <int> s;
    		for (int p10 = 10; p10 <= j; p10 *= 10) {
            	int new_number = concat(j % p10, j / p10);
				if (j < new_number && new_number <= b)
					s.insert(new_number);
			}
			sol += s.size();
		}

		printf("Case #%d: %d\n", i, sol);
	}

	return 0;
}
