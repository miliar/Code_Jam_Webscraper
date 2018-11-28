#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <set>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t; scanf("%d",&t); t;})
#define sz size()
#define pb push_back
#define mkp make_pair

vector<double> v;

#define eps 1e-20
bool range(double p, double a, double delta) {
    return (p-(a-delta) >= -eps && a+delta - p >= -eps);

}
int gap;
bool ok(double t) {
    vector <double> b = v;
    b[0] -= t;
    FOR(i,1,b.sz) {
        double pos1 = b[i-1] + gap;
        if(range(pos1, b[i], t)) b[i] = pos1;
        else b[i] -= t;
    }
    //cout << t <<"\t:"; REP(i,b.sz) cout << b[i] <<" ";  cout << endl;
    REP(i,b.sz-1) {
        if(b[i+1]-b[i] -gap < -eps) return false;
    }
    return true;

}

int main() {
    int kases=GI+1;
    FOR(kase,1,kases) {
        printf("Case #%d: ", kase);
        v.clear();
        int n = GI;
        gap = GI;
        vector < pair<int,int> > p;
        REP(i,n) {
            int a = GI, b = GI;
            p.pb(mkp(a,b));
        }
        sort(p.begin(), p.end());
        REP(i,p.sz) while(p[i].second--) v.pb(p[i].first);
        //REP(i,v.sz) cout << v[i] <<" "; cout << endl;
        double lo = 0, hi = 100000, mid;
        REP(i,50) {
            mid = (lo+hi)/2;
            if(ok(mid)) hi = mid;
            else lo = mid;        
        }
        printf("%10lf\n", mid);
        
        
        
        
        
        
        
    
    }



}

