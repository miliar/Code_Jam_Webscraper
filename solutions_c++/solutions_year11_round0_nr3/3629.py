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

const int N = 15;
int dp[1 << N];
int candy[N];
int main() {
    #ifndef ONLINE_JUDGE
        freopen("candy", "r", stdin);
        freopen("out", "w", stdout);
    #endif
    int T, n, i, j, one, zero, sum;
    scanf("%d", &T);
    for( int cas = 1; cas <= T; cas ++){
        scanf("%d", &n);
        sum = 0;
        for(i = 0; i < n; i ++){
            scanf("%d", candy + i);
            sum += candy[i];
        }
        int top = 1 << n;
        int ans, num;
        ans = -1;
        for( i = 1; i < top - 1; i ++){
            one = zero = num = 0;
            for( j = 0; j < n; j ++){
                if((i >> j) & 1) {
                    one ^= candy[j];
                    num += candy[j];
                }else {
                    zero ^= candy[j];
                }
            }
            if(one == zero && num > ans) {
                ans = num;
            }
        }
        printf("Case #%d: ", cas);
        if(ans == -1) {
            puts("NO");
        }else printf("%d\n", ans);
    }
    return 0;
}
