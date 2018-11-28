#include <cstdio>

char words[5000][17];
bool letterPossible[15][256];
char code[1000];

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int l, d, n;
    scanf("%d", &l);
    scanf("%d", &d);
    scanf("%d", &n);

    for(int i = 0; i < d; i++)
	scanf("%s", words[i]);

    for(int casenum = 1; casenum <= n; casenum++) {

	scanf("%s", code);

	int index = 0;
	for(int i = 0; i < l; i++) {

	    for(int j = 0; j < 256; j++)
		letterPossible[i][j] = false;

	    if(code[index] == '(') {
		index++;
		while(code[index] != ')') {
		    letterPossible[i][code[index]] = true;
		    index++;
		}
		index++;
	    }
	    else {
		letterPossible[i][code[index]] = true;
		index++;
	    }

	}

	int count = d;
	for(int i = 0; i < d; i++) {
	    for(int j = 0; j < l; j++) {
		if(!letterPossible[j][words[i][j]]) {
		    count--;
		    break;
		}
	    }
	}

	printf("Case #%d: %d\n", casenum, count);

    }
}
