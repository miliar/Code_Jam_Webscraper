#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <assert.h>

using namespace std;

#define pi 3.14159265358979323
#define eps 1e-7

double dist(double a1, double a2, double b1, double b2) {
    return sqrt((a1-b1)*(a1-b1)+(a2-b2)*(a2-b2));
}

double dist2(double a1, double a2, double b1, double b2) {
    return (a1-b1)*(a1-b1)+(a2-b2)*(a2-b2);
}

double piearea(double y1, double y2, double r) { //y1 > y2
    double an1 = asin(y1/r);
    double an2 = asin(y2/r);
    return (an1-an2) / 2 * r*r;
}

double inarea(double lx, double ly, double r, double side) {
    if (dist2(lx+side, ly+side, 0, 0) <= r*r) return side*side;
    double lefti = sqrt(r*r-lx*lx);
    double topi = sqrt(r*r-(ly+side)*(ly+side));
    double boti = sqrt(r*r-ly*ly);
    double righti = sqrt(r*r-(lx+side)*(lx+side));
    double res = 0;
    if (lefti <= ly+side && boti > lx+side) {
        //cout << "case 1 " << lefti << " " << boti << endl;
        assert(r*r >= (lx+side)*(lx+side));
        double righti = sqrt(r*r-(lx+side)*(lx+side));
        res += piearea(lefti, righti, r);
        res -= (lefti-ly) * lx / 2;
        res -= side * ly / 2;
        res += (righti-ly) * (lx+side) / 2;
    }
    else if (lefti <= ly+side && boti <= lx+side) {
        //cout << "case 2 " << lefti << " " << boti << endl;
        res += piearea(lefti, ly, r);
        res -= (lefti-ly)*lx/2;
        res -= (boti-lx)*ly/2;
    }
    else if (lefti > ly+side && boti <= lx+side) {
        //cout << "case 3 " << lefti << " " << boti << endl;
        assert(r*r >= (ly+side)*(ly+side));
        double topi = sqrt(r*r-(ly+side)*(ly+side));
        res += piearea(ly+side, ly, r);
        res -= (boti-lx) * ly / 2;
        res -= side * lx / 2;
        res += (topi-lx) * (ly+side) / 2;
    }
    else {
        //cout << "case 4 " << lefti << " " << boti << endl;
        assert(r*r >= (ly+side)*(ly+side));
        double topi = sqrt(r*r-(ly+side)*(ly+side));
        assert(r*r >= (lx+side)*(lx+side));
        double righti = sqrt(r*r-(lx+side)*(lx+side));
        res += piearea(ly+side, righti, r);
        res -= side * lx / 2;
        res -= side * ly / 2;
        res += (topi-lx) * (ly+side) / 2;
        res += (righti-ly) * (lx+side) / 2;
    }
    return res;
}

int main () {
    int N, i, j, cse=0;
    cin >> N;
    double f, R, t, r, g;
    while (N--) {
        cin >> f >> R >> t >> r >> g;
        double rac = pi * R*R / 4.0;
        double inner1 = R-t, inner2 = R-t-f;
        if (inner2 <= 0) {
            cout << "Case #" << ++cse << ": 1" << endl;
            continue;
        }
        vector<pair<double, double> > vec;
        for (i=0; ;i++) {
            for (j=0; ;j++) {
                double lx=r+(double)i*(g+2*r)+f, ly=r+(double)j*(g+2*r)+f;
                //cout << i << " " << j << " " << lx << " " << ly << endl;
                if (dist2(lx, ly, 0, 0) < inner2*inner2) {
                    vec.push_back(make_pair(lx, ly));
                }
                else break;
            }
            if (j == 0) break;
        }
        double empty = 0;
        if (g > 2*f) {
            for (i=0; i<vec.size(); i++) {
                empty += inarea(vec[i].first, vec[i].second, inner2, g-2*f);
                //cout << vec[i].first << " " << vec[i].second << " " << empty << endl;
            }
        }
        //cout << "empty rac " << empty << " " << rac << endl;
        double p = 1.0 - (double)empty/rac;
        cout << "Case #" << ++cse << ": " << p << endl;
    }
    return 0;
}
