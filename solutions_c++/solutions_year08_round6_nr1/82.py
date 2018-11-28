
#include <stdio.h>
#include <vector>
#include <set>

using namespace std;

int prob, nprob;
int N, M;
int nbH[1000], nbW[1000];
int tot;
int H1, W1, H2, W2;
int HH1, WW1, HH2, WW2;
set<pair<int,int> > nb;


int main() {
	freopen("a.in", "r", stdin);
	//freopen("a.out", "w", stdout);

	scanf("%d", &nprob);
	for (prob = 1; prob <= nprob; prob++) {
		scanf("%d", &N);
		int flag = 0;
		H2 = W2 = 0; H1 = W1 = 100000000; tot = 0; nb.clear();
		for (int i = 0; i < N; i++) {
			int h, w; char b[10];
			scanf("%d%d %s", &h, &w, b);
			if (b[0] == 'B') {
				if (h > H2) H2 = h;
				if (w > W2) W2 = w;
				if (h < H1) H1 = h;
				if (w < W1) W1 = w;
				flag = 1;
			} else {
				nbH[tot] = h; nbW[tot] = w; tot++;
				scanf("%*s");
			}
		}

		HH1 = WW1 = 0; HH2 = WW2 = 100000000;
		for (int i = 0; i < tot; i++) {
			if (flag == 0) {
				nb.insert(make_pair(nbH[i], nbW[i]));
				continue;
			}

			if (nbH[i] > H2) {
				if (nbH[i] < HH2) HH2 = nbH[i];
			}
			if (nbH[i] < H1) {
				if (nbH[i] > HH1) HH1 = nbH[i];
			}
			if (nbW[i] > W2) {
				if (nbW[i] < WW2) WW2 = nbW[i];
			}
			if (nbW[i] < W1) {
				if (nbW[i] > WW1) WW1 = nbW[i];
			}
		}

		printf("Case #%d:\n", prob);

		scanf("%d", &M);
		for (int i = 0; i < M; i++) {
			int h, w;
			scanf("%d%d", &h, &w);
			if (!flag) {
				if (nb.find(make_pair(h, w)) != nb.end())
					printf("NOT BIRD\n");
				else
					printf("UNKNOWN\n");

				continue;
			}

			if (h >= H1 && h <= H2 && w >= W1 && w <= W2)
				printf("BIRD\n");
			else if (h > HH1 && h < HH2 && w > WW1 && w < WW2)
				printf("UNKNOWN\n");
			else
				printf("NOT BIRD\n");
		}
	}


	return 0;
}
