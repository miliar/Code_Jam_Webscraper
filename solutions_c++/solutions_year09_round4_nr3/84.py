#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>

using namespace std;

bool comp(const vector<int>& a, const vector<int>& b) {
    return a[0] > b[0];
}

bool f(const vector<int>& a, const vector<int>& b) {
    for(size_t i=0; i<a.size(); i++) {
        if(a[i] <= b[i]) return false;
    }
    return true;
}

bool g[101][101] = {{0}};
int T, n, k;

int f(int x, vector<int>& v) {
    if(x == n) return v.size();

    bool b = false;
    int y = 100000;
    for(int i=v.size()-1; i>=0; i--) {
        if(g[v[i]][x]) {
            b = true;
            int tmp = v[i];
            v[i] = x;
            y = min(y, f(x+1, v));
            v[i] = tmp;
        }
    }


    if(b == false) {
        v.push_back(x);
        y = f(x+1, v);
        v.pop_back();
    }

    return y;
}

int main() {
    cin >> T;
    for(int t=1; t<=T; t++) {
        cin >> n >> k;

        vector<int> p[101];
        for(int i=0; i<n; i++) {
            for(int j=0; j<k; j++) {
                int x;
                cin >> x;
                p[i].push_back(x);
            }
        }

        sort(p, p+n, comp);

        memset(g, 0, sizeof(g));

        for(int i=0; i<n; i++) {
            for(int j=i+1; j<n; j++) {
                g[i][j] = f(p[i], p[j]);
            }
        }

        vector<int> v;

        cout << "Case #" << t << ": " << f(0, v) << endl;
    }
}

