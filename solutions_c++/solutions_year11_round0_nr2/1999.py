#include<cstdio>
#include<cstring>
int T;
int com[26][26], de[26][26];
int N, C, D, lst[101], cnt;
char cmd[101];
void out(){
	putchar('[');
	if(cnt)putchar(lst[0] + 'A');
	for(int i = 1; i < cnt; i++)
	    printf(", %c", lst[i] + 'A');
	putchar(']');
	putchar('\n');
}
int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 0; t < T; t++){
		cnt = 0;
		memset(com, -1, sizeof(com));
		memset(de, 0, sizeof(de));
		scanf("%d", &C);
		for(int i = 0; i < C; i++){
			scanf("%s", cmd);
			int I = cmd[0] - 'A', J = cmd[1] - 'A';
			com[I][J] = com[J][I] = cmd[2] - 'A';
		}
		scanf("%d", &D);
		for(int i = 0; i < D; i++){
			scanf("%s", cmd);
			int I = cmd[0] - 'A', J = cmd[1] - 'A';
			de[I][J] = de[J][I] = 1;
		}
		scanf("%d", &N);
		scanf("%s", cmd);
		for(int i = 0; i < N; i++){
			if(!cnt){
				lst[cnt++] = cmd[i] - 'A';
			}else{
				if(com[lst[cnt - 1]][cmd[i] - 'A'] != -1){
					lst[cnt - 1] = com[lst[cnt - 1]][cmd[i] - 'A'];
				}else{
					bool flg = false;
					for(int j = 0; j < cnt && !flg; j++)
					    if(de[lst[j]][cmd[i] - 'A'])flg = true;
					if(flg)cnt = 0;
					else{
						lst[cnt++] = cmd[i] - 'A';
					}
				}
			}
		}
		printf("Case #%d: ", t + 1);
		out();
	}
}
