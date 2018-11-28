#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <set>
#include <vector>
using namespace std;

int L, D, N;
set<char> s[30];
char buf[1000000];
char list[6000][30];
char path[30];


int main()
{
    int cn;
    int len, cnt;
    int i, j, k;
    char ch;
    scanf("%d%d%d", &L, &D, &N);
    for (i = 0; i < D; i++) {
        scanf("%s", list[i]);
    }
    for (cn = 1; cn <= N; cn++) {
        scanf("%s", buf);
        len = strlen(buf);
        for (i = 0; i < 30; i++) {
            s[i].clear();
        }
        i = 0;
        j = 0;
        while (i < len) {
            ch = buf[i];
            if (ch >= 'a' && ch <= 'z') {
                s[j].insert(ch);
                i++;
                j++;
                continue;
            }
            for ( ; buf[i] != ')'; i++) {
                if (buf[i] >= 'a' && buf[i] <= 'z')
                    s[j].insert(buf[i]);
            }
            i++;
            j++;
        }
        cnt = 0;
        for (i = 0; i < D; i++) {
            for (j = 0; j < L; j++) {
                if (s[j].find(list[i][j]) == s[j].end())
                    break;
            }
            if (j == L)
                cnt++;
        }
        printf("Case #%d: %d\n", cn, cnt);
    }
    return 0;
}
