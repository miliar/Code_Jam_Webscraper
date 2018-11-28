#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <sstream>
#include <string>
#include <map>
#include <queue>

using namespace std;

int P;
int M[4100];
int p[4100][4100];
int qtd;
int part[4100][4100];
bool foi[4100][4100];

void read() {
	scanf("%d", &P);
	
	qtd = 1;
	for (int i = 0; i < P; i++) {
		qtd *= 2;
	}
	
	for (int i = 0; i < qtd; i++) {
		scanf("%d", &M[i]);
		M[i] = P-M[i];

		int at = i;
		int tam = qtd;
		for (int j = 0; j < P; j++) {
			tam /= 2;
			at = at/2;
			
			p[i][j] = at;
		}
	}
	
	int tam = qtd/2;
	for (int i = 0; i < P; i++) {
		for (int j = 0; j < tam; j++) {
			scanf("%d", &part[i][j]);
		}
		
		tam /= 2;
	}
	
}

void process() {
	
	int total = 0;
	memset(foi, false, sizeof(foi));
	for (int i = 0; i < qtd; i++) {
		
		int cont = 0;
		for (int j = P-1; j >= 0; j--) {
			
			if (cont < M[i]) {
			
				
			
				if (!foi[j][p[i][j]]) {
					//printf("i %d M %d partida %d, tot %d\n", i, M[i], j, part[j][p[i][j]]);
					total += part[j][p[i][j]];
					foi[j][p[i][j]] = true;
				}
				cont++;
			} else {
				break;
			}
		}
	}
	
	printf("%d\n", total);
}

int main() {
	
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	
	int casos;
	scanf("%d", &casos);
	for (int i = 1; i <= casos; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}
