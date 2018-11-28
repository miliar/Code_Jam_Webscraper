#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <utility>
#include <complex>

using namespace std;

typedef long long LL;
typedef long double LD;

int nTests, test;

// <solution>

int X, S, R, N;
LD toRun;

void solve()
{
    cin >> X >> S >> R >> toRun >> N;

    vector<pair<int, int> > ws;
    for (int i = 0; i < N; i++)
    {
        int b, e, w;
        cin >> b >> e >> w;

        ws.push_back(make_pair(w, e - b));
        X -= e - b;
    }        
    ws.push_back(make_pair(0, X)); 

    sort(ws.begin(), ws.end());

    LD ans = 0.0;
    for (int i = 0; i < ws.size(); i++)
    {
        LD byRun = ws[i].second / (LD)(ws[i].first + R);
        if (byRun < toRun + 1e-9)
        {
            toRun -= byRun;
            ans += byRun;
        }
        else
        {
            ans += toRun;
            ans += (ws[i].second - (ws[i].first + R) * toRun) / (LD)(ws[i].first + S);
            toRun = 0.0;
        }
    }

    cout << "Case #" << test << ": " << fixed << setprecision(9) << ans << '\n';
}

// </solution> 

int main()
{                
    cin >> nTests;
    for (test = 1; test <= nTests; test++)
        solve();
    return 0;
}
