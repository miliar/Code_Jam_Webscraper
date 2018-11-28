#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <map>
#include <string>

using namespace std;

map<string, int> engine;
char nome[110], marca[110], buf[200];

int main() {
	int i, test=1, N, S, Q, tam, marcados, ans;
	gets(buf);
	sscanf(buf, "%d", &N);
	while (N--) {
		engine.clear();
		gets(buf);
		sscanf(buf, "%d", &S);
		for (i=1;i<=S;i++) {
			gets(nome);
			tam = strlen(nome);
			if (nome[tam-1] == '\n') nome[tam-1] = '\0';
			string s = nome;
			engine[s] = i;
		}
		gets(buf);
		sscanf(buf, "%d", &Q);
		ans = 0;
		marcados = 0;
		memset(marca, 0, sizeof(marca));
		for (i=0;i<Q;i++) {
			gets(nome);
			tam = strlen(nome);
			if (nome[tam-1] == '\n') nome[tam-1] = '\0';
			string s = nome;
			if (marca[engine[s]] == 0) {
				marca[engine[s]] = 1;
				marcados++;
				if (marcados == S) {
					ans++;
					memset(marca, 0, sizeof(marca));
					marcados = 1;
					marca[engine[s]] = 1;
				}
			}
		}
		printf("Case #%d: %d\n", test++, ans);
	}
	return 0;
}
