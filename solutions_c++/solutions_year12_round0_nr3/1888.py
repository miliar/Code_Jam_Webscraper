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
//#include <conio.h>

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

int dd[2000005];
int A, B, T;

string int_str(int x) {
    ostringstream os;
    os << x;
    return os.str();
}

int str_int(string s) {
    istringstream is(s);
    int x;
    is >> x;
    return x;
}

void process(int A, int B) {
    memset(dd, 0, sizeof(dd));
    int res = 0;
    FOR(i, A, B) {
        string s = int_str(i);
        int n = s.length();
        FOR(j, 1, n - 1) {
            s = s.substr(1) + s[0];
            int x = str_int(s);
            if (x <= i || x > B) continue;
            if (dd[x] != i) res++;
            dd[x] = i;
        }
    }
    cout << res << endl;
}

int main () {
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    cin >> T;
    FOR(i, 1, T) {
        printf("Case #%d: ", i);
        cin >> A >> B;
        process(A, B);
    }
    return 0;
}
