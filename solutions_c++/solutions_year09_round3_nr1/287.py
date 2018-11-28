#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <map>
#include <string.h>

using namespace std;

map<char, int> mapa;
char s[500];

unsigned long long elev(unsigned long long n, int e) {
	unsigned long long ans = 1;
	for (int i=1;i<=e;i++) {
		ans *= n;
	}
	return ans;
}

int main() {
	int _42=1, N;
	scanf(" %d", &N);
	while (N--) {
		scanf(" %s", s);
		int tam = strlen(s);
		mapa.clear();
		mapa[s[0]] = 1;
		int prox=1;
		while (prox < tam && s[prox] == s[0]) {
			prox++;
		}
		if (prox < tam) mapa[s[prox]] = 0;
		int cont = 2;
		for (int i = prox+1;i<tam;i++) {
			if (mapa.find(s[i]) == mapa.end()) {
				mapa[s[i]] = cont++;
			}
		}
		unsigned long long ans = 0;
		for (int i=0;i<tam;i++) {
			ans += (unsigned long long)(mapa[s[i]])*elev(cont, tam-i-1);
		}
		printf("Case #%d: %llu\n", _42++, ans);
	}
	return 0;
}

