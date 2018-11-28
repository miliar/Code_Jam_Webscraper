#include <stdio.h>
#include <algorithm>

using namespace std;

int main(void) {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-small-attempt1.out", "w", stdout);

	char table[333];
	char *q[] = { "ejp mysljylc kd kxveddknmc re jsicpdrysi",
		"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
		"de kr kd eoya kw aej tysr re ujdr lkgc jv",
		//"y n f i c w l b k u o m x s e v z p d r j g a t h a q",
	};
	char *a[] = {
		"our language is impossible to understand",
		"there are twenty six factorial possibilities",
		"so it is okay if you want to just give up",
		//"a b c d e f g h i j k l m n o p q r s t u v w x y z",
	};

	for(int i=0;i<sizeof(q)/sizeof(char*);i++) for(int j=0;j<strlen(q[i]);j++) table[q[i][j]] = a[i][j]; 
	table[' ']= ' ';
	table['q']='z';
	table['z']='q';

	//table[113]='z';
	int T; scanf("%d\n", &T);

	for(int tc=1; tc<=T; tc++) {
		printf("Case #%d: ", tc);
		char t[222];
		gets(t);
		for(int i=0;i<strlen(t);i++) printf("%c", table[t[i]]);
		printf("\n");
	}



	return 0;
}