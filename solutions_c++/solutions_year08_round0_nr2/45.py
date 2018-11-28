#include <cstdio>
#include <queue>

using namespace std;

int T;
int NA, NB;

// 0 - Saida em A, 1 - Saida em B, 2 - chegada em A, 3 - chegada em B

priority_queue< pair <int, int> > heap;

int h, m;
char lixo;
void read() {
	scanf("%d ", &T);
	scanf("%d %d", &NA, &NB);
	
	while (!heap.empty()) {
		heap.pop();
	}
	
	pair<int, int> evento;
	
	for (int i = 0 ; i < NA ; i++) {
		scanf("%d%c%d", &h, &lixo, &m);
		evento.first = -(h*60 + m);
		evento.second = 0; // saida em A
		heap.push(evento);
		
		scanf("%d%c%d", &h, &lixo, &m);
		evento.first = -(h*60 + m + T);
		evento.second = 3; // chegada em B
		heap.push(evento);
	}

	
	for (int i = 0 ; i < NB ; i++) {

		scanf("%d%c%d", &h, &lixo, &m);
		evento.first = -(h*60 + m);
		evento.second = 1; // saida em B
		heap.push(evento);
				
		scanf("%d%c%d", &h, &lixo, &m);
		evento.first = -(h*60 + m + T);
		evento.second = 2; // chegada em A
		heap.push(evento);
		
	}
	

	
	/* Teste da leitura
	printf("\n A:\n");
	for (int i = 0 ; i < NA ; i++) {
		printf("%d\n", tabelaA[i].first);
	}
	
	printf("\n B:\n");
	for (int i = 0 ; i < NB ; i++) {
		printf("%d\n", tabelaB[i].first);
	}*/
}


void process() {
	
	int aInicio, bInicio, a, b;	
	aInicio = bInicio = a = b = 0;
	
	while (!heap.empty()) {
		pair <int, int> e = heap.top();
		heap.pop();
				
		int tempo = e.first;
		int evento = e.second;
		
		// 0 - Saida em A, 1 - Saida em B, 2 - chegada em A, 3 - chegada em B
		
		if (evento == 0) { // saida em A
			
			if (a > 0) {
				a--;
			} else {
				aInicio++;
			}
			
		} else if (evento == 1) { // saida em B
		
			if (b > 0) {
				b--;
			} else {
				bInicio++;
			}
			
		} else if (evento == 2) { // chegada em A
		
			a++;
			
		} else if (evento == 3) { // chegada em B
			
			b++;
			
		}
		
	}
	
	printf("%d %d\n", aInicio, bInicio);
}

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int qnt;
	scanf("%d ", &qnt);
	
	for (int i = 1 ; i <= qnt ; i++) {
		read();
		printf("Case #%d: ", i);
		process();
	}
	
	return 0;
}
