#include <iostream>
#include <vector>
#include <string.h>
#include <map>
#include <algorithm>
#include <cassert>
#include <sstream>
using namespace std;
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int _; scanf("%d", &_); _;})
#define sz size()
#define pb push_back
#define mkp make_pair
#define INF 1e8
#define MAX 1000
typedef vector<int> VI;

int main() {
    int kases = GI;
    FOR(kase, 1, kases+1) {
        string s;
        cin >> s;
       // cout << s <<" -> ";
        string p = s;
        next_permutation(s.begin(), s.end());
        if(s <= p) {
            string ans = "";
            sort(s.begin(), s.end());
            int cnt = 1, i=0;
            while(i < s.sz && s[i] == '0') i++, cnt++;
            if(i < s.sz) {
                ans += s[i];
                i++;
            }
            while(cnt--) ans += "0";
            while(i < s.sz) ans += s[i], i++;
            s=ans;
        }
        printf("Case #%d: %s\n", kase, s.c_str());
    }
    








}
