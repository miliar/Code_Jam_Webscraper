#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>

using namespace std;


char tab[256];

char W1[]="ejp mysljylc kd kxveddknmc re jsicpdrysi\nrbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd\nde kr kd eoya kw aej tysr re ujdr lkgc jv\ny zqee";
char W2[]="our language is impossible to understand\nthere are twenty six factorial possibilities\nso it is okay if you want to just give up\na qzoo";

int main() {
    for (int i=0; i<255; i++) tab[i]='/';
    for ( int i = 0; W1[i]; i++) tab[W1[i]]=W2[i];
	
	char W[10000];
	int T;
    scanf("%d", &T);
        gets(W);
    for (int t=1; t<=T; t++) {
        gets(W);
		for (int i=0; W[i]; i++) W[i]=tab[W[i]];
        printf("Case #%d: %s\n", t, W);
    }
    return 0;
}

