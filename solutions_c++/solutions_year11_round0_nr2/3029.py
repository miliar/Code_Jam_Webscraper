#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

int t, cs, ds, n;
string C[40], D[30], in, res;
int v[256];

int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);
    scanf("%d", &t);
    for (int cas = 1; cas <= t; cas++) {
        cin >> cs;
        for (int i = 0; i < cs; i++) cin >> C[i];
        cin >> ds;
        for (int i = 0; i < ds; i++) cin >> D[i];
        cin >> n >> in;
        memset(v, 0, sizeof(v));
        res.clear();
        for (int i = 0; i < n; i++) {
            if (res.size() == 0) {
                res.push_back(in[i]);
                v[in[i]]++;
                continue;
            }
            bool flag = false;
            for (int j = 0; j < cs; j++) {
                if ((C[j][0] == in[i] && C[j][1] == res[res.size() - 1]) || (C[j][1] == in[i] && C[j][0] == res[res.size() - 1])) {
                    v[res[res.size() - 1]]--;
                    v[res[res.size() - 1] = C[j][2]]++;
                    flag = true;
                    break;
                }
            }
            if (flag) continue;
            for (int j = 0; j < ds; j++) {
                if ((D[j][0] == in[i] && v[D[j][1]] > 0) || (D[j][1] == in[i] && v[D[j][0]] > 0)) {
                    res.clear();
                    memset(v, 0, sizeof(v));
                }
            }
            if (res.size() > 0) {
                res.push_back(in[i]);
                v[in[i]]++;
            }
        }
        cout << "Case #" << cas << ": [";
        if (res.size() > 0) {
            for (int i = 0; i < res.size() - 1; i++) cout << res[i] << ", ";
            cout << res[res.size() - 1];
        }
        cout << "]" << endl;
    }
    return 0;
}