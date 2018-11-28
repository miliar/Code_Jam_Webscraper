#include <cstdio>
#include <algorithm>
#include <vector>


using namespace std;


int main() {
	FILE *fin = fopen("C-small-attempt1.in", "rt");
	FILE *fout = fopen("out.txt", "wt");

	int T;
	fscanf(fin, "%d", &T);
	
	for (int t = 1; t <= T; ++t) {
		int n, l, h;
		int A[10000];
		fscanf(fin, "%d %d %d", &n, &l, &h);

		for (int i = 0; i < n; ++i) fscanf(fin, "%d", &A[i]);

		int II = l;
		bool ok;
		for (; II <= h; ++II) {
			ok = true;
			int mod1 = 0;
			int mod2 = 0;
			for (int k = 0; k < n; ++k) {
				mod1 = A[k] % II;
				mod2 = II % A[k];
				if (mod1 != 0 && mod2 != 0) {
					ok = false;
					break;
				}
			}
			if (ok) {
				fprintf(fout, "Case #%d: %d\n", t, II);
				break;
			}
		}
		if (ok == false) fprintf(fout, "Case #%d: NO\n", t);
	}
	fclose(fout);
	return 0;
}