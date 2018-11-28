#include <cstdio>
#include <cstring>

int num[50];
int N;


void process() {
	
	int trocas = 0;
	int j, temp;
	for (int i = 0 ; i < N ; i++) {
		if (num[i] > i) {
			// pega o primeiro <= i e traz pra cima
			for (j = i+1 ; num[j] > i ; j++);
			
			// trocar i por j
			temp = num[j];
			for (int k = j ; k > i ; k--) {
				num[k] = num[k-1];
			}
			num[i] = temp;
			trocas+=j-i;
		}
	}
	
	printf("%d\n", trocas);
}

char input[50];
void read() {
	scanf("%d", &N);
	
	for (int i = 0 ; i < N ; i++) {
		scanf("%s", input);
		num[i] = 0;
		for (int j = 0 ; j < N ; j++) {
			if (input[j] == '1') {
				num[i] = j;
			}
		}
	}
	
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 1 ; i <= T ; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}
