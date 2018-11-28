#include <cstdio>
#include <cstring>

char text[550];
int tam;
int pd[550][30];
char padrao[20] = {'w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'c', 'o', 'd', 'e', ' ', 'j', 'a', 'm', '\0'};
int tamPadrao;

int max = 10000;
int caso;

void read() {
	gets(text);
	tam = strlen(text);
}

int calc(int pt, int pp) {
	if (pd[pt][pp] == -1) {
		
		if (pp == tamPadrao) {
			pd[pt][pp] = 1;
		} else {
			int tot = 0;
			
			for (int i = pt+1; i < tam; i++) {
				if (text[i] == padrao[pp]) {
					tot += calc(i, pp+1);
					
					if (tot >= max) {
						tot %= max;
					}
				}
			}
			
			pd[pt][pp] = tot;
		}
	}
	
	return pd[pt][pp];
}

void process() {
	memset(pd, -1, sizeof(pd));
	
	int total = 0;
	for (int i = 0; i < tam; i++) {
		if (text[i] == padrao[0]) {
			total += calc(i, 1);
			
			if (total >= 10000) {
				total %= 10000;
			}
		}
	}
	
	printf("Case #%d: %04d\n", caso++, total);
}

int main() {
	//freopen("C-large.in", "r", stdin);
	//freopen("c.out", "w", stdout);
	
	tamPadrao = strlen(padrao);
	
	//printf("%s %d\n", padrao, tamPadrao);
	
	caso = 1;
	
	int casos;
	scanf("%d ", &casos);
	
	for (int i = 1; i <= casos; i++) {
		read();
		process();
	}
	
	return 0;
}
