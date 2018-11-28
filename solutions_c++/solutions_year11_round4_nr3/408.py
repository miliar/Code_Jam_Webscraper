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
#define REP(i,n) for(typeof(n) i=0;i<(n);i++)
#define REP1(i,n) for(typeof(n) i=1;i<=(n);i++)

typedef vector<int> VI;
typedef pair<int,int> ip;
typedef long long ll;
typedef vector<ip> VP;
typedef vector<string> VS;

bool P[1<<20];

void pre_calc() {
    memset(P,true,sizeof(P));
    P[0] = P[1] = false;
    for(int i = 2; i*i < (1<<20); i++) if(P[i])
        for(int j = i+i; j < (1<<20); j += i) P[j] = false;
}

void do_case(int cn) {
    ll N;
    cin >> N;
    ll res = (N != 1);
    for(ll i = 2; i*i <= N; i++) if(P[i]) {
        ll k = 0, p = i;
        while(N >= p*i) {
            k++;
            p *= i;
        }
        res += k;
    }
    cout << "Case #" << cn << ": " << res << endl;
}

#define fname "C-large"

int main() {
    pre_calc();
    freopen(fname ".in", "r", stdin);
    freopen(fname ".out", "w", stdout);
    int T;
    cin >> T;
    REP1(it,T) do_case(it);
    return 0;
}
