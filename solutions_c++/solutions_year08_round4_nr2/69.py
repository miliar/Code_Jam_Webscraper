#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <numeric>

using namespace std;

typedef signed long long i64;  
typedef unsigned long long u64;
typedef long double real;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;

#define forr(i,n0,n1) for(int i=(n0); i<(n1); i++)
#define forn(i,n) for(int i=0; i<(n); i++)
#define fors(i,s) forn(i, (int)s.length())
#define forv(i,v) forn(i, (int)v.size())
#define fore(t, it, obj) for (t :: iterator it = obj.begin(); it != obj.end(); it++)

#define two(n) (1 << (n))
#define has(mask, i) (((mask) & two(i)) != 0)

#define pb push_back
#define all(v) v.begin(), v.end()
#define mp make_pair

int A, B, R;

int check(int dxa, int dya, int dxb, int dyb)
{
    if (dxa <= A && dxb <= A && dya <= B && dyb <= B)
    {
        int exp = dxa * dyb - dxb * dya;

        if (exp == R)
        {
            cout << "0 0 ";
            cout << dxa << " " << dya << " ";
            cout << dxb << " " << dyb;
            return R;
        }
        else
            return -1;
    }

    return -1;
}

int area(int x1, int y1, int x2, int y2, int x3, int y3)
{
    int dx1 = x2 - x1;
    int dy1 = y2 - y1;
    int dx2 = x3 - x1;
    int dy2 = y3 - y1;

    return abs(dx1 * dy2 - dx2 * dy1);
}

bool naive()
{
    forn(x1, A + 1)
    forn(x2, A + 1)
    forn(x3, A + 1)
    forn(y1, B + 1)
    forn(y2, B + 1)
    forn(y3, B + 1)
    {
        if (area(x1, y1, x2, y2, x3, y3) == R)
        {
            cout << x1 << " " << y1 << endl;
            cout << x2 << " " << y2 << endl;
            cout << x3 << " " << y3 << endl;
            return true;
        }
    }

    return false;
}

void solve()
{
    for (int dya = 0; dya <= max(A, B); dya++)
    {
        for (int dxb = 0; dxb <= max(A, B); dxb++)
        {
            int result = R + dya * dxb;

            for (int i = 1; i * i <= result; i++)
                if (result % i == 0)
                {
                    int x = i;
                    int y = result / i;

                    if (check(x, dya, dxb, y) == R)
                    {
                        return;
                    }

                    if (check(y, dya, dxb, x) == R)
                    {
                        cout << "*";

                        return;
                    }
                }
        }
    }

    cout << "IMPOSSIBLE";
}

int main()
{
    freopen("input.txt", "rt", stdin);

    int testCount;

    cin >> testCount;

    forn(ta, testCount)
    {
        cin >> A >> B >> R;
        //cout << naive() << endl;
        cout << "Case #" << ta + 1 << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
