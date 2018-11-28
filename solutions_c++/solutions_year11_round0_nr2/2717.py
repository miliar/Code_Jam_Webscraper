//*****************
// LAM PHAN VIET **
// Google Code Jam -  Problem B. Magicka
// Time limit:
//********************************
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <deque>
#include <map>
#include <string>
#include <vector>
using namespace std;

#define For(i, a, b) for (int i=a; i<=b; i++)
#define maxN 105
int n;
char s[maxN], Combine[maxN][maxN];
bool Ops[maxN][maxN];
deque<char> List;

void ReadInput() {
    For (i, 'A', 'Z')
        For (j, 'A', 'Z') {
            Combine[i][j] = ' ';
            Ops[i][j] = false;
        }
    int m;
    char tmp[10], u, v;
    scanf("%d", &m);
    while (m--) {
        scanf(" %s", &tmp);
        u = tmp[0]; v = tmp[1];
        Combine[u][v] = Combine[v][u] = tmp[2];
    }
    scanf("%d", &m);
    while (m--) {
        scanf(" %s", &tmp);
        u = tmp[0]; v = tmp[1];
        Ops[u][v] = Ops[v][u] = true;
    }
    scanf("%d", &n);
    scanf(" %s", &s);
    List.clear();
}

void Solve() {
    char u, v;
    For (i, 0, n-1) {
        List.push_back(s[i]);
        int m = List.size();
        u = List[m-1];
        if (m<=1) continue;
        v = List[m-2];
        bool f = false;
        if (Combine[u][v]!=' ') {
            List.pop_back(); List.pop_back();
            List.push_back(Combine[u][v]);
            f = true;
        }
        if (!f) {
            for (int i=m-2; i>=0; i--)
                if (Ops[List[i]][u]) {
                    List.clear();
                    break;
                }
        }
    }
}

main() {
//    freopen("bb.inp", "r", stdin); freopen("bb.out", "w", stdout);
    int Case;
    scanf("%d", &Case);
    For (kk, 1, Case) {
        ReadInput();
        Solve();
        printf("Case #%d: [", kk);
        if (List.size()) printf("%c", List[0]);
        for (int i=1, size=List.size(); i<size; i++)
            printf(", %c", List[i]);
        printf("]\n");
    }
}

/* lamphanviet@gmail.com - 2011 */
