#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <math.h>
#include <queue>
#include <memory.h>
#include <iostream>
#include <stack>
#include <complex>
#include <list>

using namespace std;

void ASS(bool b)
{
    if (!b)
    {
	    ++*(int*)0;
    }
}

#define FOR(i, x) for (int i = 0; i < (int)(x); i++)
#define CL(x) memset(x, 0, sizeof(x))
#define CLX(x, y) memset(x, y, sizeof(x))

#pragma comment(linker, "/STACK:106777216")

typedef vector<int> vi;
typedef long long LL;

int A, B;

string S(int x)
{
    char buf[16];
    sprintf(buf, "%d", x);
    return buf;
}


map<pair<int, int>, int> mp;

int f[1 << 21];

int Solve()
{
    CL(f);
    ASS(S(A).size() == S(B).size());
    int s[16];
    int res = 0;
    for (int n = A; n <= B; n++)
    {
        int k = 0;
        int x = n;
        while (x)
        {
            s[k++] = x % 10;
            x /= 10;
        }
        reverse(s, s + k);
        for (int i = 1; i < k; i++)
        {
            if (s[k - i] == 0)
                continue;
            x = 0;
            FOR(j, i)
                x = x * 10 + s[k - i + j];
            FOR(j, k - i)
                x = x * 10 + s[j];
            if (n < x && x <= B)
            {
                if (f[x] != n)
                {
                    f[x] = n;
                    res++;
                }
            }
        }
    }
    return res;
}

bool Ok(const int n, const int m)
{
    string s = S(n);
    for (int k = 1; k < (int)s.size(); k++)
    {
        int x = 0;
        FOR(i, k)
            x = x * 10 + (s[s.size() - k + i] - '0');
        FOR(i, s.size() - k)
            x = x * 10 + (s[i] - '0');
        if (x == m)
            return 1;
    }
    return 0;
}

int Vlob()
{
    int res = 0;
    for (int i = A; i <= B; i++)
        for (int j = i + 1; j <= B; j++)
            res += Ok(i, j);
    return res;
}

int main()
{
    freopen("c:\\my\\in.txt", "r", stdin);
    freopen("c:\\my\\out.txt", "w", stdout);

    int t;
    cin >> t;
    FOR(i, t)
    {
        cout << "Case #" << (i + 1) << ": ";
        cin >> A >> B;
        int res = Solve();
        cout << res << endl;
        //int res2 = Vlob();
        //if (res != res2)
        //{
        //    cout << A << " " << B << endl;
        //    cout << res << " " << res2 << endl;
        //    return 0;
        //}
        //ASS(res == res2);
    }

    return 0;
}
