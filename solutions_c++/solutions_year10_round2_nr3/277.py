#include <ctime>
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

#define forn(i, n) for (int i = 0; i < int(n); i++)

li M = 100003;

li C[1000][1000];
li z[1000][1000];

int main(int argc, char* argv[])
{
	C[0][0] = 1;
	for (int i = 1; i <= 600; i++)
	{
    	C[i][0] = 1;
        C[i][i] = 1;
        for (int j = 1; j < i; j++)
        	C[i][j] = C[i - 1][j] + C[i - 1][j - 1] % M;
    }

    for (int i = 2; i <= 600; i++)
    	z[i][1] = 1;

    for (int j = 2; j < 600; j++)
    	for (int i = j + 1; i <= 600; i++)
        {
        	for (int t = 1; t < j; t++)
            {
            	z[i][j] = (z[i][j] + z[j][t] * C[i - j - 1][j - t - 1]) % M;
            }
        }

	freopen("C-large.in", "rt", stdin);

	int testCount;
	cin >> testCount;

    forn(tt, testCount)
    {
    	li n;
        cin >> n;

        li result = 0;
        for (int j = 1; j < n; j++)
        	result = (result + z[n][j]) % M;

        cout << "Case #" << (tt + 1) << ": ";
        cout << result % M;
        cout << endl;
    }

    return 0;
}
