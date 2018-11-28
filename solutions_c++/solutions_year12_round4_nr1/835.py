#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <complex>

using namespace std;

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;

const int N_MAX = 10500;
int d[N_MAX], l[N_MAX];
int x[N_MAX];

int main()
{
    int nTests;
    cin >> nTests;


    for (int test = 0; test < nTests; ++test)
    {
        int n;
        cin >> n;
        
        for (int i = 0; i < n; ++i)
        {
            cin >> d[i] >> l[i];
            x[i] = -1;
        }

        x[0] = d[0];

        int dist;
        cin >> dist;        
        bool ok = false;

        for (int i = 0; i < n; ++i)
        {
            if (x[i] == -1) continue;
            if (dist - d[i] <= x[i]) ok = true;

            for (int j = i + 1; j < n; ++j)
                if (x[i] >= (d[j] - d[i]))
                {
                    int nv = min(d[j] - d[i], l[j]);
                    if (x[j] == -1 || x[j] < nv)
                        x[j] = nv;
                }
        }

        cout << "Case #" << test + 1 << ": " << (ok ? "YES" : "NO") << '\n';
    }
    return 0;
}
