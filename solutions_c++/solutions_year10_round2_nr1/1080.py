//compiled in vc
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <complex>
/* C++ */
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <ctime>

#define MAXN 10000000
#define MAXM 105
#define MAXP 105

using namespace std;

char exist[MAXN][MAXP];
char create[MAXM][MAXP];

int main() {
    int t, n, m;

    scanf("%d", &t);

    for(int kase = 1; kase <= t; kase++) {
        int ret = 0, cntDir = 0;
        scanf("%d%d", &n, &m);

        for(int i = 0; i < n; i++) {
            scanf("%s", exist[i]);
            int len = strlen(exist[i]);
            exist[i][len++] = '/';
            exist[i][len] = '\0';
        }

        for(int i = 0; i < m; i++) {
            char tmp[MAXM];

            scanf("%s", create[i]);
            int len = strlen(create[i]);
            create[i][len++] = '/';
            create[i][len] = '\0';
            //printf("%s\n", create[i]);

            strcpy(tmp, create[i]);

            char endPt[] = "/";
            while(strlen(tmp) > 0) {
                //printf("%s\n", tmp);

                if(!strcmp(endPt, tmp)) break;

                bool exed = false;
                for(int j = 0; j < n; j++) {
                    if(!strcmp(tmp, exist[j])) {
                        exed = true;
                        break;
                    }
                }

                if(!exed) {
                    strcpy(exist[n++], tmp);
                    ret++;
                }

                int lenTmp = strlen(tmp);
                lenTmp--;
                if(len > 0) lenTmp--;

                for(int j = lenTmp; j >= 0; j--) {
                    if(tmp[j] == '/') break;
                    else tmp[j] = '\0';
                }
            }
        }

        printf("Case #%d: %d\n", kase, ret);
    }
    return 0;
}
