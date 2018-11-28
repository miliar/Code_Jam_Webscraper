#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <climits>
using namespace std;

int main()
{
    int cases;
    cin >> cases;

    for (int cs = 0; cs < cases; ++cs) {
        int k;
        string s;
        cin >> k >> s;
        int L = (int)s.size();

        vector<int> v;
        for (int i = 0; i < k; ++i)
            v.push_back(i);

        int best = INT_MAX;
        do {
            string t;
            for (int i = 0; i < L; i += k) {
                string sub = s.substr(i, k);
                string perm(k, '-');
                for (int j = 0; j < k; ++j)
                    perm[j] = sub[v[j]];
                t += perm;
            }

            int cost = 0;
            char last = '-';
            for (int i = 0; i < L; ++i) {
                char ch = t[i];
                if (last != ch) {
                    last = ch;
                    ++cost;
                }
            }
            best = min(best, cost);
        } while (next_permutation(v.begin(), v.end()));

        cout << "Case #" << cs + 1 << ": " << best << '\n';
    }

    return 0;
}
