#include <stdio.h>
#include <string.h>

bool marca[15][2000];
int anc[2000][15], d[2000];
int M[2000];

int main() {
	int T, _42=1, P;
	scanf(" %d", &T);
	while (T--) {
		scanf(" %d", &P);
		for (int i=0;i<(1<<P);i++) {
			scanf(" %d", &M[i]);
			d[i] = P - M[i];
		}
		for (int i=P-1;i>=0;i--) {
			for (int j=0;j<(1<<i);j++) {
				int bla;
				scanf(" %d", &bla);
			}
		}
		for (int i=1;i<=P;i++) {
			for (int j=0;j<(1<<P);j++) {
				anc[j][i] = (j/(1<<i));
			}
		}
		memset(marca, 0, sizeof(marca));
		int ans = 0;
		while (1) {
			int best = -1, maior = 0;
			for (int i=0;i<(1<<P);i++) {
				if (d[i] > maior) {
					maior = d[i];
					best = i;
				}
			}
			if (best == -1) break;
			
			for (int i=P;i>=1;i--) {
				if (!marca[i][anc[best][i]]) {
					marca[i][anc[best][i]] = true;
					ans++;
					for (int j=0;j<(1<<P);j++) {
						if (anc[j][i] == anc[best][i]) {
							d[j]--;
						}
					}
				}
				if (d[best] == 0) break;
			}
		}
		printf("Case #%d: %d\n", _42++, ans);
	}
}
