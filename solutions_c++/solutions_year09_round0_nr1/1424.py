#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <list>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (itn i = (a); i >= (b); i++)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define mp make_pair
#define cl clear()
#define sz(a) ((int)a.size())
#define X first
#define Y second
#define pb push_back
#define sqr(a) ((a) * (a))

int l, d, n;

string a[5000];

int main()
{
	scanf("%d%d%d\n", &l, &d, &n);
	REP(i, d)
        getline(cin, a[i]);
    string s;
    REP(i, n)
    {
        getline(cin, s);
        int k = 0;
        REP(t, d)
        {
            int j = 0;
            REP(id, l)
            {
                if (s[j] == '(')
                {
                    j++;
                    bool q = false;
                    while (s[j] != ')')
                    {
                        if (s[j] == a[t][id])
                            q = true;
                        j++;
                    }
                    if (!q)
                        goto wtf;
                }
                else if (s[j] != a[t][id])
                    goto wtf;
                j++;
            }
            k++;
            wtf:;
        }
        printf("Case #%d: %d\n", i + 1, k);
    }
	return 0;
}
