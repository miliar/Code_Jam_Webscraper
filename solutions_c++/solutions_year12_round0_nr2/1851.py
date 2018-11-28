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


int main()
{
    vector<int> mx_s(31, -1), mx_ns(31, -1);
    for (int i = 0; i <= 10; ++i)
        for (int j = i; j <= 10; ++j)
            for (int k = j; k <= 10; ++k)
            {
                int s = i + j + k;
                if (k - i <= 2)
                {
                    if (k - i == 2)
                        mx_s[s] = max(mx_s[s], k);
                    else
                        mx_ns[s] = max(mx_ns[s], k);
                }
            }
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test)
    {
        int n, s, p;
        cin >> n >> s >> p;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) cin >> a[i];
        
        vector<int> fr(s + 1, -1), to(s + 1, -1);
        fr[0] = 0; 
        for (int i = 0; i < n; ++i)
        {
            to.assign(s + 1, -1);
            if (mx_ns[ a[i] ] != -1)
                for (int j = 0; j <= s; ++j)
                    to[j] = fr[j] + (mx_ns[ a[i] ] >= p);
            if (mx_s[ a[i] ] != -1)
                for (int j = 0; j < s; ++j)
                    to[j + 1] = max(to[j + 1], fr[j] + (mx_s[ a[i] ] >= p));
            swap(fr, to);
        }
        cout << "Case #" << test << ": " << fr[s] << '\n';
    }
    return 0;
}
