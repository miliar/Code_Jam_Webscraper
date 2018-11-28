#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;


int N;
char basestr[100];
int basestrlen;
int **ps;
int *pslen;

void init() {
	//freopen("C-test.in","r",stdin);freopen("C-test.out","w",stdout);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&N);
	fgetc(stdin);
	strcpy(basestr, "welcome to code jam");
	basestrlen = strlen(basestr);
}

void initline() {
	ps = (int**)malloc(sizeof(int*)*basestrlen);
	pslen = (int*)malloc(sizeof(int)*basestrlen);
	
	char buf[512];
	fgets(buf, 512, stdin);
	
	int len = strlen(buf);
	if (buf[len-1] == '\n')
		len--;

	for(int i=0; i<basestrlen; i++) {
		ps[i] = (int*)malloc(sizeof(int)*500);
		pslen[i] = 0;
		for(int j=0; j<len; j++) {
			if (buf[j] == basestr[i]) {
				ps[i][pslen[i]] = j;
				pslen[i]++;
			}
		}
	}
}

void recurse(int letter, int index, int &result) {
	if (letter == basestrlen) {
		result = (result + 1) % 10000;
		return;
	}
	for(int i=0; i<pslen[letter]; i++) {
		if (ps[letter][i] < index)
			continue;

		recurse(letter + 1, ps[letter][i] + 1, result);
	}
}

void work(int ca) {
	int r=0;
	int letter=0, index=0;
	recurse(letter, index, r);
	printf("Case #%d: %04d\n", ca, r);
}

int main(int argc, char **argv) {
	init();
	for(int i=0; i<N; i++) {
		initline();
		work(i+1);
	}
	return 0;
}
