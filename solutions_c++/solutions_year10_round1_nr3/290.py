#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <complex>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <string.h>
using namespace std;
#define x first
#define y second
#define REP(i,n) for(int i=0;i<int(n);++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
typedef pair<int,int> PII;

map<PII,int> m;

int f(int a, int b) {
    if (a<0 or b<0) return 0;
    if (a==1 and b>1) return 1;
    if (b==1 and a>1) return 1;
    if (a==1 and b==1) return 0;
    if (m.count(PII(a,b))) return m[PII(a,b)];
    if (m.count(PII(b,a))) return m[PII(b,a)];
    
    for (int k=1;a-k*b>0;++k) if (f(a-k*b,b)==0) return m[PII(a,b)]=1;
    for (int k=1;b-k*a>0;++k) if (f(a,b-k*a)==0) return m[PII(a,b)]=1;
    return m[PII(a,b)]=0;
}

int main () {
    int a1,a2,b1,b2;
    int t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        cout <<"Case #" <<cas << ": ";
        cin >> a1 >> a2 >>b1  >>b2;
        int ans=0;
        for (int a=a1;a<=a2;++a) for (int b=b1;b<=b2;++b) ans+=f(a,b);
        cout << ans << endl;
    }
}
