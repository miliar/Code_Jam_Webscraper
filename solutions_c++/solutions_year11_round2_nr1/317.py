#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <map>
#include <cmath>

#define mp make_pair

using namespace std;

typedef long long ll;
typedef long double ld;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int i, j;
    int n, T, t;
    cin>>T;
    vector<string> v;
    vector<int> win, games;
    vector<double> wp, owp, oowp;
    string s;
    for(t=1; t<=T; ++t) {
        cin>>n;
        v.clear();
        v.resize(n);
        win.clear();
        win.resize(n, 0);
        games.clear();
        games.resize(n, 0);
        wp.clear();
        owp.clear();
        oowp.clear();
        for(i=0; i<n; ++i) {
            cin>>v[i];
        }
        for(i=0; i<n; ++i) for(j=0; j<n; ++j) {
            if (v[i][j] != '.') {
                win[i] += v[i][j] - '0';
                games[i]++;
            }
        }
        for(i=0; i<n; ++i) {
            wp.push_back(1.0 * win[i] / games[i]);
        }
        for(i=0; i<n; ++i) {
            double r = 0.0;
            int c = 0;
            for(j=0; j<n; ++j) {
                if (v[i][j] != '.') {
                    int owins = win[j] - (v[j][i] - '0');
                    r += 1.0 * owins / (games[j]-1);
                    c++;
                }
            }
            r /= c;
            owp.push_back(r);
        }
        for(i=0; i<n; ++i) {
            double r = 0.0;
            int c = 0;
            for(j=0; j<n; ++j) {
                if (v[i][j] != '.') {
                    r += owp[j];
                    c++;
                }
            }
            oowp.push_back(r / c);
        }
        cout<<"Case #"<<t<<":"<<endl;
        for(i=0; i<n; ++i) {
            cout<<0.25*wp[i] + 0.5*owp[i] + 0.25 * oowp[i]<<endl;
        }
    }
    return 0;
}
