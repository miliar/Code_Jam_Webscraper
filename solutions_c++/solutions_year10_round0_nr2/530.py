#include <iostream>
#include <queue>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <list>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long long ll;

class ln{
    public:
        int a[60];
        int k;
        
        ln(const ln &b)
        {
            if (&b != this)
            {
                memcpy(a, b.a, sizeof(a));
                k = b.k;
            }
        }
        ln(string s = "")
        {
            memset(a, 0, sizeof(a));
            k = sz(s);
            REP(i, k)
                a[i] = s[k - i - 1] - '0';
            while (k > 0 && s[k - 1] == 0)
                k--;
        }
        bool Less(const ln &b, int t)
        {
            if (k < b.k + t)
                return 1;
            if (k > b.k + t)
                return 0;
            FOD(i, k - 1, t)
                if (a[i] < b.a[i - t])
                    return 1;
                else if (a[i] > b.a[i - t])
                    return 0;
            return 0;
        }
        bool operator < (const ln &b) const
        {
            if (k < b.k)
                return 1;
            if (k > b.k)
                return 0;
            FOD(i, k - 1, 0)
                if (a[i] < b.a[i])
                    return 1;
                else if (a[i] > b.a[i])
                    return 0;
            return 0;
        }
        void Substruct(const ln &b, int tt)
        {
            int t = 0;
            FOR(i, tt, k)
            {
                a[i] = a[i] - t - b.a[i - tt];
                t = 0;
                while (a[i] < 0)
                    t++, a[i] += 10;
            }
            while (k > 0 && a[k - 1] == 0)
                k--;
        }
        ln operator - (const ln &b)
        {
            ln rt;
            int t = 0;
            REP(i, k)
            {
                rt.a[i] = a[i] - t - b.a[i];
                t = 0;
                while (rt.a[i] < 0)
                    t++, rt.a[i] += 10;
            }
            rt.k = k;
            while (rt.k > 0 && rt.a[rt.k - 1] == 0)
                rt.k--;
            return rt;
        }
        ln operator % (const ln &b)
        {
            ln rt = *this;
            int t = rt.k - b.k;
            while (t >= 0)
            {
                if (rt.Less(b, t))
                {
                    if (rt.k != 1)
                    {
                        rt.a[rt.k - 2] += 10 * rt.a[rt.k - 1];
                        rt.a[rt.k - 1] = 0;
                        rt.k--;
                    }
                    t--;
                }
                else
                {
                    rt.Substruct(b, t);
                    while (t >= 0 && rt.a[b.k + t - 1] == 0)
                        t--;
                }
            }
            while (rt.k > 0 && rt.a[rt.k - 1] == 0)
                rt.k--;
            return rt;
        }
        void out()
        {
            if (k == 0)
                printf("0");
            FOD(i, k - 1, 0)
                printf("%d", a[i]);
            printf("\n");
        }
};

ln b[1000];

ln gcd(ln x, ln y)
{
    if (x < y)
        swap(x, y);
    while (y.k != 0)
    {
        x = x % y;
        swap(y, x);
    }
    return x;
}

int main()
{
    int c;
    scanf("%d", &c);
    REP(ii, c)
    {
        int k;
        scanf("%d", &k);
        string s;
        REP(i, k)
        {
            cin >> s;
            b[i] = ln(s);
        }
        sort(b, b + k);
        ln rt = b[k - 1] - b[k - 2];
        FOD(i, k - 2, 1)
        {
            ln kk = b[i] - b[i - 1];
            rt = gcd(kk, rt);
        }
        ln rr = b[0] % rt;
        printf("Case #%d: ", ii + 1);
        if (rr.k == 0)
            rr.out();
        else
            rr = rt - rr, rr.out();
    }
}
