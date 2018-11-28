#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


double solve(int x, int s, int r, int t, int n, vector<int>& b, vector<int>& e, vector<int>& w)
{
    struct part
    {
        int start;
        int speed;
        int len;
        part() { }
        part(int start, int speed, int len) : start(start), speed(speed), len(len) { }
        bool operator < (const part& rhs) const { return start < rhs.start; }
    };

    struct cmp_by_speed
    {
        bool operator () (const part& a, const part& b) const
        {
            return a.speed < b.speed;
        }
    };

    vector<part> ev;
    for (int i = 0; i < n; ++i) {
        ev.push_back(part(b[i], w[i] + s, e[i] - b[i]));
    }
    sort(ev.begin(), ev.end());
    vector<part> nev;
    int last = 0;
    for (int i = 0; i < n; ++i) {
        if (ev[i].start > last) {
            nev.push_back(part(last, s, ev[i].start - last));
        }
        nev.push_back(ev[i]);
        last = ev[i].start + ev[i].len;
    }
    if (ev[n - 1].start + ev[n - 1].len < x) {
        nev.push_back(part(ev[n - 1].start + ev[n - 1].len, s, x - ev[n - 1].start - ev[n - 1].len));
    }

    //for (int i = 0, ilen = (int) nev.size(); i < ilen; ++i) {
    //    cout << nev[i].start << " " << nev[i].len << " with speed " << nev[i].speed << endl;
    //}

    sort(nev.begin(), nev.end(), cmp_by_speed());

    double result = 0.0;
    double remt = t;
    for (int i = 0, ilen = (int) nev.size(); i < ilen; ++i) {
        double needt = double(nev[i].len) / (nev[i].speed + (r - s));
        if (remt >= needt) {
            result += needt;
            remt -= needt;
        } else {
            result += double(nev[i].len) / nev[i].speed - (r - s) * remt / nev[i].speed;
            remt = 0;
        }
    }

    return result;
}

int main()
{
    int tests;
    cin >> tests;
    cout.precision(20);
    for (int test = 0; test < tests; ++test) {
        int x, s, r, t, n;
        cin >> x >> s >> r >> t >> n;
        vector<int> b(n), e(n), w(n);
        for (int i = 0; i < n; ++i) {
            cin >> b[i] >> e[i] >> w[i];
        }
        cout << "Case #" << (test + 1) << ": " << solve(x, s, r, t, n, b, e, w) << endl;
    }
}