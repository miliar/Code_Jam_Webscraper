#include <ctime>
#include <string.h>
#include <cstdio>
#include <queue>
#include <cassert>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <cassert>
#include <utility>

using namespace std;

typedef long long li;
typedef long double ld;

const int INF = 1000000000;
const ld EPS = 1E-9;

#define forn(i, n) for (int i = 0; i < int(n); i++)

int z[500][500];
int n, m;

void readdata()
{
	int r;
	cin >> r;
    n = 0; m = 0;

    memset(z, 0, sizeof(z));

    forn(i, r)
    {
    	int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        for (int a = x1; a <= x2; a++)
        for (int b = y1; b <= y2; b++)
        z[a][b] = 1;
        n = max(n, x2 + 1);
        m = max(m, y2 + 1);
    }

}

bool has()
{
	bool ok = false;

	forn(i, n)
    	forn(j, m)
        	if (z[i][j])
            	ok = true;

    if (!ok)
    	return false;

    forn(i, n)
    	forn(j, m)
        {
            if (z[i][j] > 0)
            {
            	if (z[i - 1][j] <= 0 && z[i][j - 1] <= 0)
                	z[i][j] = 2;
            }
        }

    forn(i, n)
    	forn(j, m)
        {
            if (i > 0 && j > 0)
            {
            	if (z[i - 1][j] > 0 && z[i][j - 1] > 0 && z[i][j] == 0)
                	z[i][j] = -1;
            }
        }

    forn(i, n)
    	forn(j, m)
        {
        	if (z[i][j] == 2)
            	z[i][j] = 0;
            if (z[i][j] == -1)
            	z[i][j] = 1;
        }
}

void solve()
{
	int ans = 0;
	while (has()) ans++;
    cout << ans << endl;
}

int main(int argc, char* argv[])
{
	freopen("C-small-attempt0.in", "rt", stdin);

	int testCount;
	cin >> testCount;

    int minTest = 1;
    int maxTest = testCount;

    if (argc == 3)
    {
    	minTest = atoi(argv[1]);
    	maxTest = atoi(argv[2]);
    }

    for (int tt = 1; tt <= testCount; tt++)
    {
    	readdata();

        if (minTest <= tt && tt <= maxTest)
        {
	        cout << "Case #" << tt << ": ";
            int now = clock();
            solve();
            int duration = clock() - now;
            cerr << "[INFO]: Test#" << tt << " takes " << duration << "ms" << endl;
        }
    }

    return 0;
}
