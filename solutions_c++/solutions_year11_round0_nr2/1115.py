#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, tt, i, j, k, c, d, n;
    cin >> t;
    string tmp;
    for (tt = 1; tt <= t; tt++) {
        vector<string> s1, s2;
        string input;
        s1.clear();
        s2.clear();
        cin >> c;
        char aa;
        for (i = 0; i < c; i++) {
            cin >> tmp;
            s1.push_back(tmp);
            aa = tmp[0];
            tmp[0] = tmp[1];
            tmp[1] = aa;
            s1.push_back(tmp);
        }
        cin >> d;
        for (i = 0; i < d; i++) {
            cin >> tmp;
            s2.push_back(tmp);
            aa = tmp[0];
            tmp[0] = tmp[1];
            tmp[1] = aa;
            s2.push_back(tmp);
        }
        cin >> n >> input;
        string output;
        bool flag;
        int l;
        for (i = 0; i < n; i++) {
            output.push_back(input[i]);
            l = (int)output.size();
            for (j = 0; j < 2 * c; j++)
                if (output[l - 2] == s1[j][0] && output[l - 1] == s1[j][1]) {
                    output.erase(l - 2, 2);
                    output.push_back(s1[j][2]);
                    break;
                }
            l = (int)output.size();
            flag = 0;
            for (j = l - 1; j >= 0; j--) {
                for (k = 0; k < 2 * d; k++) {
                    if (output[j] ==  s2[k][0] && output[l - 1] == s2[k][1]) flag = 1;
                    if (flag) break;
                }
                if (flag) break;
            }
            if (flag) output.clear();
        }
        l = (int)output.size();
        cout << "Case #" << tt << ": [";
        for (i = 0; i < l; i++) {
            if (i != 0) cout << ", ";
            cout  << output[i];
        }
        cout << "]" << endl;
    }
    return 0;
}
