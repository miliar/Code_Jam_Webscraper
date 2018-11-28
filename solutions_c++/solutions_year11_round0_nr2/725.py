#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

#define REP(i,N) for (int i=0; i<N; i++)

char c[256][256];
bool d[256][256];
string el;

int main ()
{
    freopen ("B-large.in", "r", stdin);
    //freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);

    string s;
    int T, C, D, N;
    cin >> T;
    REP (cas, T)
    {
        REP (i, 256) REP (j, 256) c[i][j] = d[i][j] = 0;
        el = "";

        cin >> C;
        REP (i, C)
        {
            cin >> s;
            c[s[0]][s[1]] = c[s[1]][s[0]] = s[2];
        }
        cin >> D;
        REP (i, D)
        {
            cin >> s;
            d[s[0]][s[1]] = d[s[1]][s[0]] = true;
        }
        cin >> N >> s;
        REP (i, N)
        {
            el += s[i];
            while (el.length() >= 2)
            {
                char end0 = el[el.length() - 1], end1 = el[el.length() - 2];
                if (c[end0][end1] == 0) break;
                el = el.substr(0, el.length() - 2) + c[end0][end1];
            }
            bool clear = false;
            REP (j, el.length()) REP (i, j) if (d[el[i]][el[j]]) clear = true;
            if (clear) el = "";
        }
        string ans = "[";
        if (el.length() > 0)
        {
            ans += el[0];
            REP (i, el.length()) if (i > 0)
            {
                ans += ", ";
                ans += el[i];
            }
        }
        ans += "]";
        cout << "Case #" << (cas+1) << ": " << ans << endl;
    }

    return 0;
}
