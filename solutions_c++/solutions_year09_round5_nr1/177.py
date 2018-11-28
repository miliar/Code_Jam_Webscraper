#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cstdlib>

using namespace std;

int R,C;
char mapa[20][20];

int qtdBoxes;

struct Sit {
	int i[5];
	int j[5];
	bool operator< (const Sit & outro) const {
		for (int x = 0 ; x < qtdBoxes ; x++) {
			if (i[x] != outro.i[x]) return i[x] < outro.i[x];
			if (j[x] != outro.j[x]) return j[x] < outro.j[x];
		}
		return false;
	}
};

set<Sit> marcados;
bool isMarc(Sit s) {
	return marcados.find(s) != marcados.end();
}

void marc(Sit s) {
	marcados.insert(s);
}

map<Sit, int> distancias;
int getDist(Sit s) {
	if (distancias.find(s) == distancias.end()) {
		return 0x63636363;
	} else {
		return distancias[s];
	}
}

struct SitDist {
	Sit s;
	int d;
	bool operator<(const SitDist & outro) const {
		return d > outro.d;
	}
};

pair<int,int> pares[5];
Sit ajustar(Sit s) {
	for (int i = 0 ; i < qtdBoxes ; i++) {
		pares[i].first = s.i[i];
		pares[i].second = s.j[i];
	}
	sort(pares, pares+qtdBoxes);
	for (int i = 0 ; i < qtdBoxes ; i++) {
		s.i[i] = pares[i].first;
		s.j[i] = pares[i].second;
	}
	return s;
}

int incI[4] = { 0, 1, 0,-1};
int incJ[4] = { 1, 0,-1, 0};

bool verificar(Sit &s, int caixa) {
	if (qtdBoxes == 1) return true;
	bool ok;
	for (caixa = 0 ; caixa < qtdBoxes ; caixa++ ) {
		ok = false;
		for (int i = 0 ; i < qtdBoxes ; i++) {
			if (caixa != i) {
				if (s.i[caixa] == s.i[i]) {
					if (s.j[caixa]+1 == s.j[i] || s.j[caixa]-1 == s.j[i]) {
						ok = true;
						break;
					}
				}
				if (s.j[caixa] == s.j[i]) {
					if (s.i[caixa]+1 == s.i[i] || s.i[caixa]-1 == s.i[i]) {
						ok = true;
						break;
					}
				}
				
			}
		}
		if (!ok) return false;
	}
	return true;
}

priority_queue<SitDist> heap;

void insercaoValida(Sit s, int d) {
	s = ajustar(s);
	if (!isMarc(s)) {
		if (getDist(s) > d+1) {
			distancias[s] = d+1;
			SitDist sd;
			sd.s = s;
			sd.d = d+1;
			heap.push(sd);
		}
	}
}

void tentar2(Sit s, int d, int caixa, int iLivre, int jLivre) {
	if (s.i[caixa] >= 0 && s.i[caixa] < R && s.j[caixa] >= 0 && s.j[caixa] < C) {
		if (mapa[s.i[caixa]][s.j[caixa]] == '.' || mapa[s.i[caixa]][s.j[caixa]] == 'x') {
			bool ok = true;
			for (int i = 0 ; i < qtdBoxes ; i++) {
				if (caixa != i) {
					if (s.i[i] == s.i[caixa] && s.j[i] == s.j[caixa]) {
						ok = false;
						break;
					}
					if (s.i[i] == iLivre && s.j[i] == jLivre) {
						ok = false;
						break;
					}
				}
			}
			if (ok) {
				
				if (verificar(s,caixa)) {
					
					insercaoValida(s,d);
					
				}
				
			}
		}
	}
}

void andar2(Sit s, int d, int caixa) {
	for (int lado = 0 ; lado < 4 ; lado++) {
		int iLivre = s.i[caixa]-incI[lado];
		int jLivre = s.j[caixa]-incJ[lado];
		if (iLivre >= 0 && iLivre < R && jLivre >= 0 && jLivre < C) {
			if (mapa[iLivre][jLivre] == '.' || mapa[iLivre][jLivre] == 'x') {
				s.i[caixa]+=incI[lado];
				s.j[caixa]+=incJ[lado];
				tentar2(s,d,caixa,iLivre,jLivre);
				s.i[caixa]-=incI[lado];
				s.j[caixa]-=incJ[lado];
			}
		}
	}
}

