#include<iostream>
#include<limits>
#include<cstring>
#include<algorithm>
#include<set>
#include<utility>

using namespace std;

int a[111][111];

int ABS(int x) {
    return x < 0?-x:x;
}

bool IN(int k, int i, int j) {
    return ABS(i) + ABS(j) < k;
}

int f(int x) {
    return x * x;
}

int main() {
    int T, k;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> k;
        memset(a, 0, sizeof(a));
        for(int i = -k + 1; i < k; i++) {
            int p = k - 1 - ABS(i);
            for(int j = -p; j <= p; j += 2) {
                cin >> a[i + k][j + k];
            }
        }

        set<int> s1, s2;

        for(int i = -k + 1; i < k; i++) {
            int p = k - 1 - ABS(i);
            for(int j = -p; j <= p; j += 2) {
                for(int i2 = i + 2; IN(k, i2, j); i2 += 2) {
                    if(a[i + k][j + k] != a[i2 + k][j + k]) {
                        s1.insert((i + i2) / 2);
                    }
                }
                for(int j2 = j + 2; IN(k, i, j2); j2 += 2) {
                    if(a[i + k][j + k] != a[i + k][j2 + k]) {
                        s2.insert((j + j2) / 2);
                    }
                }
            }
        }

        int n = k;
        for(int i = 0; ; i++) {
            if(s1.find(i) == s1.end() or s1.find(-i) == s1.end()) {
                n += ABS(i);
                break;
            }
        }

        for(int j = 0; ; j++) {
            if(s2.find(j) == s2.end() or s2.find(-j) == s2.end()) {
                n += ABS(j);
                break;
            }
        }
        
        cout << "Case #" << t << ": " << f(n) - f(k) << endl;
    }
}

