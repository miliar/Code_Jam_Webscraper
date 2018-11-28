#include <string>
#include <string.h>
#include <vector>
#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
	int T;

	scanf("%d", &T);

	for (int C = 1; C <= T; C++) {
		int N, S, p;
		int answer = 0;

		scanf("%d %d %d", &N, &S, &p);

		vector <int> t(N+100);

		for (int i = 0; i < N; i++)
			scanf("%d", &t[i]);

		for (int i = 0; i < N; i++) {
			if (t[i] <= 1) {
				if (t[i] == 0 && p == 0 || t[i] == 1 && p <= 1)
					answer++;
			}
			else {
				int max = ceil((double) t[i] / 3);

				if (max >= p) {
					answer++;
				}
				else if (S >= 1 && t[i]%3 != 1 && max+1 == p) {
					answer++;
					S--;
				}
			}
		}

		printf("Case #%d: %d\n", C, answer);
	}

	return 0;
}

