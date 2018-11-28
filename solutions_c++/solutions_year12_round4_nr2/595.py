#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <utility>
#include <iomanip>

#define SQR(x) ((x) * (x))
#define EPS (1e-7)

using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

int w, l, n;

double x[10000], y[10000], r[10000], a[10000];
double ax[10000], ay[10000];
int z[10000];
int tot;

pair<double, int> tmp[10000];

double getdist(double x0, double y0, double x1, double y1) {
    return sqrt(SQR(x1 - x0) + SQR(y1 - y0));
}

bool check(double x0, double y0, double r0) {
    for (int i = 1; i <= tot; ++i) {
        if (getdist(x0, y0, x[i], y[i]) <= r0 + r[i] + EPS)
            return false;
    }
    return true;
}

bool check_ans() {
    tot = 0;
    double ym = 0;
    for (int i = n; i >= 1; --i) {
        double px, py;
        if (i == n) {
            px = 0; py = 0;
        }
        else {
            px = x[tot] + r[tot] + a[i] + EPS;
            py = y[tot];
            if (px > w) {
                px = 0;
                py = ym + a[i] + EPS;
            }
        }
        if (py > l) return false;
        ++tot;
        x[tot] = px; y[tot] = py; r[tot] = a[i]; z[tot] = tmp[i].second;
        ym = max(ym, py + a[i]);
    }
    return true;
}

void random_a() {
    for (int i = 0; i < 100; ++i) {
        int t1, t2;
        t1 = rand() % n + 1;
        t2 = rand() % n + 1;
        swap(a[t1], a[t2]);
    }
}

int main() {
    srand(time(NULL));
    int total;
    fin >> total;
    for (int now_case = 1; now_case <= total; ++now_case) {
        fout << "Case #" << now_case << ": ";
        fin >> n >> w >> l;
        for (int i = 1; i <= n; ++i) {
            fin >> a[i];
            tmp[i] = make_pair(a[i], i);
        }
        sort(tmp + 1, tmp + 1 + n);
        for (int i = 1; i <= n; ++i) a[i] = tmp[i].first;
        while (!check_ans()) random_a();
        for (int i = 1; i <= n; ++i) {
            ax[z[i]] = x[i];
            ay[z[i]] = y[i];
        }
        fout.precision(16);
        for (int i = 1; i <= n; ++i)
            fout << ax[i] << ' ' << ay[i] << ' ';
        fout << endl;
    }
}