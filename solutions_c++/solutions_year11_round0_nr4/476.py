#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>

FILE *in, *out;
int T, N;
std::vector<int> a, b;

int main() {
	in = fopen("goroin.txt", "r"); out = fopen("goroout.txt", "w");
	fscanf(in, "%d", &T);
	for (int t = 1; t <= T; ++t) {
		fscanf(in, "%d", &N);
		a.resize(N);
		for (int i = 0; i < N; ++i) fscanf(in, "%d", &a[i]);
		b = a;
		int n = 0;
		std::sort(b.begin(), b.end());
		for (int i = 0; i < b.size(); ++i)
			if (a[i] == b[i]) n++;
		fprintf(out, "Case #%d: %d\n", t, b.size()-n);
	}
}
