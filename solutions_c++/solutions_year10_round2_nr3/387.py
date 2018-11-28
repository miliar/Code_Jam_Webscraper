#include <iostream>
#include <cstdio>

using namespace std;

int b[32];

int T;
int n;
int ans[32];

bool check() {
    int k = n;
    b[n] = 1;
    b[1] = 1;
    while(k != 1) {
        int total = 0;
        for(int i = 2; i <= k; i++) {
            if(b[i] == 1) {
                total++;
            }
        }
        if(b[total] == 0) {
            return false;
        }
        k = total;
    }
    return true;
}

void calc(int dep) {
    if(dep >= n) {
        if(check()) {
            ans[n]++;

            // for(int i = 2; i <= n; i++) {
            //     if(b[i]) {
            //         cout << i << " ";
            //     }
            // }
            // cout << endl;
        }
        return;
    }

    for(int i = 0; i < 2; i++) {
        b[dep] = i;
        calc(dep+1);
    }
}

int main() {
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> n;
        if(ans[n] == 0) {
            calc(2);
        }
        cout << "Case #" << t << ": " << (ans[n] % 100003) << endl;
    }
    return 0;
}
