#include <iostream>
#include <string>

using namespace std;

int k;
string s;
int best;

int p[5];
bool v[5];
char ss[1000];

void go(int idx) {
    if (idx == k) {
        for (int i = 0; i < s.size(); i += k) {
            for (int j = 0; j < k; j++) {
                ss[i+j] = s[i+p[j]];
            }
        }
        int cnt = 1;
        int prev = ss[0];
        for (int i = 1; i < s.size(); i++) {
            if (ss[i] != prev) cnt++;
            prev = ss[i];
        }
        best <?= cnt;
        return;
    }
    for (int i = 0; i < k; i++) {
        if (v[i]) continue;
        v[i] = true;
        p[idx] = i; go(idx+1);
        v[i] = false;
    }
}

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        cin >> k >> s;

        best = 200000;
        for (int i = 0; i < k; i++) v[i] = false;
        go(0);
        cout << "Case #" << t << ": " << best << endl;
    }
    return 0;
}

