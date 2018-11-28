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

int a[200];

int main()
{
    freopen(TestCaseName ".in", "r", stdin);
    freopen(TestCaseName ".out", "w", stdout);
    int testCaseCount;
    scanf("%d", &testCaseCount);
    for (int testCase = 0; testCase < testCaseCount; testCase++) {
        printf("Case #%d: ", testCase + 1);
        int n, surp, p;
        scanf("%d%d%d", &n, &surp, &p);
        for (int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        sort(a, a + n);
        int answer = 0;
        for (int i = n - 1; i >= 0; i--)
            if (a[i] < p)
                break;
            else if (a[i] >= 3 * p - 2)
                    answer++;
                else if (a[i] >= 3 * p - 4)
                    if (surp > 0) {
                        surp--;
                        answer++;
                    } else break;
                else break;
        printf("%d", answer);
        
        printf("\n");
    }
    return 0;
}
// END CUT HERE

