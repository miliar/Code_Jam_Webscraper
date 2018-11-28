/*
  Name:
  Author: 3T //mailto:kasparovandme@gmail.com
  Date:
  Description:
  Time Limit:
*/

#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define REP(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

#define BIT(n) (1<<(n))
#define AND(a,b) ((a) & (b))
#define OR(a,b) ((a) | (b))
#define XOR(a,b) ((a) ^ (b))
#define sqr(x) ((x) * (x))

#define PI 3.1415926535897932385
#define INF 1000111222
#define EPS 1e-7
#define MAXN 100000

#define INP "A-small-attempt0.in"
#define OUT "A-small-attempt0.out"

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

int n, t, a, b, c, bitmask;
int Pow2[] = {1, 2, 4, 8, 16};
double p[MAXN + 5], ans, pp[100];

bool check(int bm, int del){
    //cout << "dang check " << bm << " " << del;
    if(del == a) return true;
    int tmp = a - del;
    //cout << tmp << endl;
    REP(i, tmp) if(!(bm & (1 << i))) return false;
    return true;   
}

void solve(){
    //memset(pp, 0.0, sizeof pp);
    ans = 1112223334.111;
    int lim = Pow2[a];
    REP(bitmask, lim){
        double tmp = 1.0;
        REP(i, a){
            if(bitmask & (1 << i)) tmp *= p[i];
            else tmp *= (1 - p[i]);    
        }      
        pp[bitmask] = tmp;
    }
    REP(i, a + 1){
        double tmp = 0.0;
        REP(bitmask, lim){
            if(check(bitmask, i)) {tmp = tmp + (i + b - a + i + 1) * pp[bitmask]; /*cout << " t" <<(i + b - a + i + 1) << endl;*/}
            else {tmp = tmp + (i + b - a + i + 1 + b + 1) * pp[bitmask];  /*cout << " f" << (i + b - a + i + 1 + b + 1)<< endl;*/} 
            //cout << pp[bitmask] << endl;

        }  
        //cout <<"wtf" << tmp << endl;
        ans = min(ans, tmp);  
    }
    //ko xoa
    double tmp = b + 2;
    ans = min (ans, tmp);
             
}

int main () {
    freopen(INP, "r", stdin); freopen(OUT, "w", stdout);
    scanf("%d", &t);
    FOR(j, 1, t){
        scanf("%d %d", &a, &b);
        REP(i, a) cin >> p[i];  
        solve();
        printf("Case #%d: %.6lf\n", j, ans);      
    }

    return 0;
}
