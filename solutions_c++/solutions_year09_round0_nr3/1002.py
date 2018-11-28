#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

#define REP(i, n) for ( int i = 0; i < (n); i++ ) 
#define FOR(i, a, b) for ( int i = (a); i < (b); i++ ) 

using namespace std;

const char s[] = "welcome to code jam";
const int len = 19;

char line[1000];

void fun(int cs) {
    line[0] = 0;
    scanf(" %[^\n]", line);
//    printf("|%s|\n", line);

    vector<int> cur(20, 0);
    int llen = strlen(line);

    REP(i, llen) {
        REP(j, len) {
            if ( line[i] != s[j] ) continue;
//            printf("%d %d\n", i, j);

            if ( j == 0 ) {
                cur[0] = (cur[0] + 1) % 10000;
            } else {
                cur[j] += cur[j-1];
                cur[j] %= 10000;
            }
        }
    }

    printf("Case #%d: %04d\n", cs, cur[len-1]);
}

int main() {
    int n;
    scanf("%d", &n);

    REP(i, n) {
        fun(i+1);
    }

    return 0;
}
