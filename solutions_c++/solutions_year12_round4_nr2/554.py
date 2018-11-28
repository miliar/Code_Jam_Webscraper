#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
#include <deque>
#include <queue>
#include <set>
#include <tr1/unordered_set>
#include <tr1/unordered_map>

#define D(x)

using namespace std;
using namespace std::tr1;

int main() {
    int T;
    cin >> T;

    for (int testCase = 1; testCase <= T; testCase++) {
        int N, W, L; cin >> N >> W >> L;

        vector<pair<int, int> > points(N);

        for (int i = 0; i < N; i++) {
            cin >> points[i].first;
            points[i].second = i;
        }

        sort(points.begin(), points.end());
        reverse(points.begin(), points.end());

        int lower = 0, left = 0, upper = 0;
        bool atBottom = true, atLeft = true;

        vector<int> xs(N), ys(N);

        for (int i = 0; i < N; i++) {
            int r = points[i].first, index = points[i].second;

            if (!atLeft && (left + r > W)) {
                D(cerr << " resetting" << endl);
                lower = upper;
                left = 0;
                atLeft = true;
                atBottom = false;
                D(cerr << "bounds: " << left << "," << lower << " " << upper << endl);
                if (lower > L) {
                    cerr << "error: out of room!";
                    break;
                }
            }

            int x = left, y = lower;
            if (!atLeft) x += r;
            if (!atBottom) y += r;

            xs[index] = x; ys[index] = y;
            D(cerr << "Placed " << index << " at " << x << ", " << y << endl);

            left = x+r;
            upper = max(upper, y+r);
            D(cerr << "bounds: " << left << "," << lower << " " << upper << endl);

            atLeft = false;
        }


        cout << "Case #" << testCase << ":";
        for (int i = 0; i < N; i++) {
            cout << " " << xs[i] << " " << ys[i];
        }

        cout << endl;
    }
}
