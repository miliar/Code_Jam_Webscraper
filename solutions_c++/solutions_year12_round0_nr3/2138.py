#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <math.h>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
using namespace std;

typedef long long ll;
#define pb push_back
#define mp make_pair
const long long inf = 1000 * 1000 * 1000, max_a = 2000000 + 41;
vector <long long> g[max_a];

long long to_int (string& s) {
    long long res = 0;
    for (long long i = 0; i < s.length(); i++)
        res = res * 10 + s[i] - '0';
    return res;
}

string to_str (long long x) {
       string res = "";
       while (x > 0)
             res += (x % 10 + '0'), x /= 10;
       reverse(res.begin(), res.end());
       return res;
}

long long x[41], sz = 0;

long long min_shift(long long i)
{
    string s = to_str(i);
    long long n = s.length();
    sz = 0;
    for (long long i = 0; i < n; i++) {
        if (s[0] != '0') x[sz++] = to_int(s);
        char temp = s[0];
        for (long long j = 0; j < n - 1; j++)
            s[j] = s[j + 1];
        s[n - 1] = temp;
    }
    long long res = inf;
    for (long long i = 0; i < sz; i++)
        res = min(res, x[i]);
    return res;
}

int main()
{
    //preclalc
    map <long long, vector <long long> > mp;
    for (long long i = 1; i < max_a; i++)
    {
        if (i % 20000 == 0)
           cout << i / 20000 << endl;
        g[min_shift(i)].pb(i);
    }
    
    ifstream cin ("input.txt");
    ofstream cout("output.txt");
    long long T;
    cin >> T;
    for (long long cc = 0; cc < T; cc++)
    {
        long long a, b;
        cin >> a >> b;
        long long l = 1, r;
        while (l <= a)
              l *= 10;
        r = l, l /= 10;
        long long res = 0;
        for (long long i = l; i <= b; i++)
        {
            for (long long j = 0; j < g[i].size(); j++)
                for (long long k = 0; k < g[i].size(); k++)
                    if (a <= g[i][j] && g[i][j] < g[i][k] && g[i][k] <= b)
                       res++;
        }
        cout << "Case #" << cc + 1 << ": " << res << endl;
    }
    return 0;
}
