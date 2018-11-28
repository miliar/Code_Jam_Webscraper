#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define maxn 180
int C,D,N,map[maxn][maxn],del[maxn][maxn];
char st[maxn];
int main(){
	int i,j,k,p,len,T,zu,flag,top,tem;
	char st[maxn],stack[maxn];
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d", &T);
	for (zu = 1; zu <= T; zu++){
		memset(map,0,sizeof(map));
		memset(del,0,sizeof(del));
		scanf("%d", &C);
		for (i = 1; i <= C; i++){
			scanf("%3s",st);
			map[st[0]][st[1]] = st[2];
			map[st[1]][st[0]] = st[2];
		}
		scanf("%d", &D);
		for (i = 1; i <= D; i++){
			scanf("%2s",st);
			del[st[0]][st[1]] = 1;
			del[st[1]][st[0]] = 1;
		}
		scanf("%d", &N);
		scanf("%s", st);
		stack[1] = st[0]; top = 1;
		for (i = 1; i < N; i++){
			stack[++top] = st[i];
			while (top > 1 && map[stack[top-1]][stack[top]]){
				tem = map[stack[top-1]][stack[top]];
				stack[--top] = tem ;
			}
			flag = 0;
			for (j = 1; j < top; j++)
				if (del[stack[j]][stack[top]]) flag = j;
			if (flag) top = 0;
			
		}
		printf("Case #%d: [",zu);
		if (top >= 1) {
		for (i = 1; i < top; i++)
			printf("%c, ",stack[i]);
		printf("%c]\n",stack[top]);
		}else 
		printf("]\n");
	}
	return 0;
}