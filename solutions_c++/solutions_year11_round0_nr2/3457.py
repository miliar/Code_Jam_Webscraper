
#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <map>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);freopen("A-large.out", "w", stdout);

    int T, t;
    int C, D, N;

    char cstr[110], ch;
    char tmp[110], str[110];

    int i, j, cnt;

    map<string, char> hashCOM;
    map<string, char> hashOPP;

    scanf("%d", &T);
    for (t = 1; t <= T; ++t) {
        hashCOM.clear();
        hashOPP.clear();

        scanf("%d", &C);
        for (i = 0; i < C; ++i) {
            scanf("%s", cstr);
            ch = cstr[2];
            cstr[2] = 0;
            hashCOM[cstr] = ch;
            swap(cstr[0],cstr[1]);
            hashCOM[cstr] = ch;
        }

        scanf("%d", &D);
        for (i = 0; i < D; ++i) {
            scanf("%s", cstr);
            ch = cstr[2];
            cstr[2] = 0;
            hashOPP[cstr] = ch;
            swap(cstr[0],cstr[1]);
            hashOPP[cstr] = ch;
        }

        scanf("%d", &N);
        scanf("%s", cstr);

        memset(str, 0, sizeof(str));
        cnt = 0;
        for (i = 0; i < N; ++i) {
            tmp[0] = cstr[i];
            tmp[2] = 0;
            for (j = cnt - 1; j >= 0; --j) {
                tmp[1] = str[j];
                if (j == cnt - 1) {
                    if (hashCOM.find(tmp) != hashCOM.end()) { // com
                        str[j] = hashCOM[tmp];
                        break;
                    }
                }
                if (hashOPP.find(tmp) != hashOPP.end()) {
                    cnt = 0;
                    break;
                }
            }
            if (j < 0) {
                str[cnt] = cstr[i];
                ++cnt;
            }
        }

        printf("Case #%d: [", t);
        for (i = 0; i < cnt; ++i) {
            if (i != 0) printf(", ");
            printf("%c", str[i]);
        }
        printf("]\n");
    }

    return 0;
}
