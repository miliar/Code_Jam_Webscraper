#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <limits>
#include <algorithm>

using namespace std;

const int INF = numeric_limits<int>::max();

int main()
{
    int cases;
    cin >> cases;

    string line;
    for (int cs = 0; cs < cases; ++cs) {
        int s;
        cin >> s;
        getline(cin, line);

        map<string, int> mp;
        for (int i = 0; i < s; ++i) {
            getline(cin, line);
            mp.insert(make_pair(line, i));
        }

        int q;
        cin >> q;
        getline(cin, line);

        vector<int> dp(s, 0);
        for (int i = 0; i < q; ++i) {
            string query;
            getline(cin, query);
            int idx = mp[query];

            vector<int> ndp(dp);
            ndp[idx] = INF;
            if (dp[idx] != INF) {
                for (int j = 0; j < s; ++j) {
                    if (j == idx) continue;
                    ndp[j] = min(ndp[j], dp[idx] + 1);
                }
            }
            dp.swap(ndp);
        }

        cout << "Case #" << cs + 1 << ": " << *min_element(dp.begin(), dp.end())
             << '\n';
    }

    return 0;
}
