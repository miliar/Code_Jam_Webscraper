#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	FILE* in = fopen("B-large.in", "r");
	FILE* out = fopen("B-large.out", "w");
	int t;

	fscanf(in, "%d", &t);
	for(int i = 0; i < t; ++i) {
		int n, s, p, res = 0;
		fscanf(in, "%d%d%d", &n, &s, &p);

		for(int j = 0; j < n; ++j) {
			int score;
			fscanf(in, "%d", &score);
			int avg = score / 3;
			int r = score % 3;

			if(r == 0) {
				if(avg >= p) {
					++res;
					continue;
				}
				if(avg + 1 >= p && s > 0 && avg > 0) {
					--s;
					++res;
				}
			}
			else if(r == 1) {
				if(avg + 1 >= p) {
					++res;
					continue;
				}
			}
			else {
				if(avg + 1 >= p) {
					++res;
					continue;
				}
				if(avg + 2 >= p && s > 0) {
						--s;
						++res;
				}
			}
		}

		fprintf(out, "Case #%d: %d\n", i + 1, res);
	}

	return 0;
}
