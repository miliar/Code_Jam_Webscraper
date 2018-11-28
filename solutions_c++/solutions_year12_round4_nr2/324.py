#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <cmath>
using namespace std;

typedef pair<int, int> P;

const int N = 20000;
const double eps = 1e-8;

int T, W, L, r[N], n;
P arr[N];
int rx[N], ry[N];
int pos[N];
bool check(int i) {
        for(int j = 0; j < i; j ++) {
            double dx = fabs(rx[i] - rx[j]);
            double dy = fabs(ry[i] - ry[j]);
            if(sqrt(dx * dx + dy * dy) < arr[i].first + arr[j].first - eps) return false;
            if(rx[i] > W) return false;
            if(ry[i] > L) {
                return false;
            }
        }
    return true;
}

bool check() {
    for(int i = 0; i < n; i ++) {
        if(!check(i)) {
            return false;
        }
    }
    return true;
}

bool solve() {
    rx[0] = ry[0] = 0;
    int cur_h = arr[0].first;
    int cur_y = 0;
    int cur_w = arr[0].first;
    for(int i = 1; i < n; i ++) {
        rx[i] = 0; ry[i] = 0;
        for(int j = 0; j < i && !check(i); j ++) {
            rx[i] = rx[j] + arr[i].first + arr[j].first;
            ry[i] = ry[j];
        }
        //cerr << (int)check(i) << endl;
        for(int j = 0; j < i && !check(i); j ++) {
            rx[i] = rx[j];
            ry[i] = ry[j] + arr[i].first + arr[j].first;
        }
    }
    if(L - cur_h + arr[n-1].first < 0) return false;
    return true;
}

int main() {
    cin >> T;
    for(int I = 1; I <= T; I ++) {
        cin >> n >> W >> L;
        for(int i = 0; i < n; i ++) {
            cin >> arr[i].first;
            arr[i].second = i;
        }
        sort(arr, arr + n);
        reverse(arr, arr + n);
        if(!solve()) {
            swap(L, W);
            if(!solve()) cerr << "FAIL" << endl;
            for(int i = 0; i < n; i ++) {
                swap(rx[i], ry[i]);
            }
            swap(L, W);
        }
        cerr << (check() ? "OK" : "NOK") << endl;
        for(int i = 0; i < n; i ++) {
            pos[arr[i].second] = i;
        }
        cout << "Case #" << I << ":";
        for(int i = 0; i < n; i ++) {
            cout << " " << rx[pos[i]] << " " << ry[pos[i]];
        }
        cout << endl;
    }
    return 0;
}
