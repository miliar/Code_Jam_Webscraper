#include <stdio.h>
#include <string.h>
#include <string>
#include <map>

using namespace std;


int N, S, Q;
map<string,int> aparicoes;

int main() {

	scanf(" %d", &N);
	for (int _42=1; _42 <= N; _42++) {
		aparicoes.clear();
		int ans = 0;
		char buf[200];
		int nao_apareceram;

		scanf(" %d ", &S);
		for (int i=0; i < S; i++) {
			gets(buf);
		}

		nao_apareceram = S;
		string s;
		scanf(" %d ", &Q);
		for (int i=0; i < Q; i++) {
			gets(buf);
			s = buf;
			if (aparicoes[s] == 0) {
				//printf(" @@ eliminei %s\n", buf);
				nao_apareceram--;
			}

			if (nao_apareceram == 0) {
				// todas as engines acabaram de aparecer
				// incrementa uma troca, e reinicia
				ans++;
				aparicoes.clear();
				nao_apareceram = S-1;
				//printf(" >> troquei em %s\n", buf);
			}

			aparicoes[s]++;
		}

		printf("Case #%d: %d\n", _42, ans);
	}


	return 0;
}
