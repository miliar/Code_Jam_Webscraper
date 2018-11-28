#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long ll;
#define REP(i,n) for (int i=0;i<int(n);++i)
const int INF = 1000000000;
const double eps = 1e-9;
vector<double> v;
ll c,d;

bool f(double T) {
    int n = v.size();
    double pos=-INF;//posicio de l'anterior
    for (int i=0;i<n;++i) {
        double di = max(pos+d,v[i]-T);
        if (di>v[i]+T) return 0;
        pos=di;
    }
    return 1;
}



int main() {
    cout.setf(ios::fixed);
    ll ncas;  cin >>ncas;
    for(ll cas=1;cas<=ncas;++cas) {
        cin >> c >> d;
        vector<ll> pos(c),q(c);
        ll n=0;
        ll mx=-INF,mn=INF;
        REP(i,c) {
            cin >> pos[i] >> q[i];
            n+=q[i]; //num_venedors
            mx=max(mx,pos[i]);
            mn=min(mn,pos[i]);
        }
        v = vector<double> (0); //n<=10^6
        REP(i,c) REP(j,q[i]) v.push_back(pos[i]);
        sort(v.begin(),v.end()); //ordenades
        double lo=0,hi=1000000; //HI MOLT MES GRAN!
        while (hi-lo>eps) { //CANVIAR EPS
            double m=(lo+hi)/2;
            if (f(m)) hi=m;
            else lo=m;
        }
        cout <<"Case #" << cas << ": " << lo << endl;
    }
}
