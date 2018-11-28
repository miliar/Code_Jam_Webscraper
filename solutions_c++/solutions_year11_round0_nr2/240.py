#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <string>
#include <iomanip>
#include <sstream>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cassert>
using namespace std;

//BEGIN TEMPLATE HERE
typedef long long int64;

#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))
//END TEMPLATE HERE

const int maxlen = 1 << 20;

bool opp[300][300];
char tr[300][300];
bool in[300][300];
int first[300];
char a[maxlen], s[maxlen];
int C, D, N, top;

int main() {
    freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
    //freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
    //freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
    //freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int caseId = 1; caseId <= T; caseId ++) {
        printf("Case #%d: ", caseId);
        memset(in, 0, sizeof in);
        memset(opp, 0, sizeof opp);
        scanf("%d", &C);
        for (int i = 0; i < C; i ++) {
            char sc[100];
            scanf("%s", sc);
            tr[sc[0]][sc[1]] = sc[2];
            tr[sc[1]][sc[0]] = sc[2];
            in[sc[0]][sc[1]] = in[sc[1]][sc[0]] = true;
        }
        scanf("%d", &D);
        for (int i = 0; i < D; i ++) {
            char sd[100];
            scanf("%s", sd);
            opp[sd[0]][sd[1]] = opp[sd[1]][sd[0]] = true;
        }
        scanf("%d", &N);
        scanf("%s", a);
        int top = 0;
        memset(first, -1, sizeof first);
        for (int i = 0; i < N; i ++) {
            s[++ top] = a[i];
            if (first[s[top]] == -1) {
                first[s[top]] = top;
            }
            while (top >= 2) {
                if (in[s[top - 1]][s[top]]) {
                    if (first[s[top]] == top) first[s[top]] = -1;
                    if (first[s[top - 1]] == top - 1) first[s[top - 1]] = -1;
                    char ch = tr[s[top - 1]][s[top]];
                    top -= 2;
                    s[++ top] = ch; 
                } else {
                    break;
                }
            }
            while (top >= 1) {
                bool find = false;
                for (char f = 'A'; f <= 'Z'; f ++) {
                    if (first[f] != -1 && opp[f][s[top]]) {
                        find = true;
                        break;
                    }
                }
                if (find) {
                    for (int j = 1; j <= top; j ++) {
                        if (first[s[j]] == j) {
                            first[s[j]] = -1;
                        }
                    }
                    top = 0;
                } else {
                    break;
                }
            }
        }
        printf("[");
        for (int i = 1; i + 1 <= top; i ++) printf("%c, ", s[i]);
        if (top >= 1) printf("%c", s[top]);
        printf("]\n");
    }
    return 0;
}

