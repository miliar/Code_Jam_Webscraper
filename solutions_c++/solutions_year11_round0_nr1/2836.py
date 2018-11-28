//*****************
// LAM PHAN VIET **
// Google Code Jam - Problem A. Bot Trust
// Time limit:
//********************************
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <queue>
using namespace std;

#define For(i, a, b) for (int i=a; i<=b; i++)
#define maxN 105
int n, Pos[2];
queue<int> Robot[2], Next;

int Solve() {
    int SumTime = 0;
    Pos[0] = Pos[1] = 1;
    while (!Next.empty()) {
        int r = Next.front(); Next.pop();
        int move = abs(Pos[r] - Robot[r].front()); // move to position Robot[r]
        move++;     // push button
        SumTime += move;
        Pos[r] = Robot[r].front();
        Robot[r].pop();
        
        int r2 = 1-r;
        if (Robot[r2].empty()) continue;
        int move2 = abs(Pos[r2] - Robot[r2].front());
        if (move>=move2) Pos[r2] = Robot[r2].front();
        else {
            int u = Pos[r2], v = Robot[r2].front();
            if (u<v) Pos[r2] += move;
            else Pos[r2] -= move;
        }
    }
    return SumTime;
}

main() {
//    freopen("a.inp", "r", stdin); freopen("a.out", "w", stdout);
    int Case, k;
    char ch;
    scanf("%d", &Case);
    For (kk, 1, Case) {
        scanf("%d", &n);
        Robot[0] = Robot[1] = Next = queue<int>();
        For (i, 1, n) {
            scanf(" %c %d", &ch, &k);
            if (ch=='O') {
                Robot[0].push(k);
                Next.push(0);
            }
            else {
                Robot[1].push(k);
                Next.push(1);
            }
        }
        printf("Case #%d: %d\n", kk, Solve());
    }
}

/* lamphanviet@gmail.com - 2011 */
