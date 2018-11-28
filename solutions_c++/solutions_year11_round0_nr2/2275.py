#include <string>
#include <cstring>
#include <iostream>
#define MAXN (1 << 7)
using namespace std;

int a, b, c;
string cur;
string magic, boom;
int M[32][32], B[32][32];

inline void solve()
{
    string sol;
    sol.clear();
    for (int i=0; i < cur.size(); ++i)
    {
        int add = cur[i]-'A';
        if (sol.size() && M[add][sol[sol.size()-1]-'A'])
        {
            char save = char(M[add][sol[sol.size()-1]-'A']-1 + 'A');
            sol.erase(sol.size()-1);
            sol += save;
            continue;
        }
        for (int j=0; j < sol.size(); ++j)
            if (B[add][ sol[j]-'A' ])
            {
                sol.clear();
                goto skip;
            }
        sol += cur[i];
        skip:;
    }

    cout << "[";
    if (sol.size()) cout << sol[0];
    if (sol.size() > 1)
        for (int i=1; i < sol.size(); ++i)
            cout << ", " << sol[i];
    cout << "]\n";
}

inline void read()
{
    memset(M, 0, sizeof(M));
    memset(B, 0, sizeof(B));

    cin >> a;
    for (int i=0; i < a; ++i)
    {
        cin >> magic;
        int fir = magic[0]-'A', sec = magic[1]-'A';
        M[fir][sec] = M[sec][fir] = magic[2]-'A'+1;
    }
    cin >> b;
    for (int i=0; i < b; ++i)
    {
        cin >> boom;
        int fir = boom[0]-'A', sec = boom[1]-'A';
        B[fir][sec] = B[sec][fir] = 1;
    }
    cin >> c;
    cin >> cur;
}

int main()
{
    int brt, testNo = 0;
    cin >> brt;

    while (brt --)
    {
        read();
        cout << "Case #" << ++testNo << ": ";
        solve();
    }
    return 0;
}
