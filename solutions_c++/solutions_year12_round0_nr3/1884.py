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
    int tests;
    cin >> tests;
    int p[10], q[10];
   
     
    for (int test = 1; test <= tests; ++test)
    {
        set<pair<int, int> > was;

        int a, b;
        cin >> a >> b;
        int ans = 0;
        for (int n = a; n <= b; ++n)
        {
            int m = n;
            int len = 0, pw = 10;
            for (;;)
            {
                p[len] = m / pw;
                q[len] = m % pw;
                if (p[len] == 0) break;
                len++; pw *= 10;
            }         
#ifdef DEBUG
            //cerr << "n = " << n << ", len = " << len << '\n';
#endif
            pw /= 100;
            int rpw = 1;
            
            for (int i = len - 1; i >= 0; --i)
            {
                if (pw <= q[i] && q[i] < pw * 10 && rpw <= p[i] && p[i] < rpw * 10)
                {
                    int x = q[i] * rpw * 10 + p[i];
                    if (x > n && x <= b) { was.insert(make_pair(n, x)); ans++; }
                }
                pw /= 10;
                rpw *= 10;
            }
        }
        
        cerr << "Case #" << test << ": " << was.size() << '\n';
        cout << "Case #" << test << ": " << was.size() << '\n';
    }
    return 0;
}
