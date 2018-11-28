#include <cstdio>
#include <cstring>
#include <vector>
#include <cassert>

int main() {
	char text[2000];

	int L, D, N;
	scanf("%d%d%d", &L, &D, &N);

	/* wczytaj słownik */
	std::vector<const char *> dict;
	for(int i=0; i<D; i++) {
		scanf("%s", text);
		assert((int)strlen(text) == L);
		dict.push_back(strdup(text));
	}

	/* dla każdego wzorca/przypadku testowego */
	for(int c=0; c<N; c++) {
		std::vector<int> mask;

		/* wczytaj maskę */
		scanf("%s", text);
		const char *z = text;
		while(*z) {
			int msk = 0;
			if(*z == '(') {
				z++;
				while(*z != ')' && *z) {
					msk |= 1L << (*z - 'a');
					z++;
				}
				if(*z == ')')
					z++;
			} else {
				msk |= 1L << (*z - 'a');
				z++;
			}
			mask.push_back(msk);
		}
		assert((int)mask.size() == L);

		/* sprawdź liczbę dopasowań */
		int num = 0;
		for(int d=0; d<(int)dict.size(); d++) {
			const char *z = dict[d];
			bool ok = true;
			for(int i=0; i<L; i++) {
				if(! (mask[i] & (1L<<(z[i]-'a'))) ) {
					ok = false;
					break;
				}
			}
			if(ok)
				num++;
		}

		printf("Case #%d: %d\n", c+1, num);
	}

	return 0;
}

