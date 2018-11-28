#include <QtCore/QCoreApplication>
#include <QString>
#include <QList>
#include <QStringList>
#include <QMap>
#include <QSet>
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
#define TestCaseName "C-large"
const int Bases[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

int getLength(int x)
{
    for (int i = 0; ; i++)
        if (x < Bases[i])
            return i;
}

int main()
{
    freopen(TestCaseName ".in", "r", stdin);
    freopen(TestCaseName ".out", "w", stdout);
    int testCaseCount;
    scanf("%d", &testCaseCount);
    for (int testCase = 0; testCase < testCaseCount; testCase++) {
        printf("Case #%d: ", testCase + 1);
        int A, B;
        scanf("%d%d", &A, &B);
        int L = getLength(A);
        int answer = 0;
        for (int i = A; i <= B; i++) {
            QSet<int> set;
            for (int j = 1; j < L; j++) {
                int x = i / Bases[j] + i % Bases[j] * Bases[L - j];
                if (x >= A && x <= B && i < x && !set.contains(x)) {
                    set.insert(x);
                    answer++;
                    //qDebug() << answer << i << x;
                }
            }
        }
        printf("%d\n", answer);
    }
    return 0;
}
// END CUT HERE

