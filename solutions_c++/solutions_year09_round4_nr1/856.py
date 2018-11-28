#include <cstdio>
#include <cstring>

#include <algorithm>

using namespace std;

int N;
char mapa[50][50];
int longe[50];
int perm[50];
int mark[50];

void read() {
	scanf("%d", &N);
	
	for (int i = 0; i < N; i++) {
		scanf("%s", mapa[i]);
	}
}

void process() {
	bool achou;
	for (int i = 0; i < N; i++) {
		achou = false;
		for (int j = N-1; j >= 0; j--) {
			if (mapa[i][j] == '1') {
				longe[i] = j;
				achou = true;
				break;
			}
		}
		
		if (!achou) {
			longe[i] = 0;
		}
	}
	
	int val;
	int qtdTrocas = 0;
	for (int i = 0; i < N; i++) {
		//printf("longe %d -> %d\n", i, longe[i]);
		if (longe[i] > i) {
			for (int j = i+1; j < N; j++) {
				if (longe[j] <= i) {
					val = longe[j];
					
					for (int k = j; k >= i+1; k--) {
						longe[k] = longe[k-1];
						qtdTrocas++;
					}
					longe[i] = val;
					
					break;
				}
			}
		}
	}
	
	printf("%d\n", qtdTrocas);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int casos;
	scanf("%d", &casos);
	
	for (int i = 1; i <= casos; i++) {
		printf("Case #%d: ", i);
		
		read();
		process();
	}
	
	return 0;
}
