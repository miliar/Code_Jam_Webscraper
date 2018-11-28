#include <cstdio>
#include <cstring>

using namespace std;

char wel[] = "welcome to code jam";
#define MOD 10000;

char in[1024];
int tab[2][20];
int s;

int main(){
	s = strlen(wel);
	int N;
	scanf("%d", &N);
	fgets(in, 1024, stdin);
	for(int tc=1; tc<=N; ++tc){
		int i, ii;
		memset(tab, 0, sizeof(tab));
		tab[1][0] = 1;
		fgets(in, 1024, stdin);
		int l = strlen(in);
		for(i=0; i<l; ++i){
			ii = i&1;
			tab[ii][0] = tab[!ii][0];
			for(int j=0; j<s; ++j){
				tab[ii][j+1] = tab[!ii][j+1];
				if(wel[j] == in[i])
					tab[ii][j+1] = (tab[ii][j+1] + tab[!ii][j]) % MOD;
			}
		}
		printf("Case #%d: %.4d\n", tc, tab[!(i&1)][19]);
	}
}
