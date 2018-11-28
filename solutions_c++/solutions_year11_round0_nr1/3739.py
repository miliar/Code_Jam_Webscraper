#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
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

int ABS(int x) {
    return x > 0 ? x : -x;
}
const int N = 109;
int O[N], B[N], numO[N], numB[N];

int main(int argc, char** argv) {
#ifndef ONLINE_JUDGE
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif

    int T, n, lo, lb, button, i, j, k, step, ans, Ostep, Bstep;
    char robot;
        GETNUM(T);
 //   scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
          GETNUM(n);
        memset( numO, -1, sizeof(numO));
        memset( numB, -1, sizeof(numB));
   //     scanf("%d", &n);
        lo = lb = 1;
        for (i = 1; i <= n; i++) {
               GETCHAR(robot);
               GETNUM(button);
       //     scanf(" %c %d", &robot, &button);
            if (robot == 'O') {
                numO[lo] = i;
                O[lo++] = button;
            } else {
                numB[lb] = i;
                B[lb++] = button;
            }
        }
        O[0] = B[0] = 1;
        i = j = 1;
        Ostep = Bstep = 0;
        ans = 0;
        for (k = 1; k <= n; k++) {
            if (numO[i] == k) {
                step = ABS(O[i] - O[i - 1]);
                if (Ostep >= step) {
                    Ostep = 0;
                    Bstep = 1;
                    ans++;
                } else {
                    if (Ostep != 0) {
                        step -= Ostep;
                        Ostep = 0;
                        Bstep = step + 1;
                        ans += step + 1;
                    } else {
                        ans += step + 1;
                        Bstep += step + 1;
                    }
                }
                i++;
            } else {
                step = ABS(B[j] - B[j - 1]);
                if (Bstep >= step) {
                    Ostep = 1;
                    Bstep = 0;
                    ans++;
                } else {
                    if (Bstep != 0) {
                        step -= Bstep;
                        Bstep = 0;
                        Ostep = step + 1;
                        ans += step + 1;
                    }else {
                        ans += step + 1;
                        Ostep += step + 1;
                    }
                }
                j++;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return (EXIT_SUCCESS);
}

