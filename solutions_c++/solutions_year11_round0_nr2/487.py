#include <stdio.h>
#include <string.h>
char stk[110],com[128][128];
bool clr[128][128];
int top;
bool needClear(char c){
	for(int i=0;i<top;i++)
		if(clr[c][stk[i]])
			return true;
	return false;
}
int main(int argc, const char *argv[])
{
	int times;
	scanf("%d",&times);
	for(int tm=1;tm<=times;tm++){
		memset(com,0,sizeof(com));
		memset(clr,0,sizeof(clr));
		int N,C,D;
		top=0;
		scanf("%d",&C);
		char s[110];
		for(int i=0;i<C;i++){
			scanf("%s",s);
			com[s[0]][s[1]]=com[s[1]][s[0]]=s[2];
		}
		scanf("%d",&D);
		for(int i=0;i<D;i++){
			scanf("%s",s);
			clr[s[0]][s[1]]=clr[s[1]][s[0]]=true;
		}
		scanf("%d",&N);
		scanf("%s",s);
		for(int i=0;i<N;i++){
			char c=s[i];
			if(top && com[c][stk[top-1]]){
				stk[top-1]=com[c][stk[top-1]];
			}else{
				if(needClear(c))top=0;
				else stk[top++]=c;
			}
		}
		printf("Case #%d: [",tm);
		for(int i=0;i<top;i++){
			if(i)printf(", ");
			printf("%c",stk[i]);
		}
		printf("]\n");
	}
	return 0;
}
