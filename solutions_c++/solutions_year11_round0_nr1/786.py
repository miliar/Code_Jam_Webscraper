#include <cstdio>

bool orange[105];
int button[105];
int bpos, opos, t, index, bnext, onext, n;

inline void make_o_next() {
	for(int i = index; i < n; i++)
		if(orange[i]) {
			onext = i;
			return;
		}
	onext = -1;
}

inline void make_b_next() {
	for(int i = index; i < n; i++)
		if(!orange[i]) {
			bnext = i;
			return;
		}
	bnext = -1;
}

inline int abs(int a) {
	return a < 0 ? -a : a;
}

int main() {
	int ncases;
	scanf("%d", &ncases);
	for(int casenum = 1; casenum <= ncases; casenum++) {
		scanf("%d", &n);
		for(int i = 0; i < n; i++) {
			char c;
			do { c = fgetc(stdin); } while (c != 'O' && c != 'B');
			orange[i] = (c == 'O');
			scanf("%d", &button[i]);
		}
		bpos = 1; opos = 1; t = 0; index = 0;
		make_o_next();
		make_b_next();
		while(index < n) {
			if(orange[index] && opos == button[index]) {
				index++;
				t++;
				make_o_next();
				if(bnext != -1) {
					if(button[bnext] < bpos)
						bpos--;
					else if(button[bnext] > bpos)
						bpos++;
				}
			}
			else if(!orange[index] && bpos == button[index]) {
				index++;
				t++;
				make_b_next();
				if(onext != -1) {
					if(button[onext] < opos)
						opos--;
					else if(button[onext] > opos)
						opos++;
				}
			}
			else {
				int od = (onext == -1 ? 0 : abs(opos - button[onext]));
				int bd = (bnext == -1 ? 0 : abs(bpos - button[bnext]));
				if(bd == 0) {
					t += od;
					opos = button[onext];
				}
				else if(od == 0) {
					t += bd;
					bpos = button[bnext];
				}
				else {
					if(bd < od) {
						t += bd;
						bpos = button[bnext];
						opos = opos + bd * (button[onext] < opos ? -1 : 1);
					} else {
						t += od;
						opos = button[onext];
						bpos = bpos + od * (button[bnext] < bpos ? -1 : 1);
					}
				}
			}
		}
		printf("Case #%d: %d\n", casenum, t);
	}
}
