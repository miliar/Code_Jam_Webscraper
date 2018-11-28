#include<algorithm>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<map>
#include<list>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<string>
#include<vector>
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,n) for(int i=0;i<(n);++i)
#define fup FOR
#define fdo FORD
#define VAR(v,i) __typeof(i) v=(i)
#define FORE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define ALL(x) (x).begin(),(x).end()
#define SIZE(x) ((int)(x).size())
#define siz SIZE
#define CLR memset((x),0,sizeof (x))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define SQR(a) ((a)*(a))

#define DEBUG 1
#define debug(x) {if(DEBUG) cerr << #x << " = " << x << endl;}
#define debugv(x) {if(DEBUG) {cerr << #x << " = "; FORE(it,(x)) cerr << *it << " . "; cerr  <<endl;}}

using namespace std;
typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef VI vi;
typedef LL lli;

const int inf = 1000000000;

void solve(int tcase) {
    printf("Case #%d: ", tcase);
    int n;
    scanf("%d", &n);
    vector<int> A;
    REP(i,n) {
        int a;
        scanf("%d", &a);
        A.PB(a);
    }
    A.PB(inf);
    sort(ALL(A));
    if (n < 2) {
        printf("%d\n", n);
        return;
    }
    int mn = n;
    list<int> str;
    list<int>::iterator it = str.end();
    int prev = -1;
    REP(i, n+1) {
        if (A[i]!=prev) {
            if (A[i] != prev+1) it = str.begin();
            while(it != str.end()) {
                mn = min(mn, *it);
                list<int>::iterator jt = it;
                ++it;
                str.erase(jt);
            }
            it = str.begin();
            prev = A[i];
        }
        if (it != str.end()) {
            *it = *it + 1;
            ++it;
        } else {
            str.push_front(1);
        }
    }
    printf("%d\n", mn);
}

int main() {
    int t;
    scanf("%d", &t);
    REP(i, t) solve(i+1);
    return 0;
}
