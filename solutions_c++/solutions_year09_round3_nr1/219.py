#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <sstream>
#include <complex>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <climits>
#include <cstdlib>
using namespace std;
#define rep(i,n) for(int i = 0;i < (int)(n); i++)
#define all(a) (a).begin(),(a).end()
#define iter(c) __typeof((c).begin())
#define foreach(i,c) for (iter(c) i = (c).begin(); i != (c).end(); i++)
#define inrange(x,mn,mx) (x >= mn && x < mx)
#define pb push_back
#define mp make_pair

int main() {
    int n;
    cin >> n;
    string trash;
    getline(cin, trash);
    rep(I,n) {
        string s;
        getline(cin, s);
        set<char> chrs;
        rep(i,s.size()) {
            chrs.insert(s[i]);
        }
        int base = chrs.size();
        if (base == 1) base = 2;
        map<char,int> taiou;
        int cur = 0;
        unsigned long long ans = 0;
        rep(i,s.size()) {
            if (taiou.find(s[i]) == taiou.end()) {
                taiou.insert(mp(s[i], (i == 0) ? 1 : cur));
                if (i > 0 && cur == 0) cur += 2;
                else if (i > 0) cur += 1;
                //printf("apply %c as %d\n", s[i], taiou[s[i]]);
            }
            ans *= base;
            ans += taiou[s[i]];
        }
        printf("Case #%d: %lld\n", I+1, ans);
    }
    return 0;
}

