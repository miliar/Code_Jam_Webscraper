#include <cstdio>

int L, D, N;
char dic[5100][20];

char word[20][25];
int qtdWord[20];

char temp[10100];
int K;

void preRead() {
	scanf("%d%d%d", &L, &D, &N);
	
	
	for (int i = 0; i < D; i++) {
		scanf("%s", dic[i]);
	}
	/*
	for (int i = 0; i < D; i++) {
		printf("%s\n", dic[i]);
	}
	*/
}

void read() {
	scanf("%s", temp);
	//printf("%s\n", temp);

	int j, pos;
	j = 0;
	pos = 0;
	while (temp[j] != '\0') {
		if (temp[j] == '(') {
			j++;
			qtdWord[pos] = 0;
			while (temp[j] != ')') {
				word[pos][qtdWord[pos]++] = temp[j];
				j++;
			}
			j++;
		} else {
			qtdWord[pos] = 1;
			word[pos][0] = temp[j];
			j++;
		}
		
		//printf("leu %d\n", pos+1);
		pos++;
	}
	
	/*
	for (int j = 0; j < L; j++) {
		printf("pos %d:", j);
		for (int k = 0; k < qtdWord[j]; k++) {
			printf(" %c", word[j][k]);
		}
		printf("\n");
	}
	*/
}

void calc() {
	K = 0;

	bool pode;
	bool algum;
	for (int i = 0; i < D; i++) {
		pode = true;
		for (int j = 0; j < L; j++) {
			
			algum = false;
			for (int k = 0; k < qtdWord[j]; k++) {
				if (word[j][k] == dic[i][j]) {
					algum = true;
					break;
				}
			}
			
			if (!algum) {
				pode = false;
				break;
			}
		}
		
		if (pode) {
			K++;
		}
	}
}

void process() {
	int caso = 1;
	for (int i = 0; i < N; i++) {
		read();
		
		calc();
		printf("Case #%d: %d\n", caso++, K);
	}
}

int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("a.out", "w", stdout);
	
	preRead();
	process();
	
	return 0;
}
