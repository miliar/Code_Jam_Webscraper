#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

int main(void) { 
    static const char *needle = "welcome to code jam";
    int LEN = strlen(needle);

    int CASES; scanf("%d\n", &CASES);
    for ( int tt=1; tt<=CASES; ++tt ) { // caret here
        int cnt[LEN+1];
        fill(cnt, cnt+LEN+1, 0); cnt[0] = 1;

        int ch;
        while ( (ch = getchar()) != '\n' ) {
            for ( int i=LEN-1; i>=0; --i ) {
                if ( ch == needle[i] ) {
                    cnt[i+1] += cnt[i];
                    cnt[i+1] %= 10000;
                }
            }
        }
        printf("Case #%d: %04d\n", tt, cnt[LEN]);
    }

    return 0;
} 
