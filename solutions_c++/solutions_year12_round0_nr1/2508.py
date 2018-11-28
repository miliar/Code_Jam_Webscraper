#include <stdio.h>
#include <stdlib.h>
#include <string>

int table[500];

void study(){
	std::string beforetable[3] = 
	{"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
	std::string aftertable[3] =
	{"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up"};
	/*for (int i='a';i<='z';++i)
		table[i] = i;*/
	table['z'] = 'q';
	table['q'] = 'z';
	for (int i=0;i<3;++i){
		for (int j=0;j<(int)beforetable[i].length();++j){
			int before = beforetable[i][j];
			int after = aftertable[i][j];
			table[before] = after;
		}
	}
}

char str[300];

int main(){
	int t,T;
	freopen("a-small.in","rt",stdin);
	freopen("a-small.out","wt",stdout);
	study();
	scanf("%d\n",&T);
	for (t=1;t<=T;++t){
		gets(str);
		for (int i=0;i<strlen(str);++i){
			str[i] = table[str[i]];
		}
		printf("Case #%d: %s\n",t,str);
	}
	return 0;
}