#include <QtCore/QCoreApplication>
#include <QString>
#include <QList>
#include <QStringList>
#include <QMap>
#include <QDebug>
#include <QFile>
#include <QDataStream>
#include <QTextStream>
#include <QStack>
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
#define TestCaseName "C-small-attempt0"

const int MAX_N = 2000, MAX_HEIGHT = 1000000000;
int N;
int x[MAX_N + 1];
int heights[MAX_N + 1];

struct Peak {
    int number, gradient;
    Peak (int n = 0, int g = 0) {
        number = n;
        gradient = g;
    }
};
int gradients[MAX_N];

QStack<Peak> peaks;

int main()
{
    freopen(TestCaseName ".in", "r", stdin);
    freopen(TestCaseName ".out", "w", stdout);
    int testCaseCount;
    scanf("%d", &testCaseCount);
    for (int testCase = 0; testCase < testCaseCount; testCase++) {
        printf("Case #%d:", testCase + 1);
        scanf("%d", &N);
        for (int i = 0; i < N - 1; i++) {
            scanf("%d", &x[i]);
            x[i]--;
        }
        heights[N - 1] = MAX_HEIGHT;
        peaks.clear();
        peaks.push(Peak(N - 1, 0));


        heights[0] = -1;
        for (int i = N - 2; i >= 0; i--) {
            while (peaks.top().number < x[i])
                peaks.pop();
            if (peaks.top().number == x[i]) {
                Peak t = peaks.top();
                heights[i] = heights[t.number] - (t.number - i) * t.gradient;
                peaks.push(Peak(i, t.gradient + 1));
            } else break;
        }

        if (heights[0] == -1) {
            printf(" Impossible\n");
            continue;
        }

        Fill(gradients, 0);
        for (int i = 1; i < N; i++) {
            int maxGradient = 0;
            for (int j = 0; j < i; j++)
                if (x[j] == i)
                    maxGradient++;
            gradients[i] = maxGradient;
        }
        for (int i = N - 1; i >= 0; i--) {
            int maxGradient = gradients[i];
            for (int j = 0; j < i; j++)
                if (x[j] == i)
                    gradients[j] = maxGradient++;
        }
        heights[N - 1] = MAX_HEIGHT;
        for (int i = N - 2; i >= 0; i--)
            heights[i] = heights[x[i]] - gradients[i] * (x[i] - i);
        for (int i = 0; i < N; i++)
            printf(" %d", heights[i]);
        printf("\n");
    }
    return 0;
}
// END CUT HERE

