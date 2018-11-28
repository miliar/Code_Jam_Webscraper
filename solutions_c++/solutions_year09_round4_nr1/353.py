#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

const int N = 40;

int m[N];
int q[50000]; // small only

inline int getState(const int* m, int n) {
    int r = 0;
    for (int i = 0; i < n; i++) r = (r * 10) + m[i];
    return r;
}

void getArr(int* m, int n, int r) {
    for (int i = n-1; i >= 0; i--) {
        m[i] = r % 10; r /= 10;
    }
}

inline bool target(const int* m, int n) {
    for (int i = 1; i <= n; i++) {
        if (i < m[i-1]) return false;
    }
    return true;
}

int entryPoint(int caseNo) {
    int n; cin >> n;
    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        int j = n-1;
        while (j >= 0 && s[j] == '0') j--;
        m[i] = j+1;
    }

    printf("Case #%d: ", caseNo);

    int s = getState(m, n);
    int get = 0, put = 0;
    set<int> all;
    q[put++] = s; all.insert(s);
    int steps = 0;
    while (get < put) {
        int limit = put;
        while (get < limit) {
            s = q[get++];
            getArr(m, n, s);
            if (target(m, n)) {
                printf("%d\n", steps);
                return 0;
            }

            for (int i = 1; i < n; i++) {
                if (m[i-1] == m[i]) continue;
                int temp = m[i]; m[i] = m[i-1]; m[i-1] = temp;
                int t = getState(m, n);
                if (all.find(t) == all.end()) {
                    all.insert(t); q[put++] = t;
                }
                temp = m[i]; m[i] = m[i-1]; m[i-1] = temp;
            }
        }
        steps++;
    }
    return 0;
}

int main() {
    int cases; cin >> cases;
    for (int caseNo = 1; caseNo <= cases; caseNo++)
        entryPoint(caseNo);
    return 0;
}
