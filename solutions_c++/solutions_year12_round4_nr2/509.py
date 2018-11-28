#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <cstring>
#include <cstdio>
#include <time.h>
#include <cstdlib>

using namespace std;

int N, W, L;
double ans[2][1001];
double r[1001];

bool f(int k)
{
    if (k == N) return true;
    for (int c = 0; c < 1000; ++c)
    {
        ans[0][k] = (double)W * ((double)(rand()*rand())/ ((double)RAND_MAX*(double)RAND_MAX));
        ans[1][k] = (double)L * ((double)(rand()*rand())/ ((double)RAND_MAX*(double)RAND_MAX));
        bool good = true;
        for (int j = 0; j < k; ++j)
        {
            if (((ans[0][j] - ans[0][k])*(ans[0][j] - ans[0][k]) + (ans[1][j] - ans[1][k])*(ans[1][j] - ans[1][k]) - 1E-8) < ((r[j] + r[k]) * (r[j] + r[k])))
            {
                good = false;
                break;
            }
        }
        if (good && f (k + 1)) return true;
    }
    return false;
}



int main()
{
    int T;
    cin >> T;
    srand ( time(NULL) );
    for (int t = 1; t <= T; ++t)
    {
        cin >> N >> W >> L;
        for (int i = 0; i < N; ++i) cin >> r[i];
        f(0);
        cout << "Case #" << t <<":";
        for (int i = 0; i < N; ++i)printf(" %.2lf %.2lf", ans[0][i], ans[1][i]);
        cout << endl;
    }
    return 0;
}