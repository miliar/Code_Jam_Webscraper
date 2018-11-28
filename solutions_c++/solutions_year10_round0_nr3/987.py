#include <stdio.h>
#include <string.h>
#include <algorithm>

const int SIZE = 1024;

typedef long long int64;

int t, c, n;
int arr[2*SIZE];
int s;

int next[SIZE];
int inc[SIZE];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d%d", &t, &c, &n);
		for (int i = 0; i<n; i++) {
			scanf("%d", arr+i);
			arr[i+n] = arr[i];
		}

		s = 0;
		for (int i = 0; i<n; i++) s += arr[i];

		for (int i = 0; i<n; i++) {
			if (c >= s) {
				inc[i] = s;
				next[i] = i;
				continue;
			}

			int ost = c;
			int j;
			for (j = i; ost>=arr[j]; j++) ost -= arr[j];
			next[i] = j % n;
			inc[i] = c - ost;
		}
		
		int64 money = 0;
		int curr = 0;
		for (int i = 0; i<t; i++) {
			money += inc[curr];
			curr = next[curr];
		}

		printf("Case #%d: %I64d\n", tt, money);
	}
	return 0;
}
