#include <stdio.h>
#include <memory.h>

struct NODE
{
	bool ch[15][26];
}word[1000];

char str[100000][20];
char ch[10000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int Case = 1;
	int i,j,k,p;
	int L,D,N;
	while (scanf("%d%d%d",&L,&D,&N) != EOF) {
		for (i = 0; i < D; i ++) {
			scanf("%s",str[i]);
		}
		memset(word,false,sizeof(word));
		for (i = 0; i < N; i ++) {
			scanf("%s",ch);
			int len = strlen(ch);
			int k = 0;
			for (j = 0; j < len; j ++) {
				if (ch[j] == '(') {
					for (p = j + 1; p < len; p ++) {
						if (ch[p] == ')') break;
						word[i].ch[ k ][ ch[p]-'a' ] = true;
					}
					j = p;
					k ++;
				} else {
					word[i].ch[ k ][ ch[j] - 'a' ] = true;
					k ++;
				}
			}
		}
		

		
		for (j = 0; j < N; j ++) {
			int ans = 0;
			for (i = 0; i < D; i ++) {
				// str[i] == word[j] ??
				for (k = 0; k < L; k ++) {
					if (word[j].ch[k][ str[i][k] - 'a' ]) continue;
					else break;
				}
				//printf("k : %d\n",k);
				if (k < L) continue;
				else {
					ans ++;
				}
			}
			printf("Case #%d: %d\n",Case ++,ans);
			
		}
		
	}
	return 0;
}
