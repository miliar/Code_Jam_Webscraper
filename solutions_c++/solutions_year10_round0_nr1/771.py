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

int main(int argc, char* argv[])
{
	freopen("A-large.in", "rt", stdin);
    
	int t;
	cin >> t;

    forn(tt, t)
    {
    	li n, k;
    	cin >> n >> k;

        li first = (1LL << n) - 1;
        li gap = (1LL << n);

        bool ok = false;

        if (k >= first)
        {
        	k -= first;
            if (k % gap == 0)
            	ok = true;
        }

        cout << "Case #" << (tt + 1) << ": " << (ok ? "ON" : "OFF") << endl;
    }

    return 0;
}
