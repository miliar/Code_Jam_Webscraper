#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<memory.h>

char pattern[16][26];
char words[5100][16];

int main() {
    freopen("A-large.in","r", stdin);
    freopen("A-large-res.out", "w", stdout);
    int L,D,N;
    scanf("%d%d%d", &L, &D, &N);
    for (int i = 0 ; i < D; ++i) scanf("%s", words[i]);
    for (int i = 0 ; i < N; ++i) {
        
        // read pattern
        char line[1024];
        for (int a = 0 ; a < 16; ++a) for (int b = 0 ; b < 26 ; ++b) pattern[a][b] = 0;
        scanf("%s",line);
        
        // parse pattern
        char *p = line;
        int cnt = 0;
        while (*p != 0){
            if (*p != '(' && *p != ')') {
                pattern[cnt][*p-'a'] = 1;
                ++p;
            }
            else if (*p == '(') {
                ++p;
                while (*p != ')') {
                    pattern[cnt][*p-'a'] = 1;
                    ++p;
                }
                ++p;
            }
            ++cnt;
        }
        
        // match pattern
        int res = 0;
        for (int j = 0; j < D; ++j) {
            bool flag = true;
            for (int k = 0 ; k < L ; ++k) {
                if (pattern[k][words[j][k]-'a'] == 0){
                    flag = false;
                    break;
                }
            }
            res += (flag?1:0);
        }
        printf("Case #%d: %d\n", i+1, res);
    }
    
    return 0;
}
