#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MAXL = 30, MAXD = 6000;
string s;
string a[MAXD];
int l, d, n, tot, now;
int st[MAXL], ed[MAXL];

bool match(string t)
{
    bool flag;
    for (int i = 0; i != l; ++i)
    {
        flag = false;
        for (int j = st[i]; j != ed[i]; ++j)
            if (s[j] == t[i])
            {
                flag = true;
                break;
            }
        if (!flag) return false;
    }
    return true;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin >> l >> d >> n;
    for (int i = 0; i != d; ++i)
        cin >> a[i];
    for (int i = 0; i != n; ++i)
    {
        cin >> s;
        bool flag = false;
        int k = 0;
        for (int j = 0; j != s.size(); ++j)
            if (s[j] == '(')
            {
                st[k] = j + 1;
                flag = true;
            }
            else if (s[j] == ')')
            {
                ed[k] = j;
                flag = false;
                ++k;
            }
            else if (!flag)
            {
                st[k] = j;
                ed[k] = j + 1;
                ++k;
            }
        cout << "Case #" << i + 1 << ": ";
        tot = 0;
        for (int j = 0; j != d; ++j)
            if (match(a[j])) ++tot;
        cout << tot << endl;
    }

    return 0;
}
