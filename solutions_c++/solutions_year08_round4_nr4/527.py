#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int perm[17];

int calc(string &s) {
    char pr = s[0];
    int cnt = 1;
    for (int i=1; i<s.size(); i++) {
        if (s[i] != pr) {
            cnt++;
            pr = s[i];
        }
    }
    return cnt;
}

int main () {
    int N, cs=0;
    cin >> N;
    string s;
    int k, i, j;
    for (i=0; i<16; i++) {
        perm[i] = i;
    }
    while (N--) {
        cin >> k;
        cin >> s;
        int mi = s.size();
        do {
            string tmp = s;
            for (i=0; i<s.size(); i+=k) {
                for (j=0; j<k; j++) {
                    tmp[i+j] = s[i+perm[j]];
                }
            }
            int t = calc(tmp);
            if (t < mi) mi = t;
        }
        while (next_permutation(perm, perm+k));
        cout << "Case #" << ++cs << ": " << mi << endl;
    }
    return 0;
}
