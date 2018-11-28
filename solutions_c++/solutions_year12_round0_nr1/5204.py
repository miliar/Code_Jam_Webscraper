#include <stdio.h>
#include <string.h>

int main() {
    char a[] = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z";
    char b[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q";
    int len = strlen(a);
    char mm[256];
    for(int i = 0; i < len; i++) mm[a[i]] = b[i];
    
    int numT; scanf("%d ", &numT);
    
    char instr[200];
    for(int cno = 1; cno <= numT; cno++) {
    	gets(instr);
    	printf("Case #%d: ", cno);
    	for(int i = 0; instr[i]; i++) putchar(mm[instr[i]]);
    	putchar('\n');
    }
    
    return 0;
}