void tentar(Sit s, int d, int caixa, int iLivre, int jLivre) {
	if (s.i[caixa] >= 0 && s.i[caixa] < R && s.j[caixa] >= 0 && s.j[caixa] < C) {
		if (mapa[s.i[caixa]][s.j[caixa]] == '.' || mapa[s.i[caixa]][s.j[caixa]] == 'x') {
			bool ok = true;
			for (int i = 0 ; i < qtdBoxes ; i++) {
				if (caixa != i) {
					if (s.i[i] == s.i[caixa] && s.j[i] == s.j[caixa]) {
						ok = false;
						break;
					}
					if (s.i[i] == iLivre && s.j[i] == jLivre) {
						ok = false;
						break;
					}
				}
			}
			if (ok) {
				
				if (verificar(s,caixa)) {
					
					insercaoValida(s,d);
					
				} else {
					for (int i = 0 ; i < qtdBoxes ; i++) {
						andar2(s,d+1,i);
					}
				}
				
			}
		}
	}
}

void andar(Sit s, int d, int caixa) {
	for (int lado = 0 ; lado < 4 ; lado++) {
		int iLivre = s.i[caixa]-incI[lado];
		int jLivre = s.j[caixa]-incJ[lado];
		if (iLivre >= 0 && iLivre < R && jLivre >= 0 && jLivre < C) {
			if (mapa[iLivre][jLivre] == '.' || mapa[iLivre][jLivre] == 'x') {
				s.i[caixa]+=incI[lado];
				s.j[caixa]+=incJ[lado];
				tentar(s,d,caixa,iLivre,jLivre);
				s.i[caixa]-=incI[lado];
				s.j[caixa]-=incJ[lado];
			}
		}
	}
}


void process(int caso){
	
	marcados.clear();
	distancias.clear();
	while (!heap.empty()) {
		heap.pop();
	}
	
	Sit s;
	qtdBoxes = 0;
	for (int i = 0 ; i < R ; i++) {
		for (int j = 0 ; j < C ; j++) {
			if (mapa[i][j] == 'o') {
				s.i[qtdBoxes] = i;
				s.j[qtdBoxes] = j;
				qtdBoxes++;
				mapa[i][j] = '.';
			} else if (mapa[i][j] == 'w') {
				s.i[qtdBoxes] = i;
				s.j[qtdBoxes] = j;
				qtdBoxes++;
				mapa[i][j] = 'x';
			}
		}
	}
	
	s = ajustar(s);
	distancias[s] = 0;
	SitDist sd;
	sd.s = s;
	sd.d = 0;
	
	heap.push(sd);
	int resultado = -1;
	bool ok;
	
	while (!heap.empty()) {
		sd = heap.top();
		heap.pop();
		s = sd.s;
		
		if (!isMarc(s)) {
			marc(s);
			
			ok = true;
			for (int i = 0 ; i < qtdBoxes ; i++) {
				if (mapa[s.i[i]][s.j[i]] != 'x') {
					ok = false;
					break;
				}
			}
			if (ok) {
				resultado = sd.d;
				break;
			}
			
			for (int i = 0 ; i < qtdBoxes ; i++) {
				andar(s, sd.d, i);
			}
			
		}
		
	}
	
	//printf("qtdBoxes %d\n", qtdBoxes);
	
	printf("Case #%d: %d\n", caso, resultado);
	
	
}

void read(){
	scanf("%d%d", &R, &C);
	for (int i = 0 ; i < R ; i++) {
		scanf("%s", mapa[i]);
	}
}

int main(){
	
	freopen("A-small-attempt1.in","r", stdin);
	freopen("A-small-attempt1.out","w", stdout);
	
	int T;
	scanf("%d", &T);
	for (int i = 1 ; i <= T ; i++) {
		read();
		process(i);
	}
	
	return 0;
}
