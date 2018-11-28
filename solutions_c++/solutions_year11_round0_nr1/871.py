#include <stdio.h>

int t, T, n, c, i;
char s[2];
int Oi[100], Bi[100];
int Oc[100], Bc[100];
int nOi, nBi, iOi, iBi;
int Opos, Bpos;
int cnt;

int main() {
	scanf("%d", &t);
	for (int T = 1; T <= t; T++) {
		printf("Case #%d: ", T);
		scanf("%d", &n);
		nOi = nBi = i = 0;
		while (n--) {
			scanf("%s%d", s, &c);
			if (s[0] == 'O') {
				Oc[nOi] = i++;
				Oi[nOi++] = c;
			} else {
				Bc[nBi] = i++;
				Bi[nBi++] = c;
			}
		}
		Opos = Bpos = 1;
		iOi = iBi = cnt = 0;
		
		for (;iOi < nOi || iBi < nBi;) {
			bool pushed = false;
			if (iOi < nOi) {
				if (Opos < Oi[iOi]) Opos++;
				else if (Opos > Oi[iOi]) Opos--;
				else {
					if (iBi < nBi) {
	 					if (Oc[iOi] < Bc[iBi]) {iOi++; pushed = true;}
					} else {iOi++;pushed = true;}
				}
			}
			if (iBi < nBi) {
				if (Bpos < Bi[iBi]) Bpos++;
				else if (Bpos > Bi[iBi]) Bpos--;
				else if (!pushed) {
					if (iOi < nOi) {
	 					if (Bc[iBi] < Oc[iOi]) iBi++;
					} else iBi++;
				}
			}
			cnt++;
		}

		printf("%d\n", cnt);
	}
	return 0;
}
