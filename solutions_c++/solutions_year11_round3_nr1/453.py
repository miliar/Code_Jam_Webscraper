#include <cstdio>

int cas, t, r, c, cnt;
char g[51][51];
bool flag;

int main(void)
{
	scanf("%d", &t);
	for(cas = 1; cas <= t; cas++){
		scanf("%d%d", &r, &c);

		cnt = 0;
		getchar();
		for(int i=0; i<r; i++){
			for(int j=0; j<c; j++){
				scanf("%c", &g[i][j]);
				if(g[i][j] == '#') cnt++;
			}
			getchar();
		}

		if(cnt % 4) {
			printf("Case #%d:\nImpossible\n", cas);
			continue;
		}
		
		flag = true;
		while(cnt){
			for(int i=0; i<r; i++){
				for(int j=0; j<c; j++){
					if(g[i][j]=='#'){
						if(g[i][j+1]=='#'&&g[i+1][j]=='#'&&g[i+1][j+1]=='#'){
							g[i][j]='/';
							g[i][j+1]='\\';
							g[i+1][j]='\\';
							g[i+1][j+1]='/';
							cnt -= 4;
						} else {
							flag = false;
						}
					}
					if(!flag)
						break;
				}
				if(!flag)
					break;
			}
			if(!flag)
				break;
		}

		if(flag){
			printf("Case #%d:\n", cas);
			for(int i=0; i<r; i++){
				for(int j=0; j<c; j++){
					printf("%c", g[i][j]);
				}
				puts("");
			}
		} else {
			printf("Case #%d:\nImpossible\n", cas);
		}

	}
}
