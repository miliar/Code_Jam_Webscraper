#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;


int L, D, N;
char **dict;
char *ct;

void init() {
	//freopen("A-test.in","r",stdin);freopen("A-test.out","w",stdout);
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&L,&D,&N);
	//printf("L: %d D: %d N: %d\n", L, D, N);
	dict = (char**)malloc(sizeof(char*)*D);
	for(int i=0; i<D; i++) {
		fgetc(stdin);
		dict[i] = (char*)malloc(L + 3);
		fgets(dict[i], L + 1, stdin);
	}
	for(int i=0; i<D; i++) {
		//printf("dict[%d]: %s\n", i, dict[i]);
	}
	fgetc(stdin);
	ct = (char*) malloc(D);
}

void printct(int p, int c) {
	printf("p: %d c: %d   ");
	for(int i=0; i<D; i++) {
		printf("(%d, %d)", i, ct[i]);
	}
	printf("\n");
}

void work(int ca) {
	memset(ct, 1, D);
	char c;
	c = fgetc(stdin);

	bool z = false;
	int p = 0;

	while( c!= '\n') {
		if (c == '(') {
			z = 1;
		}
		else if (c == ')') {
			z = 0;
			for(int i=0; i<D; i++) {
				ct[i] = (ct[i] == 2)?1:0;
			}
			//printct(p, c);
			p++;
		}
		else if (c>='a' && c<='z') {
			if (z) {
				for(int i=0; i<D; i++) {
					if ((ct[i] == 1) && (dict[i][p] == c)) {
						ct[i] = 2;
					}
				}
			} else {
				for(int i=0; i<D; i++) {
					if (ct[i] && (dict[i][p] != c)) {
						ct[i] = 0;
					}
				}
				p++;
			}
		}
		else {
			printf("error in %d, read char %d\n", ca, (int)c);
			return;
		}
		c = fgetc(stdin);
	}

	if (p!=L) {
		printf("error in %d, only found %d chars\n", ca, p);
	}

	int r=0;
	for(int i=0; i<D; i++) {	
		if (ct[i])
			r++;
	}
	printf("Case #%d: %d\n", ca, r);
}

int main(int argc, char **argv) {
	init();
	for(int i=0; i<N; i++) {
		work(i+1);
	}
	return 0;
}