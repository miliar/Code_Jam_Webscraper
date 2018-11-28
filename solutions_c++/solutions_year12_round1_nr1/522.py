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
#define TestCaseName "A-large"

double correct[100000];

int main()
{
    freopen(TestCaseName ".in", "r", stdin);
    freopen(TestCaseName ".out", "w", stdout);
    int testCaseCount;
    scanf("%d", &testCaseCount);
    for (int testCase = 0; testCase < testCaseCount; testCase++) {
        printf("Case #%d: ", testCase + 1);
        int already, all;
        scanf("%d%d", &already, &all);
        for (int i = 0; i < already; i++)
            scanf("%lf", &correct[i]);
        double best = all + 2;
        double p = 1;
        for (int i = 0; i < already; i++) {
            p *= correct[i];
            best = min(best, (already - i - 1 + all - i - 1 + 1) + (all + 1) * (1 - p));
        }

        printf("%lf", best);
        printf("\n");
    }
    return 0;
}
// END CUT HERE

