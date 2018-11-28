#include <iomanip>
#include <iostream>
#include <vector>
using namespace std;

struct triple {
    int b, e, w;
};

bool by_b(triple a, triple b) {
    return a.b < b.b;
}

bool by_w(triple a, triple b) {
    return a.w < b.w;
}

int main() {
    int cs;
    cin >> cs;
    for (int cc = 1; cc <= cs; cc++) {
        int x, s, r, n;
        double t;
        cin >> x >> s >> r >> t >> n;
        vector<triple> v(n);
        for (int i = 0; i < n; i++)
            cin >> v[i].b >> v[i].e >> v[i].w;
        sort(v.begin(), v.end(), by_b);
        int p = 0;
        vector<triple> w;
        for (int i = 0; i < v.size(); i++) {
            if (p < v[i].b) {
                //add
                triple t;
                t.b = p;
                t.e = v[i].b;
                t.w = 0;
                w.push_back(t);
            }
            p = v[i].e;
        }
        if (p < x) {
            //add
            triple t;
            t.b = p;
            t.e = x;
            t.w = 0;
            w.push_back(t);
        }
        for (int i = 0; i < w.size(); i++)
            v.push_back(w[i]);
        sort(v.begin(), v.end(), by_w);
        double timer = 0;
        for (int i = 0; i < v.size(); i++) {
            int dist = v[i].e - v[i].b;
            double rt = (double)dist / (v[i].w + r);
            if (rt <= t) {
                t -= rt;
                timer += ((double)v[i].e - v[i].b) / (v[i].w + r);
            } else {
                timer += t;
                timer += ((double)v[i].e - v[i].b - t * (v[i].w + r)) / (v[i].w + s);
                t = 0;
            }
        }
        cout << "Case #" << cc << ": " << setprecision(99) << timer << "\n";
    }
}
