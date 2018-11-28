#include <cstdio>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

int R,C,F;
char mapa[55][55];

struct Sit {
	int i,j;
	
	int a,b; // trecho aberto
	
	int d;
		
	bool operator <(const Sit & outro) const {
		return d > outro.d;
	}
};

int melhor[51][51][51][51];
bool marc[51][51][51][51];

priority_queue<Sit> heap;

void tenta(int i, int j, int queda, int d, int a, int b) {
	while (i < R-1) {
		if (mapa[i+1][j] == '.') {
			i++;
			queda++;
			a=b=C; // nao tem mais nada cavado
		} else {
			break;
		}
	}
	if (queda <= F) {
		Sit s;
		s.i = i;
		s.j = j;
		s.d = d;
		s.a = a;
		s.b = b;
		heap.push(s);
	}
}

void process() {
	
	memset(melhor, -1, sizeof(melhor));
	memset(marc, false, sizeof(marc));
	
	Sit s;
	s.i = 0;
	s.j = 0;
	s.a = s.b = C; // nada
	s.d = 0;
	
	
	
	melhor[0][0][C][C] = 0;
	
	while (!heap.empty()) {
		heap.pop();
	}
	
	heap.push(s);
	int a,b;
	
	//printf("\n");
	while (!heap.empty()) {
		s = heap.top();
		heap.pop();
		
		if (!marc[s.i][s.j][s.a][s.b]) {
			//printf("  -> (%d, %d) - %d\n", s.i, s.j, s.d);
			marc[s.i][s.j][s.a][s.b] = true;
			if (s.i == R-1) {
				printf("Yes %d\n", s.d);
				return;
			}
			
			
			a = b = s.j;
			while (a > 0) {
				if (mapa[s.i][a-1] == '#') {
					// ve se nao ta no livre
					if (s.a <= (a-1) && s.b >= (a-1)) {
						// ok
					} else {
						break;
					}
				}
				if (mapa[s.i+1][a-1] == '.'){
					break;
				}
				a--;
			}
			while (b < C-1) {
				if (mapa[s.i][b+1] == '#') {
					// ve se nao ta no livre
					if (s.a <= (b+1) && s.b >= (b+1)) {
						// ok
					} else {
						break;
					}
				}
				if (mapa[s.i+1][b+1] == '.'){
					break;
				}
				b++;
			}
			
			//printf("      -> a %d  b %d\n", a, b);
			
			// posso andar livremente entre a e b
			
			if (a > 0 && (mapa[s.i][a-1] == '.' || (s.a <= (a-1) && s.b >= (a-1)) ) ) {
				// posso cair para a esquerda
				tenta(s.i+1, a-1, 1, s.d, C,C);
			}
			
			if (b < C-1 && (mapa[s.i][b+1] == '.' || (s.a <= (b+1) && s.b >= (b+1)) ) ) {
				// posso cair para a direita
				tenta(s.i+1, b+1, 1, s.d, C,C);
			}
			
			if (a < b) {
				// posso cavar algum trecho entre a e b
				
				for (int a2 = a ; a2 <= b ; a2++) {
					for (int b2 = a2 ; b2 <= b ; b2++) {
						if (a2 > 0 && a2 > a) {
							// posso cair pela esquerda
							tenta(s.i+1, a2, 1, s.d + (b2-a2+1), a2,b2);
						}
						if (b2 < C-1 && b2 < b) {
							// posso cair pela direita
							tenta(s.i+1, b2, 1, s.d + (b2-a2+1), a2,b2);
						}
					}
				}
				
			}
			
			
			
			/*
			if (s.j > 0) {
				if (mapa[s.i][s.j-1] == '.') {
					
					tenta(s.i, s.j-1, 0, s.d);
					
					if (mapa[s.i+1][s.j-1] == '#') {
						tenta(s.i+1, s.j-1, 1, s.d+1);
					}
				}
			}
			
			if (s.j < C-1) {
				if (mapa[s.i][s.j+1] == '.') {
					
					tenta(s.i, s.j+1, 0, s.d);
					
					if (mapa[s.i+1][s.j+1] == '#') {
						tenta(s.i+1, s.j+1, 1, s.d+1);
					}
				}
			}
			*/
			
		}
		
	}
	
	printf("No\n");
}

void read() {
	scanf("%d%d%d", &R, &C, &F);
	for (int i = 0 ; i < R ; i++) {
		scanf("%s", mapa[i]);
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int N;
	scanf("%d", &N);
	for (int i = 1 ; i <= N ; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}
