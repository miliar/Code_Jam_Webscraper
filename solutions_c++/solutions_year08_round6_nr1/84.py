#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <climits>
using namespace std;

enum Result { UNKNOWN, BIRD, NOTBIRD };

int main()
{
    int cases;
    cin >> cases;
    for (int cs = 0; cs < cases; ++cs) {
        vector<int> weights, heights;
        vector<bool> isBird;
        int N;
        cin >> N;
        for (int i = 0; i < N; ++i) {
            int w, h;
            bool bird = true;
            string s;
            cin >> w >> h >> s;
            if (s == "NOT") {
                cin >> s;
                bird = false;
            }
            weights.push_back(w);
            heights.push_back(h);
            isBird.push_back(bird);
        }

        cout << "Case #" << cs + 1 << ":\n";

        int wmin = INT_MAX;
        int wmax = INT_MIN;
        int hmin = INT_MAX;
        int hmax = INT_MIN;
        for (int i = 0; i < N; ++i) {
            if (isBird[i]) {
                wmin = min(wmin, weights[i]);
                wmax = max(wmax, weights[i]);
                hmin = min(hmin, heights[i]);
                hmax = max(hmax, heights[i]);
            }
        }

        int wlb = INT_MIN, wub = INT_MAX;
        int hlb = INT_MIN, hub = INT_MAX;
        for (int i = 0; i < N; ++i) {
            if (!isBird[i]) {
                int w = weights[i];
                int h = heights[i];
                if (wmin <= w && w <= wmax) {
                    if (h < hmin)
                        hlb = max(hlb, h);
                    else
                        hub = min(hub, h);
                }
                else if (hmin <= h && h <= hmax) {
                    if (w < wmin)
                        wlb = max(wlb, w);
                    else
                        wub = min(wub, w);
                }
            }
        }

        int M;
        cin >> M;
        for (int i = 0; i < M; ++i) {
            int w, h;
            cin >> w >> h;

            Result result = UNKNOWN;
            if (wmin <= w && w <= wmax && hmin <= h && h <= hmax)
                result = BIRD;
            else if (w <= wlb || wub <= w || h <= hlb || hub <= h)
                result = NOTBIRD;
            else {
                for (int i = 0; i < N; ++i)
                    if (!isBird[i] && weights[i] == w && heights[i] == h)
                        result = NOTBIRD;
            }

            switch (result) {
            case UNKNOWN:
                cout << "UNKNOWN\n";
                break;
            case BIRD:
                cout << "BIRD\n";
                break;
            case NOTBIRD:
                cout << "NOT BIRD\n";
                break;
            }
        }
    }

    return 0;
}
