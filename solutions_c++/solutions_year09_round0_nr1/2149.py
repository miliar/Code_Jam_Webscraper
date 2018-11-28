#include <cstdio>
#define FOR(i,a,b) for(int i=a; i<b; ++i)
using namespace std;

int L, D, N;
char tab[5005][17];

int main() {
	scanf("%d%d%d", &L, &D, &N);
	FOR(i,0,D) scanf("%s", tab[i]);
	//FOR(i,0,D) printf("* %s\n", tab[i]);
	FOR(z,0,N) {
		char aux[500];
		scanf("%s", aux);
		int res = 0;
		FOR(i,0,D) {
			int cnt = 1, k = 0;
			FOR(j,0,L) {
				if(aux[k] == '(') {
					++k;
					int g = 0;
					while(aux[k] != ')') {
						if(aux[k] == tab[i][j]) g = 1;
						++k;
					}
					if(!g) {
						cnt = 0;
						break;
					}
					++k;
				} else {
					if(aux[k] != tab[i][j]) {
						cnt = 0;
						break;
					}
					++k;
				}
			}
			res += cnt;
		}
		printf("Case #%d: %d\n", z + 1, res);
	}
	return 0;
}
