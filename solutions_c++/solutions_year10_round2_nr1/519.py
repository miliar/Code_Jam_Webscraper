#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
#include <string>
using namespace std;

map<string, int> mapa;
char s[200];

int main() {
	int _42=1, T, N, M;
	scanf(" %d", &T);
	while (T--) {
		scanf(" %d %d", &N, &M);
		mapa.clear();
		for (int i=0;i<N;i++) {
			scanf(" %s", s);
			string aux = s;
			mapa[s] = 1;
		}
		int ans = 0;
		for (int i=0;i<M;i++) {
			scanf(" %s", s);
			string aux = s;
			for (int j=1;j<aux.size();j++) if (aux[j] == '/') {
				string aux2 = aux.substr(0, j);
				if (mapa[aux2] != 1) {
					mapa[aux2] = 1;
					ans++;
				}
			}
			if (mapa[aux] != 1) {
				mapa[aux] = 1;
				ans++;
			}
		}
		
		printf("Case #%d: ", _42++);
		printf("%d\n", ans);
	}
}
