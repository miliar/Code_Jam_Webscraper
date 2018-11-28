#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;

char s[200];

int inv[30][30], op[30][30];

int main(){
	int i, j, k, m, n, cas, len, C, D, N;
	freopen("B-large (1).in", "r", stdin);
	freopen("w.txt", "w", stdout);
	scanf("%d", &cas);
	for(int ri = 1; ri <= cas; ri++){
		printf("Case #%d: ", ri);
		scanf("%d", &C);
		memset(inv, -1, sizeof(inv));
		for(i = 0; i < C; i++){
			scanf("%s", s);
			inv[s[0]-'A'][s[1]-'A'] = inv[s[1]-'A'][s[0]-'A'] = s[2];
		}
		scanf("%d", &D);
		memset(op, 0, sizeof(op));
		for(i = 0; i < D; i++){
			scanf("%s", s);
			op[s[0]-'A'][s[1]-'A'] = op[s[1]-'A'][s[0]-'A'] = 1;
		}
		scanf("%d%s", &N, s);
		char ans[200] = {0};
		len = 0;
		for(i = 0; i < N; i++){
			if(len > 0){
				if(inv[s[i]-'A'][ans[len-1]-'A'] > -1){
					ans[len-1] = inv[s[i]-'A'][ans[len-1]-'A'];
				}else{
					for(j = 0; j <= len - 1; j++){
						if(op[s[i]-'A'][ans[j]-'A'])
							break;
					}
					if(j <= len - 1){
						len = 0;
						ans[len] = 0;
					}else
						ans[len++] = s[i];
				}
			}else
				ans[len++] = s[i];
		}
		//puts(ans);
		putchar('[');
		for(i = 0; i < len; i++){
			if(i) printf(", ");
			putchar(ans[i]);
		}
		puts("]");
	}
}
