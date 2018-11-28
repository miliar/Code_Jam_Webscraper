#include <stdio.h>
#include <string.h>

#define Key 37211

typedef char *pchar;

struct{
	int locate;
	pchar str;
} hash[Key];

void Insert(pchar str,int locate){
	int p=1;
	int i;
	for (i=0;str[i];i++)
		p=p*str[i]%Key;
	while (hash[p].locate){
		p++;
		if (p==Key) p=0;
	}
	hash[p].locate=locate;
	hash[p].str=str;
}

int find(pchar str){
	int p=1;
	int i;
	for (i=0;str[i];i++)
		p=p*str[i]%Key;
	while (strcmp(hash[p].str,str)){
		p++;
		if (p==Key) p=0;
	}
	return hash[p].locate;
}

int tests,s,q;
char buf[110][110];
bool used[110];
char str[110];

int main(){

	scanf("%d\n",&tests);
	int ss,i,k,tot,times;
	for (ss=1;ss<=tests;ss++){
		scanf("%d\n",&s);
		memset(hash,0,sizeof hash);
		memset(used,0,sizeof used);
		for (i=1;i<=s;i++){
			gets(buf[i]);
			Insert(buf[i],i);
		}
		scanf("%d\n",&q);
		tot=times=0;
		for (i=1;i<=q;i++){
			gets(str);
			k=find(str);
			if (!used[k]){
				used[k]=true;
				tot++;
				if (tot==s){
					times++;
					memset(used,0,sizeof used);
					used[k]=true;
					tot=1;
				}
			}
		}
		printf("Case #%d: %d\n",ss,times);
	}
}
