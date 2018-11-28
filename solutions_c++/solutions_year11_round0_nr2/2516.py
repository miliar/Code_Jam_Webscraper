#include <stdio.h>

char combiners[36][3];
int ncombiners;

char negaters[28][2];
int nnegaters;


char combines(char c1, char c2) {
	int i;
	for(i = 0; i < ncombiners; i++) {
		if ((combiners[i][0] == c1 && combiners[i][1] == c2) ||
		    (combiners[i][1] == c1 && combiners[i][0] == c2)) {
			return combiners[i][2];
		}
	}
	return '\0';
}

int negates(char c1, char c2) {
	int i;
	for(i = 0; i < nnegaters; i++) {
		if ((negaters[i][0] == c1 && negaters[i][1] == c2) ||
		    (negaters[i][1] == c1 && negaters[i][0] == c2)) {
			return 1;
		}
	}
	return 0;
}

class invocation {
	char elts[100];
	int nelts;
		
    public:
	invocation() : nelts(0) {}
	void add(char c) {
		if (nelts == 0) {
			elts[0] = c;
			nelts = 1;
			return;
		}
		char comb = combines(c, elts[nelts-1]);
		if (comb) {
			nelts--;
			add(comb);
		} else {
			int i;
			for(i = 0; i < nelts; i++) {
				if (negates(c, elts[i])) {
					nelts = 0;
					return;
				}
			}
			elts[nelts] = c;
			nelts++;
			return;
		}
	}
	void print() {
		int i;
		printf("[");
		for(i = 0; i < nelts; i++) {
			if (i > 0) {
				printf(", ");
			}
			putchar(elts[i]);
		}	
		printf("]");
	}
};

int main() {
	int ncases;
	scanf("%d", &ncases);
	int i, j, k;
	for(i = 1; i <= ncases; i++) {
		int c, d, n;
		scanf("%d ", &c);
		ncombiners = 0;
		for(j = 0; j < c; j++) {
			char c1, c2, tgt;
			scanf("%c%c%c ", &c1, &c2, &tgt);
			combiners[ncombiners][0] = c1;
			combiners[ncombiners][1] = c2;
			combiners[ncombiners][2] = tgt;
			ncombiners++;
		}
		scanf("%d ", &d);
		nnegaters = 0;
		for(j = 0; j < d; j++) {	
			char c1, c2;
			scanf("%c%c ", &c1, &c2);
			negaters[nnegaters][0] = c1;	
			negaters[nnegaters][1] = c2;	
			nnegaters++;
		}
		scanf("%d ", &n);
		char ch;
		invocation inv;	
		for(j = 0; j < n; j++) {
			scanf("%c", &ch);
			inv.add(ch);
		}	
		printf("Case #%d: ", i);
		inv.print();
		printf("\n");
	}
}	
