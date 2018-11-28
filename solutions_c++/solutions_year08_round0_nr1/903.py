#include <vector>
#include <cstdio>
#include <string>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <set>
using namespace std;

int main() {
    int n;
    string str;
    getline(cin, str);
    n = atoi(str.c_str());
    for (int cas = 1; cas <= n; cas++) {
        int S, Q;
        getline(cin, str);
        S = atoi(str.c_str());
        vector<string> engines;
        for (int i = 0; i < S; i++) {
            getline(cin, str);
            engines.push_back(str);
        }
        getline(cin, str);
        Q = atoi(str.c_str());
        vector<string> q(Q);
        for (int i = 0; i < Q; i++) {
            getline(cin, q[i]);
        }
        
        vector<vector<int> > ans(Q+1, vector<int>(S, 1000000));
        for (int i = 0; i < S; i++) {
            ans[0][i] = 0;
        }

        for (int i = 0; i < Q; i++) {
            for (int s = 0; s < S; s++) {
                int w = 1000000;
                if (q[i] != engines[s]) {
                    for (int t = 0; t < S; t++) {
                        if (s != t) {
                            w <?= ans[i][t]+1;
                        } else {
                            w <?= ans[i][t];
                        }
                    }
                }
                ans[i+1][s] = w;
            }
        }
        
        int answer = 1000000;
        for (int i = 0; i < S; i++) {
            answer <?= ans[Q][i];
        }
        printf("Case #%d: %d\n", cas, answer);
    }
}

