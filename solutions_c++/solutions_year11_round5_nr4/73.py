#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <conio.h>

using namespace std;

#define oo 1000000000
#define fi first
#define se second
#define sqr(a) ((a)*(a))
#define FR(i,n) for (int i = 0; i < (n); i++)
#define DN(i,a) for(int i = (a)-1; i >= 0; i--)
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)

typedef pair<int, int> PII;
typedef vector<int> VI;

string s, res;
int a[100], num, nTest;
bool ok;

bool check() {
    int l = s.length();
    long long x = 0;
    FR(i, l) {
        if (s[i] =='1') x = x * 2 + 1; else x = x * 2;   
    }
    long long y = (long long) sqrt(x);
    if (x == y * y) {
//        cout << x << ' ' << y << endl;
        return true;
    }
    return false;
}

void recruise(int i) {
    if (ok) return;
    if (i > num) {
        if (check()) {
            ok = true;
            res = s;
        }   
        return;
    }    
    FOR(j, '0', '1') {
        s[a[i]] = j;
        recruise(i + 1);   
    }
}

int main () {
    freopen("d.in", "r", stdin);
    freopen("test.out", "w", stdout);
    cin >> nTest;
    FOR(test, 1, nTest) {
        cin >> s;
        int l = s.length();
        num = 0;
        FR(i, l) {
            if (s[i] == '?') a[++num] = i;   
        }
        ok = false;
        recruise(1);
        printf("Case #%d: ", test);
        cout << res << endl;
    }
    return 0;   
}
