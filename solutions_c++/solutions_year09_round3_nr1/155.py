#include <iostream>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

const int MAXN = 100;
int kase, kases, n;
long long tot, res;
map<char,long long> a;
string s;
long long b[MAXN];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> kases;
    for (kase = 1; kase <= kases; ++kase)
    {
        cin >> s;
        n = s.size();
        a.clear();
        tot = 0;
        for (int i = 0; i != n; ++i)
            if (a.count(s[i]))
                b[i] = a[s[i]];
            else
            {
                if (tot == 0)
                {
                    b[i] = 1;
                    a[s[i]] = 1;
                }
                else if (tot == 1)
                {
                    b[i] = 0;
                    a[s[i]] = 0;
                }
                else
                {
                    b[i] = tot;
                    a[s[i]] = tot;
                }
                ++tot;
            }
        if (tot == 1) ++tot;
        res = 0;
        for (int i = 0; i != n; ++i)
            res = res * tot + b[i];
        cout << "Case #" << kase << ": " << res << endl;
    }
    return 0;
}
