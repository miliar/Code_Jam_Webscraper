#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int main()
{
    int i, j, k, tt;
    ifstream fin("C.in");
    fin >> tt;
    cout.precision(9);
    cout.setf(ios::fixed, ios::floatfield);
    for (int test = 1; test <= tt; test++) {
        int n, x, s, r, b, e, wi;
        double res = 0, t;

        fin >> x >> s >> r >> t >> n;

        vector < pair <double, pair <int, int> > > p;

        int len = 0;
        double dl, v;
        for (i = 0; i < n; i++) {
            fin >> b >> e >> wi;
            dl = e - b;
            len += e - b;
            p.push_back(make_pair(1.0 / (wi + s) - 1.0 / (wi + r), make_pair(dl, wi)));
        }

        dl = x - len;
        p.push_back(make_pair(1.0 / s - 1.0 / r, make_pair(dl, 0)));

        sort(p.rbegin(), p.rend());

        for (i = 0; i < p.size(); i++) {
            dl = p[i].second.first, v = p[i].second.second;
            if (t) {
                double t1 = dl / (v + r), t2 = min(t1, t);
                dl -= t2 * (v + r);
                t -= t2;
                res += t2 + dl / (v + s);
            }
            else res += double(dl) / (v + s);
        }

        cout << "Case #" << test << ": " << res << endl;
    }

    return 0;
}
