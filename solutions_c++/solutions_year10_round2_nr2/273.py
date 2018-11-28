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

const double E = 1E-9;

#define forn(i, n) for (int i = 0; i < int(n); i++)

li n, k, b, t;
vector<li> x, v;

int main(int argc, char* argv[])
{
	freopen("B-large.in", "rt", stdin);

	int testCount;
	cin >> testCount;

    forn(tt, testCount)
    {
    	cin >> n >> k >> b >> t;
        x.resize(n);
        v.resize(n);
        forn(i, n)
        	cin >> x[i];
        forn(i, n)
        	cin >> v[i];

        vector<bool> used(n, false);
        vector<int> r;
        int z = 0;
        forn(i, n)
        {
        	if (x[i] + t * v[i] >= b)
            {
            	z++;
                used[i] = true;
                r.push_back(i);
            }
        }

        int result = -1;
        if (z >= k && k > 0)
        {
        	reverse(r.begin(), r.end());
            int from = r[k - 1];
            result = 0; 
            for (int i = from; i < n; i++)
            	for (int j = i + 1; j < n; j++)
                	if (used[i] && !used[j])
                    	result++;
        }

        if (k == 0)
        	result = 0;

        cout << "Case #" << (tt + 1) << ": ";
        if (result == -1)
        	cout << "IMPOSSIBLE";
        else
        	cout << result;
        cout << endl;
    }

    return 0;
}

