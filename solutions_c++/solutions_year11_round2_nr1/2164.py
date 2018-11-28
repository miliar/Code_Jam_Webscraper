#include <iostream>

using namespace std;

int N;
char    a[105][105];
double  wp[105];
double  ewp[105][105];
double  owp[105];
double  oowp[105];

void
solve() {
    double      w, l, lw, ll;
    int         i, j;

    for (i=0;i<N;i++) {
        wp[i] = 0;
        w = l = 0;
        for (j=0;j<N;j++) {
            if (a[i][j] == '1') ++w;
            else if (a[i][j] == '0') ++l;
        }
        if (w+l) wp[i] = w / (w+l);
        for (j=0;j<N;++j) {
            lw = w; ll = l;
            if (a[i][j] == '1') lw = lw - 1;
            else if (a[i][j] == '0') ll = ll - 1;
            ewp[i][j] = 0;
            if (lw+ll) ewp[i][j] = lw / (lw+ll);
        }
    }

    for (i=0;i<N;++i) {
        owp[i] = 0; w = 0;
        for (j=0;j<N;++j) {
            if (i!=j) {
                if (a[i][j] != '.') { owp[i] += ewp[j][i]; ++w; }
            }
        }
        owp[i] /= w;
    }

    for (i=0;i<N;++i) {
        oowp[i] = 0; w = 0;
        for (j=0;j<N;++j) {
            if (i!=j) {
                if (a[i][j] != '.') { oowp[i] += owp[j]; ++w; }
            }
        }
        oowp[i] /= w;
    }

    for (i=0;i<N;++i) {
//        cout << wp[i] << " " << owp[i] << " " << oowp[i] << endl;
        cout << (double) (wp[i] / 4 + owp[i] / 2 + oowp[i] / 4) << endl;
    }
}

int main() {
    int     T, i, j;

    cout.precision(12);
    cin >> T;

    for (i=0;i<T;++i) {
        cin >> N;
        for (j=0;j<N;++j) {
            cin >> a[j];
        }
        cout << "Case #" << (i+1) << ":" << endl;
        solve();
    }
    return 0;
}
