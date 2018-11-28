#include<stdio.h>
#include<stdlib.h>
const char *originalC = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
const char *newC      = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
char table[127];
int count[127];
char input[10240];
int main(){
	table['z'] = 'q';
	table['q'] = 'z';
	for(int i=0;originalC[i] != '\0';i++){
		table[originalC[i]] = newC[i];
	}
	int T;
	scanf("%d%*c",&T);
	for(int i=0;i<T;i++){
		printf("Case #%d: ",i + 1);
		gets(input);
		for(int i=0;input[i] != '\0';i++){
			printf("%c",table[input[i]]);
		}
		printf("\n");
	}
	return 0;
}
