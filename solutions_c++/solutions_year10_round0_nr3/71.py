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
typedef long long ll;
typedef vector<ll> VI;
typedef vector<VI> VVI;
int r,k,n;
void f(vector<ll>& s, ll &ini, ll&val) {
    //Comencant a la posicio "ini", quan puc arribar a sumar?
    ll ac=0;
    if (ini>0) ac=s[ini-1];
    int x = lower_bound(s.begin()+ini,s.end(),ac+k)-s.begin();
    if (x<n and s[x]==ac+k) ++x;
    //x apunta al seguent
    if (x==0) val=ini=0;
    else {
        ini=x;
        val = s[x-1]-ac;
        if (ini==n) { //potser caben mes
            x = lower_bound(s.begin(),s.end(),k-val)-s.begin();
            if (x<n and s[x]==k-val) ++x;
            if (x==0) ini=0;
            else {
                ini=x;
                val+=s[x-1];
            }
        }
    }
}

int main () {
    //vector<int> w;
    //w.push_back(3);
    //int x = lower_bound(w.begin(),w.end(),4)-w.begin();
    //cout << x <<endl;
    
    
    int t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        cin >> r >> k >> n;
        vector<ll> v(n),s(n,0);
        REP(i,n) cin >> v[i];
        s[0]=v[0];
        FOR(i,1,n-1) s[i]=v[i]+s[i-1];
        if (s[n-1]<=k) {
            cout << "Case #" << cas<<": ";
            cout << s[n-1]*r << endl;
        }
        else { //mai hi caben tots
            ll val=0,a=0,b=0;
            ll ans=0;
            VVI memo(n,VI(n,-1));
            vector<ll> ben;
            int mida=-1,i=0,piv;
            for (i=0;i<r;++i) { //r vegades, pero que quan cicli acabo
                a=b;
                f(s,b,val);
                //cerr << " interval de " << a << " a " << (n+b-1)%n << endl;
                int hi = (n+b-1)%n;
                if (memo[a][hi]==-1) {
                    memo[a][hi]=i;
                    ben.push_back(val); //benefici a cada torn
                    ans+=val;
                }
                else { //deteccio del cicle
                    piv =memo[a][hi];
                    mida = i-piv;
                    //cerr << "el torn " << i << " coincideix amb el " << piv << endl;
                    break;
                }
            }
            if (piv!=-1) {
                ll sum=0;
                FOR(j,piv,i-1) sum+=ben[j];
                //sum = benefici de fer un cicle (piv,i)
                ll len = r-i;//els torns que falta fer
                ans+=sum*(len/mida);
                ll residu = len%mida;
                for (i=0;i<residu;++i) {
                    f(s,a,val); //a tenia linterval anterior
                    ans+=val;
                }
            }
            cout << "Case #" << cas<<": " << ans << endl;
        }
    }
}

