#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

#define input "B-small-attempt6.in"
#define output "B.out"
using namespace std;

int gcd(int a, int b)
{
	if (b == 0) return a;
	else return gcd(b, a % b);
}

int main()
{
	int i, j, c, n;

	FILE *fin = fopen(input, "r");
	FILE *fout = fopen(output, "w");

	fscanf(fin, "%d", &c);
	for (i = 0; i < c; i++) {
		fscanf(fin, "%d", &n);

		vector<int> t(n);

		for (j = 0; j < n; j++) fscanf(fin, "%d", &t[j]);
		sort(t.begin(), t.end());

		int g = 0, ans = 0;
		if (n == 2) {
			g = t[1] - t[0];
		}
		else {
			g = gcd(t[n - 1] - t[0], t[n - 2] - t[0]);
		}

		if (t[0] % g == 0) {
			ans = 0;
		} else {	
			ans = g - (t[0] % g);
			for (j = 0; j < n; j++) {
				if (g - (t[j] % g) < ans) {
					ans = g - (t[j] % g);
				}
			}
		}

		fprintf(fout, "Case #%d: %d\n", i + 1, ans);
	}

	fclose(fout);
	fclose(fin);

	return 0;
}