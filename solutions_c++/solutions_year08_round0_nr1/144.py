#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <cstdlib>

using namespace std;

static string gl()
{
    string ans;
    getline(cin, ans);
    return ans;
}

static int gli()
{
    string tmp = gl();
    return atoi(tmp.c_str());
}

static int pick(const vector<int> &order, int S, int pos)
{
    bool seen[S];
    int R = S;

    fill(seen, seen + S, false);
    while (pos < (int) order.size() && R > 1)
    {
        if (!seen[order[pos]])
        {
            seen[order[pos]] = true;
            R--;
        }
        pos++;
    }
    return find(seen, seen + S, false) - seen;
}

int main()
{
    int cases;
    cases = gli();
    for (int cas = 0; cas < cases; cas++)
    {
        int S = gli();
        vector<string> names(S);
        map<string, int> dict;
        for (int i = 0; i < S; i++)
        {
            string n = gl();
            dict[n] = i;
            names[i] = n;
        }

        int Q = gli();
        vector<int> order(Q);
        for (int i = 0; i < Q; i++)
            order[i] = dict[gl()];

        int st = pick(order, S,  0);
        int ans = 0;
        for (size_t pos = 0; pos < order.size(); pos++)
        {
            if (order[pos] == st)
            {
                ans++;
                st = pick(order, S, pos);
            }
        }
        cout << "Case #" << cas + 1 << ": " << ans << "\n";
    }

    return 0;
}
