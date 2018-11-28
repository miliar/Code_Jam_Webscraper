#include <cstdlib>
#include <cstdio>
#include <queue>
#define SAI_A 2
#define CHEGA_A 0
#define SAI_B 3
#define CHEGA_B 1

using namespace std;

typedef struct par {
	int first, second;
}par;

bool operator<(const par &a, const par &b) {
	if (a.first < b.first || (a.first == b.first && a.second < b.second)) return 0;
	return 1;
}

priority_queue<par> evento;

int main() {
	int i, N, NA, NB, T, ih, im, fh, fm, ansA, ansB, contA, contB, test=1;
	par aux;
	scanf("%d", &N);
	while (N--) {
		while (!evento.empty()) evento.pop();
		scanf("%d", &T);
		scanf("%d %d", &NA, &NB);
		for (i=0;i<NA;i++) {
			scanf("%d:%d %d:%d", &ih, &im, &fh, &fm);
			aux.first = ih*60 + im;
			aux.second = SAI_A;
			evento.push(aux);
			aux.first = fh*60 + fm + T;
			aux.second = CHEGA_B;
			evento.push(aux);
		}
		for (i=0;i<NB;i++) {
			scanf("%d:%d %d:%d", &ih, &im, &fh, &fm);
			aux.first = ih*60 + im;
			aux.second = SAI_B;
			evento.push(aux);
			aux.first = fh*60 + fm + T;
			aux.second = CHEGA_A;
			evento.push(aux);
		}
		contA = contB = ansA = ansB = 0;
		while (!evento.empty()) {
			aux = evento.top();
			evento.pop();
			if (aux.second == SAI_A) {
				if (contA == 0) {
					ansA++;
				}
				else {
					contA--;
				}
			}
			else if (aux.second == CHEGA_A) {
				contA++;
			}
			else if (aux.second == SAI_B) {
				if (contB == 0) {
					ansB++;
				}
				else {
					contB--;
				}
			}
			else {
				contB++;
			}
		}
		printf("Case #%d: %d %d\n", test++, ansA, ansB);
	}
	return 0;
}

