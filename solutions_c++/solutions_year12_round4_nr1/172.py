#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <cassert>
using namespace std;

int n;
int t;

int d[10000];
int l[10000];

void leggi ()
{
    cin >> n;
    for (int i = 0; i < n; i += 1)
    {
        cin >> d[i] >> l[i];
    }
    cin >> t;
}

int m[10000];

bool elabora ()
{
    memset(m, -1, sizeof(m));

    assert(d[0] <= l[0]);

    m[0] = d[0];

    for (int i = 0; i < n; i += 1)
    {
//        cout << "Got to vine " << i << " with a swing of " << m[i] << endl;
        if (d[i] + m[i] >= t)
        {
            return true;
        }

        for (int j = i+1; j < n; j += 1)
        {
            if (d[i] + m[i] >= d[j])
            {
                m[j] = max(m[j], min(l[j], d[j] - d[i]));
            }
        }
    }

    return false;
}

int main ()
{
    int tc;
    cin >> tc;
    for (int i = 0; i < tc; i += 1)
    {
        cout << "Case #" << i+1 << ": ";
        leggi();
        cout << (elabora() ? "YES" : "NO") << endl;
    }
}
