#include<stdio.h>

#include<algorithm>
#include<bitset>
using namespace std;

const int MAXD = 5012;
const int MAXL = 16;

char cuv[MAXD][MAXL];
bitset<MAXD> cur, tot;

int l, d, n;

void mark(char x, int lit) {
	for (int j=0; j<d; ++j)
		if (cuv[j][lit] == x)
			cur.set(j);
}

int main(void) {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	
	scanf("%d%d%d", &l, &d, &n);
	for (int i=0; i<d; ++i) {
		scanf("%s\n", cuv[i]);
	}
		
	for (int i=1; i<=n; ++i) {
		tot.set();
		cur.reset();
		for (int lit=0; lit<l; ++lit) {
			cur.reset();
			char x;
			scanf("%c", &x);
			if (x == '(') {
				scanf("%c", &x);
				while (x != ')') {
					mark(x, lit);
					scanf("%c", &x);
				}
			}
			else mark(x, lit);
			
			tot &= cur;
		}
		scanf("%*c"); // skip newline
		printf("Case #%d: %d\n", i, tot.count());
	}
	
	return 0;
}
