/*
 * Author:heroming
 * File:Tic-Tac-Toe-Tomek.cpp
 * Time:2013/4/13 12:19:13
 */
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define MP make_pair

#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-(x)))
#define SZ(v) ((int)(v).size())
#define FOR(it,a) for (__typeof((a).begin()) it=(a).begin();it!=(a).end();++it)

typedef long long lint;
typedef unsigned long long ulint;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

const int maxn = 6;

int t, v[maxn][maxn], w[maxn];
char c[maxn][maxn];

int solve()
{
        for (int i = 0; i < 4; ++ i)
        {
                memset(w, 0, sizeof(w));
                for (int j = 0; j < 4; ++ j)
                        ++ w[v[i][j]];
                if (w[1] + w[3] == 4)
                        return 1;
                if (w[2] + w[3] == 4)
                        return 2;
        }
        for (int j = 0; j < 4; ++ j)
        {
                memset(w, 0, sizeof(w));
                for (int i = 0; i < 4; ++ i)
                        ++ w[v[i][j]];
                if (w[1] + w[3] == 4)
                        return 1;
                if (w[2] + w[3] == 4)
                        return 2;
        }
        memset(w, 0, sizeof(w));
        for (int i = 0; i < 4; ++ i)
                ++ w[v[i][i]];
        if (w[1] + w[3] == 4)
                return 1;
        if (w[2] + w[3] == 4)
                return 2;
        memset(w, 0, sizeof(w));
        for (int i = 0; i < 4; ++ i)
                ++ w[v[i][3 - i]];
        if (w[1] + w[3] == 4)
                return 1;
        if (w[2] + w[3] == 4)
                return 2;
        memset(w, 0, sizeof(w));
        for (int i = 0; i < 4; ++ i)
                for (int j = 0; j < 4; ++ j)
                        ++ w[v[i][j]];
        if (w[0])
                return 3;
        else
                return 0;
}

int main()
{
        freopen("data.out", "w", stdout);
        scanf("%d", &t);
        for (int l = 1; l <= t; ++ l)
        {
                printf("Case #%d: ", l);
                for (int i = 0; i < 4; ++ i)
                {
                        scanf("%s", c[i]);
                        for (int j = 0; j < 4; ++ j)
                        {
                                if (c[i][j] == 'X')
                                        v[i][j] = 1;
                                else if (c[i][j] == 'O')
                                        v[i][j] = 2;
                                else if (c[i][j] == 'T')
                                        v[i][j] = 3;
                                else
                                        v[i][j] = 0;
                        }
                }
                int e = solve();
                if (e == 0)
                        printf("Draw\n");
                else if (e == 1)
                        printf("X won\n");
                else if (e == 2)
                        printf("O won\n");
                else 
                        printf("Game has not completed\n");
        }
        return 0;
}
