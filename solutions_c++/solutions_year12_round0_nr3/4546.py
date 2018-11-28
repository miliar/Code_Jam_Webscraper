#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <sstream>
using namespace std;

#define pb push_back
#define sz size()
string s;
int t, a, b;
map<char, char> mp;

int ok(int x) {
    vector<int> res;
    int cntx = 0;
    while (x) {
        res.pb(x%10);
        x /= 10;
        cntx++;
    }
    reverse(res.begin(), res.end());
    vector<int> res2 = res;
    cntx--;
    int ans = 0;
    map<int, bool> mp;
    int t2 = res2.sz;
    while (cntx) {
        vector<int> res3;
        int res3int = 0;
        for (int i  = 1; i < t2; i++) {
            res3.pb(res2[i]);
            res3int = res3int * 10 + res2[i];
        }
        res3.pb(res2[0]);
        res3int = res3int * 10 + res2[0];
        if (res3int <= b && res3int >= a) {
            bool same = true;
            for (int i = 0; i < t2; i++) {
                if (res[i] != res3[i]) {
                    same = false;
                    break;
                }
            }
            if (!same) {
                if (res3[0] != 0) {
                    if (mp[res3int] == 0) {                    
                        mp[res3int] = 1;
                        ans++;
                    }
                }
            }
        }
        res2 = res3;
        cntx--;
    }
    return ans;
}

int main() {
    freopen("c-small.in", "r", stdin);
    freopen("c-small.out", "w", stdout);
    scanf("%d", &t);
    int xx = 1;
    while (t--) {
        scanf("%d%d", &a, &b);
        int ans = 0;
        for (int i = a; i <= b; i++) ans += ok(i);
        printf("Case #%d: %d", xx++, ans / 2);
        printf("\n");
    }
    return 0;
}
