#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <iomanip>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const int ASCII_SIZE = 256;
typedef long long int LL;

ostream& operator<<(ostream& os, vector<char> v) {
    os << "[";
    for(int i = 0; i < v.size(); ++i) {
        cout << v[i];
        if(i != (v.size() - 1)) {
            os << ", ";
        }
    }
    os << "]";
    return os;
}

int main() {
    ios_base::sync_with_stdio(false);
    int t;
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase) {
        int n;
        cin >> n;
        vector<string> games(n);
        for(int i = 0; i < n; ++i) {
            cin >> games[i];
        }
        vector<long double> WP(n, 0.0);
        vector<long double> wins(n, 0.0);
        vector<long double> played(n, 0.0);
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                if(games[i][j] == '1') {
                    WP[i] += 1.0;
                    wins[i] += 1.0;
                }
                if(games[i][j] != '.') {
                    played[i] += 1.0;
                }
            }
            WP[i] /= played[i];
        }
        vector<long double> OWP(n, 0.0);
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < n; ++j) {
                if(games[i][j] == '1') {
                    OWP[i] += wins[j] / (played[j] - 1.0);
                } else if(games[i][j] == '0') {
                    OWP[i] += (wins[j] - 1.0) / (played[j] - 1.0);
                }
            }
            OWP[i] /= played[i];
        }
        vector<long double> OOWP(n, 0.0);
        for(int i = 0; i <n; ++i) {
            for(int j = 0; j < n; ++j) {
                if(games[i][j] != '.') {
                    OOWP[i] += OWP[j];
                }
            }
            OOWP[i] /= played[i];
        }
        cout << "Case #" << testCase << ": " << endl;
        for(int i = 0; i < n; ++i) {
            cout << fixed << setprecision(12) << 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] << endl;
        }
    }
}
