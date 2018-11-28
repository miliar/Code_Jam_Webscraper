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

#define REP(i,n) for(int i=0;i<int(n);++i)
#define FOR(i,a,b) for(int i=a;i<=b;++i)
typedef vector<int> VE;
typedef vector<VE> VVE;
typedef vector<VVE> VVVE;

int del,ins,m,n;
vector<int> v;
VVVE memo;

//inserting before first or after last is never needed on optimal sol
//waste of money!
const int INF = 1000000000;

//Inserto abans de p
//Borro exactament p
//Val es anterior o 256 si no hi ha res

//len indica que he intentat (insert, change, delete, deixar=)
int f(int val, int len, int p) { //la empty array es valida
    if (p==n) return 0;
    if (len>=250) return INF;
    //cout << val << " " << p << endl;
    int &ans=memo[val][len][p];
    if (ans>=0) return ans;
    ans=INF;
    //insert
    REP(col,256) if (val==256 or abs(val-col)<=m) ans=min(ans, ins+f(col,len+1,p));
    //delete
    ans=min(ans, del+f(val,len,p+1));
    //change
    REP(col,256) if (val==256 or abs(val-col)<=m) ans=min(ans, abs(col-v[p])+f(col,len+1,p+1));
    //deixar =
    if (val==256 or abs(val-v[p])<=m) ans=min(ans, f(v[p],len+1,p+1));
    //cout << "# " << val << " " << p << " -> " << ans << endl;
    return ans;
}

int main () {
    int t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        cin >> del >> ins >> m >> n;
        v=vector<int>(n);
        REP(i,n) cin >> v[i];
        memo=VVVE (257,VVE(250,VE(101,-2))); //-2 no vist, INF vist, >=0 valor
        cout <<"Case #" <<cas << ": ";
        cout << f(256, 0, 0) << endl; //256 vol dir que no hi ha anterior
    }
}
