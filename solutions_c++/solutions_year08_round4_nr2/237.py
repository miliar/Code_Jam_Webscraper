#include <iostream>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cmath>

using namespace std;

int main()
{
    int cases;
    cin >> cases;

    for (int cs = 0; cs < cases; ++cs) {
        int N, M, A;
        cin >> N >> M >> A;

        map<int, pair<int, int> > mp;
        for (int x = 0; x <= N; ++x) {
            // cout << x << endl;
            for (int y = 0; y <= M; ++y)
                // mp[x * y] = make_pair(x, y);
                mp.insert(make_pair(x * y, make_pair(x, y)));
        }
        // cout << mp.size() << endl;

        cout << "Case #" << cs + 1 << ": ";

        for (map<int, pair<int, int> >::iterator i = mp.begin();
             i != mp.end(); ++i) {
            int v = i->first;
            int x1 = i->second.first;
            int y2 = i->second.second;

            for (map<int, pair<int, int> >::iterator j = mp.begin();
                 j != mp.end(); ++j) {
                int w = j->first;
                int x2 = j->second.first;
                int y1 = j->second.second;

                if (abs(v - w) == A) {
                    cout << "0 0 " << x1 << ' ' << y1
                         << ' ' << x2 << ' ' << y2;
                    goto done;
                }
            }
        }

        cout << "IMPOSSIBLE";
    done:
        cout << '\n';
    }

    return 0;
}
