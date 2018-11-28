#include <cstdio>
#include <cstring>

const char gs[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
const char es[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char map[30];

int main(){
	for (int i = 0; i < strlen(gs); i++)
		if (gs[i] != ' ')
			map[gs[i] - 'a'] = es[i];
	map['q' - 'a'] = 'z';
	map['z' - 'a'] = 'q';
	
	int n;
	char tmp;
	scanf("%d", &n); fgetc(stdin);
	
	for (int i = 0; i < n; i++){
		printf("Case #%d: ", i + 1);
		
		tmp = fgetc(stdin);
		while (tmp != '\n'){
			printf("%c", (tmp == ' ')?(' '):(map[tmp - 'a']));
			tmp = fgetc(stdin);
		}
		
		printf("\n");
	} 
}
