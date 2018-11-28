#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

typedef long long li;
typedef long double ld;

using namespace std;

int main(int argc, char* argv[])
{
    int testcount;
    cin >> testcount;
    forn(test, testcount)
    {
        int n, s, p;
        cin >> n;
        cin >> s;
        cin >> p;
        int result = 0;
        forn(i, n)
        {
            int x;
            cin >> x;
            bool has = false;
            forn(a, 11)
                forn(b, 11)
                    forn(c, 11)
                        if (abs(a - b) < 2 && abs(a - c) < 2 && abs(b - c) < 2 && a + b + c == x)
                        {
                            if (max(a, max(b, c)) >= p)
                                has = true;
                        }
            if (has)
            {
                result++;
                continue;
            }

            forn(a, 11)
                forn(b, 11)
                    forn(c, 11)
                        if (abs(a - b) <= 2 && abs(a - c) <= 2 && abs(b - c) <= 2 && a + b + c == x)
                        {
                            if (max(a, max(b, c)) >= p)
                                has = true;
                        }

            if (has && s > 0)
            {
                result++;
                s--;
            }
        }
        cout << "Case #" << test + 1 << ": " << result << endl;
    }

    return 0;
}
