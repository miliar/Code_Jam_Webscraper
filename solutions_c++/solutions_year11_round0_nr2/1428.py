# include <cstdio>
# include <cstring>
# include <string>
# include <vector>
# include <queue>
# include <map>
# include <set>
# include <algorithm>
# include <cstdlib>

# define INF 0x3f3f3f3f

using namespace std;

int mat[1024][1024];
int op[1024][1024];
int lista[1000000];

int main (void){
	int T, C, D, N;
	char str[128];
	char combine[16];
	char oposto[16];
	scanf("%d", &T);
	for(int tc = 1; tc <= T; tc++){
		scanf("%d", &C);
		memset(mat, INF, sizeof(mat));
		for(int i = 0 ; i < C; i++){
			scanf(" %s", combine);
			mat[(int) combine[0]][(int) combine[1]] = mat[(int) combine[1]][(int) combine[0]] = combine[2];
		}
		scanf("%d", &D);
		memset(op, false, sizeof(op));
		for(int i = 0 ; i < D; i++){
			scanf(" %s", oposto);
			op[(int) oposto[0]][(int) oposto[1]] = op[(int) oposto[1]][(int) oposto[0]] = true;
		}
		scanf("%d", &N);
		scanf(" %s", str);
		int cnt = 0;
		
		for(int i = 0 ; i < N; i++){
			
			if( cnt == 0 ){
				lista[cnt++] = str[i];
				continue;
			}
			char last = (char) lista[cnt-1];
			if( mat[str[i]][last] != INF ){
				cnt--;
				lista[cnt++] = mat[str[i]][last];
				last = (char) mat[str[i]][last];
			}
			else{
				bool temOposto = false;
				for(int j = cnt-1; j>=0; j--){
					if( op[str[i]][(char) lista[j]] ){
						cnt = 0;
						temOposto = true;
						break;
					}
				}
				if( !temOposto ){
					lista[cnt++] = str[i];
					last = str[i];
				}
			}
		}
		string resposta = "";
		resposta += '[';
		for(int i = 0 ; i< cnt; i++){
			if( i > 0 ){
				resposta += ", ";
				resposta += lista[i];
			}
			else resposta += lista[i];
		}
		resposta += ']';
		printf("Case #%d:", tc);
		printf(" %s\n",  resposta.c_str());
	}
	return 0;
}