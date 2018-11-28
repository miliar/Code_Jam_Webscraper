#include <iostream>
#include <vector>
#include <cstdio>
#include <set>
using namespace std;

typedef pair<int, int> circle;

void place(int n, vector<int> const& r, set<circle>& s, vector<int> & x, vector<int> & y,
        int w, int h, int x0, int y0, bool swapped, vector<bool> can_get_out) {
    // cerr << w << "x" << h << "\n";
    // cerr << "xy00: " << x0 << " " << y0 << "\n";
    for (int i = 0; i < 4; ++i) {
        // cerr << can_get_out[i] << " ";
    }
    // cerr << "\n";

    if (s.empty()) {
        return;
    }

    if (w < h) {
        swap(w, h);
        swap(x0, y0);
        swapped = !swapped;
        bool t = can_get_out[0];
        can_get_out[0] = can_get_out[1];
        can_get_out[1] = t;

        t = can_get_out[2];
        can_get_out[2] = can_get_out[3];
        can_get_out[3] = t;

        // cerr << "swapped\n";
        // cerr << w << "x" << h << "\n";
        for (int i = 0; i < 4; ++i) {
            // cerr << can_get_out[i] << " ";
        }
        // cerr << "\n";
    }


    int max_wr;
    int cgow = can_get_out[1] + can_get_out[3];
    switch (cgow) {
        case 0: max_wr = w/2;
                break;
        case 1: max_wr = w;
                break;
        case 2: max_wr = 1000000;
                break;
        default:
                throw 42;
    }

    int max_hr;
    int cgoh = can_get_out[0] + can_get_out[2];
    switch (cgoh) {
        case 0: max_hr = h/2;
                break;
        case 1: max_hr = h;
                break;
        case 2: max_hr = 1000000;
                break;
        default:
                throw 43;
    }

    int max_ok_r = min(max_wr, max_hr);


    auto z_it = s.upper_bound(make_pair(max_ok_r + 1, -1));
    if (z_it == s.begin()) {
        return;
    }

    --z_it;
    circle z = *z_it;
    int r1 = z.first;
    s.erase(z_it);
    

    // cerr << "xy0: " << x0 << " " << y0 << "\n";
    int X = x0 + (can_get_out[1] ? 0 : r1);
    int Y = y0 + (can_get_out[0] ? 0 : r1);;


    // cerr << "using " << z.first << " " << z.second << "\n";

    x[z.second] = swapped ? Y : X;
    y[z.second] = swapped ? X : Y;

    // cerr << "XY: " << X << " " << Y << "\n";
    int y1 = Y + r1;
    int x1 = X + r1;
    int w1 = x1 - x0;
    int h1 = y1 - y0;

    vector<bool> cgo1(4, false);
    cgo1[2] = can_get_out[2];
    cgo1[1] = can_get_out[1];

    can_get_out[1] = false;
    place(n, r, s, x, y, w1, h - h1, x0, y1, swapped, cgo1);

    place(n, r, s, x, y, w - w1, h, x1, y0, swapped, can_get_out);
        
}

int main() {
    int T;
    cin >> T;
    for (int K = 1; K <= T; ++K) {
        int n, w, h;
        cin >> n >> w >> h;

        vector<int> r(n);
        set<circle> s;
        for (int i = 0; i < n; ++i) {
            cin >> r[i];
            s.insert(make_pair(r[i], i));
        }
        vector<int> x(n);
        vector<int> y(n);

        vector<bool> can_get_out(4, true);
        place(n, r, s, x, y, w, h, 0, 0, false, can_get_out);

        printf("Case #%d:", K);

        for (int i = 0; i < n; ++i) {
            printf(" %d %d", x[i], y[i]);
        }
        printf("\n");
        if (!s.empty()) {
            cerr << "Case " << K << " is bad\n";
        }
    }
}
