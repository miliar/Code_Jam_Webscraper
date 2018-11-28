#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	int tt;
	cin >> tt;
	for (int t = 1; t <= tt; t++) {
		int n, D;
		cin >> n;
		int d[10000], l[10000];
		int T[10000];
		for (int i = 0; i < n; i++)
			cin >> d[i] >> l[i];
		cin >> D;
		memset(T, 255, sizeof(T));
		int oo = T[0];
		T[0] = d[0];
		bool sol = false;
		for (int i = 0; i < n; i++)
			if (T[i] != oo) {
				if (T[i] + d[i] >= D) {
					sol = true;
					break;
				}
				for (int j = i + 1; j < n && d[j] - d[i] <= T[i]; j++) {
					if (T[j] < min(d[j] - d[i], l[j]))
						T[j] = min(d[j] - d[i], l[j]);
				}
			}
		printf("Case #%d: ", t);
		if (sol)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
