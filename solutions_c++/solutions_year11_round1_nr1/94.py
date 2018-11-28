#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cctype>
#include <climits>
#include <ctime>
#include <cmath>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>
#include <bitset>
#include <iterator>
#include <utility>
#include <algorithm>
#include <numeric>
#include <functional>
#include <complex>

using namespace std;

#define fi first
#define se second
#define sz size()
#define pb push_back
#define ins insert
#define clr clear()
#define FOR(i,a,b) for(typeof(a) i=(a);i<(b);i++)
#define FORE(i,a,b) for(typeof(a) i=(a);i<=(b);i++)
#define EACH(it,A) for(typeof(A.begin()) it=A.begin(); it!=A.end(); it++)
#define ALL(A) A.begin(), A.end()
#define REP(i,n) for(typeof(n) i=1;i<=(n);i++)
#define REPZ(i,n) for(typeof(n) i=0;i<=(n);i++)

typedef vector<int> VI;
typedef pair<int,int> ip;
typedef long long ll;
typedef vector<ip> VP;
typedef vector<string> VS;

ll gcd(ll a, ll b) {
    return b?gcd(b,a%b):a;
}

void do_case(int cn) {
    ll n, pd, pg;
    cin >> n >> pd >> pg;
    string res = "Possible";
    ll miD = 100LL / gcd(100LL,pd);
    if(n < miD) res = "Broken";
    else {
        if(pd != 100 && pg == 100) res = "Broken";
        if(pd != 0 && pg == 0) res = "Broken";
    }
    cout << "Case #" << cn << ": " << res << endl;
}

#define fname "A-large"

int main() {
    freopen(fname ".in", "r", stdin);
    freopen(fname ".out", "w", stdout);
    int T;
    cin >> T;
    REP(it,T) do_case(it);
    return 0;
}
