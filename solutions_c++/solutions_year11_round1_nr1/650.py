#include <iostream>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
using namespace std;
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz(x) ((int)((x).size()))
#define rep(i, N) for (int i = 0; i < N; ++i)
#define foreach(it,v) for(__typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define print(x) cerr<<#x<<" = ";pr(x);cerr<<endl;
#define PRC(l,r) pr(l);foreach(it,v)pr(it==v.begin()?"":","),pr(*it);pr(r);
template<class T>void pr(T x){cerr<<x;} 
template<class T>void pr(vector<T>v){PRC('[',']');} 
template<class T1,class T2>void pr(pair<T1,T2>x){pr(x.first);pr(':');pr(x.second);} 
template<class T>void pr(set<T>v){PRC('{','}');} 
template<class T1,class T2>void pr(map<T1,T2>v){PRC('{','}');}
typedef long long lint;
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

lint gcd(lint a, lint b) {
    if (!b) return a;
    return gcd(b, a % b);
}

lint extract(lint p) {
    lint g = gcd(p, 100);
    return 100 / g;
}

void solve(int num) {
    printf("Case #%d: ", num);
    lint N, PD, PG;
    cin >> N >> PD >> PG;
    if (PD != 100 && PG == 100 || PD && !PG) {
        puts("Broken");
        return;
    }
    lint e = extract(PD);
    if (e <= N) {
        puts("Possible");
        return;
    }
/*    for (lint D = 1; D <= N; ++D) {
        if (PD * D % 100 == 0) {
            puts("Possible");
            return;
        }
    }*/
    puts("Broken");
}

int main() {
    int tst;
    cin >> tst;
    for (int i = 1; i <= tst; ++i) 
        solve(i);
    return 0;
}
