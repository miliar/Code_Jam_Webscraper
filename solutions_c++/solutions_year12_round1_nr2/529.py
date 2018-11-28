#include <QtCore/QCoreApplication>
#include <QString>
#include <QList>
#include <QStringList>
#include <QMap>
#include <QDebug>
#include <QFile>
#include <QDataStream>
#include <QTextStream>
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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#include <climits>
#define Fill(A, n) memset(A, n, sizeof(A))
using namespace std;
#define TestCaseName "B-large"

struct Level {
    int easy, hard;
    int easied;
} levels[2000];

bool cmp(Level a, Level b)
{
    return a.hard < b.hard;
}

int main()
{
    freopen(TestCaseName ".in", "r", stdin);
    freopen(TestCaseName ".out", "w", stdout);
    int testCaseCount;
    scanf("%d", &testCaseCount);
    for (int testCase = 0; testCase < testCaseCount; testCase++) {
        printf("Case #%d: ", testCase + 1);
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d%d", &levels[i].easy, &levels[i].hard);
            levels[i].easied = false;
        }
        sort(levels, levels + n, cmp);
        int stars = 0, moves = 0;
        for (int i = 0; i < n; i++) {
            bool easied = true;
            while (levels[i].hard > stars) {
                easied = false;
                for (int j = n - 1; j >= i; j--)
                    if (!levels[j].easied && levels[j].easy <= stars) {
                        levels[j].easied = true;
                        stars++;
                        moves++;
                        easied = true;
                        break;
                    }
                if (!easied)
                    break;
            }
            if (!easied) {
                moves = -1;
                break;
            }
            stars++;
            if (!levels[i].easied)
                stars++;
            levels[i].easied = true;
        }
        if (moves == -1)
            printf("Too Bad");
        else printf("%d", moves + n);
        printf("\n");
    }
    return 0;
}
// END CUT HERE

