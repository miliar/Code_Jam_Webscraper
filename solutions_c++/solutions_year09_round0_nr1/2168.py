#include <stdio.h>
#include <string.h>

int L,D,N;
struct node {
	char s[30];
}goal[5010];

int token[510][30],len;
char jizz[50000];

int main() {
	int i,j,c=0,tk,pre,counter;
	
	scanf("%d%d%d",&L,&D,&N);
	for(i=0;i<D;i++)
		scanf("%s",goal[i].s);
	while(N--) {
		memset(token,0,sizeof(token));
		scanf("%s",jizz);
		len = strlen(jizz);
		printf("Case #%d: ",++c);
		i = tk = pre = 0;
		while(1) {
			if(tk >= L)	break;
			for(i=pre;i<len && jizz[i] != '(';i++);
			for(j=pre;j<i;j++)
				token[tk++][jizz[j]-'a']++;
			pre = i+1;
			if(jizz[i] == '(') {
				for(i=pre;i<len && jizz[i] != ')';i++);
				for(j=pre;j<i;j++)
					token[tk][jizz[j]-'a']++;
				tk++;
				pre = i+1;
			}
		}
		counter = 0;
		for(i=0;i<D;i++) {
			for(j=0;j<L && token[j][goal[i].s[j]-'a'];j++);
			if(j >= L)	counter++;
		}
		printf("%d\n",counter);
	}
	
	return 0;
}
