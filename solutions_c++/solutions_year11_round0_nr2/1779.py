#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;

#define pb push_back
#define sz size

int it, c, d, n;
string C[100], D[100], s, cs;
int has[256];

void read ()
{
    cin >> c;
    for (int i = 0; i < c; ++i)
        cin >> C[i];
    cin >> d;
    for (int i = 0; i < d; ++i)
        cin >> D[i];
    cin >> n >> s;
    cs = "";
}

void solve ()
{
    for (int i = 0; i < n; ++i)
    {
        bool used = false;
        if (cs.sz() > 0)
        {
            for (int j = 0; j < c; ++j)
            {
                char cr = '#';
                if (C[j][0] == s[i])
                    cr = C[j][1];
                if (C[j][1] == s[i])
                    cr = C[j][0];
                if (cr == cs[cs.sz() - 1])
                {
                    has[cs[cs.sz() - 1]]--;
                    has[C[j][2]]++;

                    cs.resize(cs.sz() - 1);
                    cs.pb(C[j][2]);

                    used = true;
                    break;
                }
            }
        }

        if (!used)
        {
            for (int j = 0; j < d; ++j)
            {
                char cr = '#';
                if (D[j][0] == s[i])
                    cr = D[j][1];
                if (D[j][1] == s[i])
                    cr = D[j][0];
                if (has[cr] - (D[j][0] == D[j][1]) > 0)
                {
                    for (int k = 0; k < cs.sz(); ++k)
                        has[cs[k]]--;
                    cs.resize(0);
                    used = true;
                    break;
                }
            }
        }

        if (!used)
        {
            cs.pb(s[i]);
            has[s[i]]++;
        }
    }

    for (int i = 0; i < cs.sz(); ++i)
        has[cs[i]]--;

    for (int i = 0; i < int(cs.sz()) - 1; ++i)
        cout << cs[i] << ", ";
    if (int(cs.sz()))
        cout << cs[cs.sz() - 1];
}

int main ()
{
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );

    cin >> it;
    for (int i = 0; i < it; ++i)
    {
        read();
        cout << "Case #" << i + 1 << ": [";
        solve();
        cout << "]\n";
    }
    return 0;
}
