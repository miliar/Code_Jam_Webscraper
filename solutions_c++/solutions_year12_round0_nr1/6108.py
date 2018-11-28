#include <stdio.h>
#include <string.h>
#define	MAX	150

char *g1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
char *g2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char *g3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
char *t1 = "our language is impossible to understand";
char *t2 = "there are twenty six factorial possibilities";
char *t3 = "so it is okay if you want to just give up";
char map[26];

void train(char *g, char *t){
	int i;
	for(i=0;g[i]!='\0';i++)
		if(g[i] != ' ')
			map[g[i]-'a'] = t[i];
}
void solve(char *in){
	int i;
	for(i=0;in[i]!='\0';i++){
		if(in[i] != ' ' && in[i] != '\n')
			printf("%c", map[in[i]-'a']);
		else
			printf("%c", in[i]);
	}
}
int main(){
	int i, T;
	char input[MAX];
	train(g1, t1);
	train(g2, t2);
	train(g3, t3);
	map['z'-'a'] = 'q';
	map['q'-'a'] = 'z';
//	for(i=0;i<26;i++)
//		printf("%c -> %c\n", i+'a', map[i]);

	scanf("%d\n", &T);
	for(i=0;i<T;i++){
		fgets(input, MAX, stdin);
		printf("Case #%d: ", i+1);
		solve(input);
//		printf("\n");
	}
	return 0;
}
