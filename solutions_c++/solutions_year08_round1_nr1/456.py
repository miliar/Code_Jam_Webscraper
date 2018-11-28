#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <string>
#include <numeric>
#include <functional>
#include <cstdlib>
#include <cmath>
#include <memory.h>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for( int t = 1; t <= T; ++t )
    {
        int n;
        cin >> n;
        vector<int> a(n);
        vector<int> b(n);
        for( int i = 0; i != n; ++i )
            cin >> a[i];
        for( int i = 0; i != n; ++i )
            cin >> b[i];
        sort(a.begin(), a.end());
        int mn = 1<<29;
        do
        {
            int x = inner_product(a.begin(), a.end(), b.begin(), 0);
            mn = min(mn, x);
        } while( next_permutation(a.begin(), a.end()) );
        cout << "Case #" << t << ": " << mn << endl;
    }
	return 0;
}

