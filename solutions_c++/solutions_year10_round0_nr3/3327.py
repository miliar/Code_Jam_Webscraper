#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <algorithm>

using namespace std;

int R,k,N;
int g[5000];
int soma;
void read() {
	scanf("%d%d%d", &R, &k, &N);
	soma = 0;
	for (int i = 0 ; i < N ; i++) {
		scanf("%d", &g[i]);
		soma += g[i];
	}
}

int vez[5000]; // i estava na frente da fila logo antes da vez vez[i]
int val[5000]; // logo antes da vez[i], ja tinhamos o valor val[i]
void process() {
	
	if (soma <= k) {
		printf("%d\n", soma*R);
		return;
	}
	
	memset(vez, -1, sizeof(vez));
	int total = 0;
	int grupo = 0;
	int i;
	int temp;
	for (i = 0 ; i < R ; i++) {
		if (vez[grupo] == -1) {
			vez[grupo] = i;
			val[grupo] = total;
			
			temp = 0;
			while (temp + g[grupo] <= k) {
				temp += g[grupo];
				grupo++;
				if (grupo == N) grupo = 0;
			}
			total += temp;
		} else {
			int tamCiclo =  i - vez[grupo];
			int falta = R - i;
			int mult = falta / tamCiclo;
			int valCiclo = total - val[grupo];
			total += valCiclo * mult;
			i+= tamCiclo*mult;
			
			for (; i < R ; i++) {
				temp = 0;
				while (temp + g[grupo] <= k) {
					temp += g[grupo];
					grupo++;
					if (grupo == N) grupo = 0;
				}
				total += temp;
			}
			break;
		}
	}
	
	printf("%d\n", total);
}

int main() {
	
	int T;
	scanf("%d", &T);
	for (int i = 1 ; i <= T ; i++) {
		read();
		printf("Case #%d: ", i);
		process();
	}
	
	return 0;
}
