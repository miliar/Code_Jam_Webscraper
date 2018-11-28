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
    int testCount;
    cin >> testCount;
    forn(test, testCount)
    {
        int a, b;
        cin >> a >> b;
        stringstream ss;
        ss << a;
        string s;
        ss >> s;
        int len = s.length();

        int mul = 1;
        forn(i, len - 1)
            mul *= 10;

        long long result = 0;

        for (int i = a; i <= b; i++)
        {
            int next = i;
            forn(j, len)
            {
                //cout << next << " ";
                int d = next % 10;
                next /= 10;
                next += d * mul;
                //cout << next << endl;

                if (next > i && next >= a && next <= b)
                    result++;
            }
            assert(next == i);
        }

        cout << "Case #" << test + 1 << ": " << result << endl;
    }
    return 0;
}
