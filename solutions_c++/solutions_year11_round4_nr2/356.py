#include <iostream>
#include <vector>
#include <map>
#include <list>
#include <algorithm>
#include <string>
#include <cmath>

#define D(x)

using namespace std;

template<typename T>
ostream& operator <<(ostream& os, vector<T> v) {
    os << "[";
    for (int i = 0; i < v.size(); i++) {
        if (i > 0) os << ", ";
        os << v[i];
    }
    os << "]";
    return os;
}

vector<vector<int> > prefixsum(const vector<vector<int> >& v, int R, int C) {
    vector<vector<int> > s(R, vector<int>(C));
    
    s[0][0] = v[0][0];
    for (int j = 1; j < C; j++) {
        s[0][j] = v[0][j] + s[0][j-1];
    }
    for (int i = 1; i < R; i++) {
        s[i][0] = v[i][0] + s[i-1][0];
        for (int j = 1; j < C; j++) {
            s[i][j] = v[i][j] + s[i-1][j] + s[i][j-1] - s[i-1][j-1];
        }
    }
    return s;
}

inline int get(vector<vector<int> >& v, int i, int j) {
    if (i > 0 && j > 0) return v[i-1][j-1];
    return 0;
}

int main() {
    int T;

    cin >> T;
    for (int testCase = 1; testCase <= T; testCase++) {
        int R, C, D;
        cin >> R >> C >> D;

        vector<vector<int> > mass(R, vector<int>(C));
        vector<vector<int> > sum(R, vector<int>(C));
        vector<vector<int> > mi(R, vector<int>(C));
        vector<vector<int> > mj(R, vector<int>(C));

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                char c;
                cin >> c;
                mass[i][j] = c - '0';
                mi[i][j] = mass[i][j] * i;
                mj[i][j] = mass[i][j] * j;
            }
        }

        sum = prefixsum(mass, R, C);
        vector<vector<int> > sumi = prefixsum(mi,R,C);
        vector<vector<int> > sumj = prefixsum(mj,R,C);
        D(cerr << mass << endl << sum << endl << sumi << endl << sumj << endl);

        int maxk = 0;

        for (int k = 3; k <= min(R, C); k++) {
            bool found = false;

            for (int i = 0; i <= R-k; i++) {
                for (int j = 0; j <= C-k; j++) {
                    int m = get(sum,i,j) - get(sum,i+k,j) - get(sum,i,j+k) + get(sum,i+k,j+k);
                    m -= mass[i][j] + mass[i+k-1][j] + mass[i][j+k-1] + mass[i+k-1][j+k-1];

                    int mi = get(sumi,i,j) - get(sumi,i+k,j) - get(sumi,i,j+k) + get(sumi,i+k,j+k);
                    mi -= mass[i][j]*i + mass[i+k-1][j]*(i+k-1) + mass[i][j+k-1]*i + mass[i+k-1][j+k-1]*(i+k-1);

                    int mj = get(sumj,i,j) - get(sumj,i+k,j) - get(sumj,i,j+k) + get(sumj,i+k,j+k);
                    mj -= mass[i][j]*j + mass[i+k-1][j]*j + mass[i][j+k-1]*(j+k-1) + mass[i+k-1][j+k-1]*(j+k-1);

                    double xmi = m * (i + (k-1)*0.5), xmj = m * (j + (k-1)*0.5);
                    D(cerr << i << " " << j << " " << k << " " << "m=" << m << " mi=" << mi
                            << " mj=" << mj << " xmi=" << xmi << " xmj=" << xmj << endl);

                    if (mi * 2 == m * (2*i+k-1) && mj * 2 == m * (2*j+k-1)) {
                        maxk = max(maxk, k);
                        found = true; break;
                    }
                }
                if (found) break;
            }
        }

        cout << "Case #" << testCase << ": ";
        if (maxk == 0) {
            cout << "IMPOSSIBLE";
        } else {
            cout << maxk;
        }
        cout << endl;
    }
}

