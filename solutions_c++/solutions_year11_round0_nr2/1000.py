
#include <cstdio>

int t, nelement[26], noppose[26];
char element[100], combine[26][26], oppose[26][28];

int main() {
	FILE * fin = fopen("magicka.in", "r"), * fout = fopen("magicka.out", "w");
	int i, d, n, j, k;
	char a, b, c;
	fscanf(fin, "%d", &t);
	for (i = 0; i < t; ++i) {
		for (j = 0; j < 26; ++j) {
			noppose[j] = 0;
			for (k = 0; k < 26; ++k) {
				combine[j][k] = 0;
			}
		}
		fscanf(fin, "%d", &d);
		for (j = 0; j < d; ++j) {
			fscanf(fin, " %c%c%c", &a, &b, &c);
			combine[a - 'A'][b - 'A'] = c;
			combine[b - 'A'][a - 'A'] = c;
		}
		fscanf(fin, "%d", &d);
		for (j = 0; j < d; ++j) {
			fscanf(fin, " %c%c", &a, &b);
			oppose[a - 'A'][noppose[a - 'A']] = b;
			++noppose[a - 'A'];
			oppose[b - 'A'][noppose[b - 'A']] = a;
			++noppose[b - 'A'];
		}
		fscanf(fin, "%d ", &n);
		j = 0;
		d = -1;
		while (j < n) {
			for (k = 0; k < 26; ++k) {
				nelement[k] = 0;
			}
			fscanf(fin, "%c", element);
			++j;
			++nelement[element[0] - 'A'];
			d = 0;
			while (j < n) {
				fscanf(fin, "%c", &c);
				++j;
				if (combine[c - 'A'][element[d] - 'A']) {
					--nelement[element[d] - 'A'];
					element[d] = combine[c - 'A'][element[d] - 'A'];
					++nelement[element[d] - 'A'];
				} else {
					for (k = 0; k < noppose[c - 'A']; ++k) {
						if (nelement[oppose[c - 'A'][k] - 'A'] > 0) {
							d = -1;
							break;
						}
					}
					if (k < noppose[c - 'A']) {
						break;
					}
					++d;
					element[d] = c;
					++nelement[element[d] - 'A'];
				}
			}
		}
		fprintf(fout, "Case #%d: [", i + 1);
		if (d != -1) {
			fprintf(fout, "%c", element[0]);
		}
		for (j = 1; j <= d; ++j) {
			fprintf(fout, ", %c", element[j]);
		}
		fprintf(fout, "]\n");
	}
	return 0;
}
