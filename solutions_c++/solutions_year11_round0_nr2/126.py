#include <stdio.h>
#include <string.h>

char C[26][26],D[26][26];
char st[128],res[128],cnt[26];
char combine(char a,char b){
	return C[a-'A'][b-'A'];
}
bool opposed(char a,char b){
	return D[a-'A'][b-'A'];
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,N;
	scanf("%d",&T);
	for (int t = 1;t <= T;t++){
		scanf("%d",&N);
		memset(C,0,sizeof(C));
		memset(D,0,sizeof(D));
		for (int i = 1;i <= N;i++){
			scanf("%s",st);
			C[st[0]-'A'][st[1]-'A'] = 
			C[st[1]-'A'][st[0]-'A'] = st[2];
		}
		scanf("%d",&N);
		for (int i = 1;i <= N;i++){
			scanf("%s",st);
			D[st[0]-'A'][st[1]-'A'] = 
			D[st[1]-'A'][st[0]-'A'] = true;
		}
		scanf("%d%s",&N,st);
		int rLen = 0;
		for (int i = 0;st[i];i++){
			if (rLen > 0){
				char c = combine(res[rLen-1],st[i]);
				if (c > 0){
					res[rLen-1] = c;
					continue;
				}
				int j = 0;
				for (;j < rLen;j++)
					if (opposed(res[j],st[i]))
						break;
				if (j < rLen){
					rLen = 0;
					continue;
				}
			}
			res[rLen++] = st[i];
		}
		printf("Case #%d: [",t);
		for (int i = 0;i < rLen;i++){
			if (i > 0)
				putchar(','),putchar(' ');
			putchar(res[i]);
		}
		putchar(']');
		putchar('\n');
	}
	//while(1);
	return 0;
}
