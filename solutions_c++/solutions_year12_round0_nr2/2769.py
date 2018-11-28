#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cassert>


using namespace std;


int main()
{
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        int n, s, p;
        cin >> n >> s >> p;

        int r = 0;
        for (int i = 0; i < n; ++i) {
            int t;
            cin >> t;
            int best = t / 3;
            if (t % 3) {
                ++best;
            }
            if (best >= p) {
                ++r;
            } else if (s > 0 && t % 3 != 1 && t / 3 > 0 && best + 1 >= p) {
                ++r;
                --s;
            }
        }

        cout << "Case #" << test << ": " << r << endl;
    }

    return 0;
}
