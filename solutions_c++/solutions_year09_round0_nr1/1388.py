#include <cstdio>

const int L = 60;
const int D = 5001;

char dictionary[D][L];
char pattern[L*(L+2)];

int main(void) {
	int l,d,n;

	scanf("%d%d%d",&l,&d,&n);
	for (int id=0; id<d; ++id) {
		scanf("%s",dictionary[id]);
	}
	for (int in=1; in<=n; ++in) {
		int res = 0;
		scanf("%s",pattern);

		for (int id=0; id<d; ++id) {
			bool ok = true;
			for (int i=0,j=0; pattern[j]; ++i,++j) {
				if (pattern[j] == '(') {
					int nok = false;
					for (++j; pattern[j]!=')'; ++j) {
						if (pattern[j] == dictionary[id][i]) nok = true;
					}
					if (!nok) {
						ok = false;
						break;
					}
				} else {
					if (pattern[j] != dictionary[id][i]) {
					       	ok = false;
						break;
					}
				}
			}
			if (ok) ++res;
		}
		printf("Case #%d: %d\n",in,res);
	}
	return 0;
}
