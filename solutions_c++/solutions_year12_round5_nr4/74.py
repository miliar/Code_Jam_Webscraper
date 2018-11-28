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
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
using namespace std;

char buf[1 << 10];
int n;

const char MAGIC[] = "oi_eas_tbg";

int G[36][36];

int decode(char ch) 
{
    if (ch <= '9')
        return ch - '0' + 26;
    return ch - 'a';
}

int F[36];

void clearF()
{
    memset(F, -1, sizeof(F));
}

int getF(int a)
{
    return F[a] == -1 ? a : (F[a] = getF(F[a]));
}

bool mergeF(int a, int b)
{
    a = getF(a);
    b = getF(b);
    if (a == b)
        return false;
    F[a] = b;
    return true;
}

bool appeared[36];
int ind[36];
int oud[36];

int main()
{
    int tests;
    scanf("%d", &tests);
    for (int cas = 1; cas <= tests; cas++) {
        scanf("%*d");
        scanf("%s", buf);
        n = strlen(buf);
        memset(G, 0, sizeof(G));
        memset(appeared, false, sizeof(appeared));
        clearF();
        memset(ind, 0, sizeof(ind));
        memset(oud, 0, sizeof(oud));
        for (int i = 0; i + 1 < n; i++) {
            char ch1 = buf[i];
            char ch2 = buf[i + 1];
            char ch1b = ch1;
            char ch2b = ch2;
            for (int i = 0; i < 10; i++) {
                if (MAGIC[i] == ch1) {
                    ch1b = '0' + i;
                }
                if (MAGIC[i] == ch2) {
                    ch2b = '0' + i;
                }
            }
            appeared[decode(ch1)] = true;
            appeared[decode(ch2)] = true;
            appeared[decode(ch1b)] = true;
            appeared[decode(ch2b)] = true;
            G[decode(ch1)][decode(ch2)] = 1;
            G[decode(ch1b)][decode(ch2)] = 1;
            G[decode(ch1)][decode(ch2b)] = 1;
            G[decode(ch1b)][decode(ch2b)] = 1;
        }
        int comps = 0;
        for (int i = 0; i < 36; i++)
            if (appeared[i])
                comps ++;
        int edges = 0;
        for (int i = 0; i < 36; i++) {
            for (int j = 0; j < 36; j++)
                if (G[i][j]) {
                    ind[i] ++;
                    oud[j] ++;
                    edges ++;
                    if (mergeF(i, j))
                        comps --;
                }
        }
        int diff = 0;
        for (int i = 0; i < 36; i++)
            diff += abs(ind[i] - oud[i]);
        diff /= 2;
        if (diff > 0)
            diff --;
        printf("Case #%d: %d\n", cas, edges + max(diff, comps - 1) + 1);
    }
}

