
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <string>
using namespace std;

///Fast IO
const int BUFFSIZE = 10240;
char BUFF[BUFFSIZE + 1], *p = BUFF;
int CHAR, SIGN, BYTES = 0;
#define GETCHAR(c) {								\
	if(p-BUFF==BYTES && (BYTES==0 || BYTES==BUFFSIZE)){BYTES=fread(BUFF,1,BUFFSIZE,stdin);p=BUFF;}	\
	if(p-BUFF==BYTES && (BYTES>0 && BYTES<BUFFSIZE)){BUFF[0]=0;p=BUFF;}					\
	c = *p++;										\
}
#define DIGIT(c) (((c) >= '0') && ((c) <= '9'))
#define LETTER(c)(((c) >= 'a' && (c) <= 'z') || ((c) >= 'A' && (c) <= 'Z'))
#define MINUS(c) ((c)== '-')
#define GETNUM(n) {								\
	n = 0;SIGN = 1; do{GETCHAR(CHAR);}while(!(DIGIT(CHAR)|| MINUS(CHAR)));	\
	if(MINUS(CHAR)){SIGN = -1; GETCHAR(CHAR);}		\
	while(DIGIT(CHAR)){n = 10*n + CHAR-'0'; GETCHAR(CHAR);}if(SIGN == -1){n = -n;}\
}
#define GETWORD(s,i) {								\
	i = 0;do{GETCHAR(s[i]);}while(!LETTER(s[i]));	\
	do{GETCHAR(s[++i]);}while(LETTER(s[i]));	\
	s[i]=0;													\
}

///Fast IO ends

char hash[26][26];
int hate[26][26];
char ans[123];

int main() {
#ifndef ONLINE_JUDGE
    freopen("magic", "r", stdin);
    freopen("out", "w", stdout);
#endif
    int T, c, d, n, i, j, k;
    char s[123];

    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        memset(hash, 0, sizeof (hash));
        memset(hate, 0, sizeof (hate));
        scanf("%d", &c);
        for (i = 0; i < c; i++) {
            scanf(" %s", s);
            hash[s[0] - 'A'][s[1] - 'A'] = s[2];
            hash[s[1] - 'A'][s[0] - 'A'] = s[2];
        }
        scanf("%d", &d);
        for (i = 0; i < d; i++) {
            scanf(" %s", s);
            hate[s[0] - 'A'][s[1] - 'A'] = 1;
            hate[s[1] - 'A'][s[0] - 'A'] = 1;
        }
        scanf("%d %s", &n, s);
        int l = -1;
        for (i = 0; i < n;) {
            if (l == -1) ans[++l] = s[i++];
            else {
                if (hash[s[i] - 'A'][ans[l] - 'A']) {
                    s[i] = hash[s[i] - 'A'][ans[l] - 'A'];
                    l--;
                    continue;
                }
                for (j = 0; j <= l; j++)
                    if (hate[s[i] - 'A'][ans[j] - 'A']) {
                        l = -1;
                        i ++;
                        break;
                    }
                if(l == -1) continue;
                ans[++l] = s[i];
                i++;
            }
        }
        printf("Case #%d: [", cas);
        if (l != -1) printf("%c", ans[0]);
        for (i = 1; i <= l; i++) {
            printf(", %c", ans[i]);
        }
        printf("]\n");
    }
    return 0;
}