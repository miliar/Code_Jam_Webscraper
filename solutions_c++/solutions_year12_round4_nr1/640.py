#include <QtCore/QCoreApplication>
#include <QString>
#include <QList>
#include <QStringList>
#include <QMap>
#include <QDebug>
#include <QFile>
#include <QDataStream>
#include <QTextStream>
#include <QQueue>
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

const int MAX_N = 10000;
int bestL[MAX_N + 1], bestR[MAX_N + 1], lessBestL[MAX_N + 1], lessBestR[MAX_N + 1];
struct Vine {
    int d, l;
} vines[MAX_N + 1];

bool operator <(const Vine &lhs, const Vine &rhs)
{
    return lhs.d < rhs.d;
}

int inside[MAX_N + 1];
int N, D;
QQueue<int> que;



int main()
{
    freopen(TestCaseName ".in", "r", stdin);
    freopen(TestCaseName ".out", "w", stdout);
    int testCaseCount;
    scanf("%d", &testCaseCount);
    for (int testCase = 0; testCase < testCaseCount; testCase++) {
        printf("Case #%d: ", testCase + 1);
        scanf("%d", &N);
        for (int i = 0; i < N; i++)
            scanf("%d%d", &vines[i].d, &vines[i].l);
        scanf("%d", &D);
        sort(vines + 1, vines + N);

        Fill(inside, false);
        inside[0] = true;
        que.clear();
        vines[N].d = D;
        vines[N].l = 0;
        for (int i = 1; i <= N; i++) {
            lessBestL[i] = bestL[i] = i + 1;
            lessBestR[i] = bestR[i] = i - 1;
        }

        lessBestL[0] = lessBestR[0] = 0;
        bestL[0] = 0;
        for (int i = 0; i <= N; i++)
            if (vines[0].d * 2 >= vines[i].d)
                bestR[0] = i;
            else break;
        que.enqueue(0);
        while (!que.empty() && !inside[N]) {
            int h = que.dequeue();
            for (int i = bestL[h]; i < lessBestL[h]; i++) {
                int dis = abs(vines[i].d - vines[h].d);
                int len = min(vines[i].l, dis);
                for (int j = bestL[i] - 1; j > 0; j--)
                    if (abs(vines[j].d - vines[i].d) <= len)
                        bestL[i] = j;
                    else break;
                if (bestL[i] != lessBestL[i] && !inside[i]) {
                    que.enqueue(i);
                    inside[i] = true;
                }
            }
            lessBestL[h] = bestL[h];

            for (int i = lessBestR[h] + 1; i <= bestR[h]; i++) {
                int dis = abs(vines[i].d - vines[h].d);
                int len = min(vines[i].l, dis);
                for (int j = bestR[i] + 1; j <= N; j++)
                    if (abs(vines[j].d - vines[i].d) <= len)
                        bestR[i] = j;
                    else break;
                if (bestR[i] != lessBestR[i] && !inside[i]) {
                    que.enqueue(i);
                    inside[i] = true;
                }
            }
            lessBestR[h] = bestR[h];

            inside[h] = false;
        }

        if (inside[N])
            printf("YES");
        else printf("NO");
        printf("\n");
    }
    return 0;
}
// END CUT HERE

