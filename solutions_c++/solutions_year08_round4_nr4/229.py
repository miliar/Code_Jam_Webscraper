#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    for (int cas = 1; cas <= n; cas++) {
        int k;
        scanf("%d", &k);
        char buf[50001]; scanf("%s", buf);
        string s = buf;
        vector<int> p(k);
        for (int i = 0; i < k; i++) p[i] = i;
        int ans = 1000000;
        do {
            int cur = 0;
            char prev = ' ';
            for (int i = 0; i < s.length(); i++) {
                int idx = p[i % k] + i/k*k;
                if (s[idx] != prev) {
                    cur++;
                    prev = s[idx];
                }
            }
            ans <?= cur;
        } while (next_permutation(p.begin(), p.end()));

        printf("Case #%d: %d\n", cas, ans);
    }
}
