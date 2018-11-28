#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <algorithm>
#include <utility>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
//#include <ext/hash_map>

using namespace std;
//using namespace __gnu_cxx;

#define FOR(i, a, n) for(int i=(a); i<(n); ++i)
#define REP(i, n) FOR(i, 0, n)
#define sz(X) int((X).size())
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define all(X) (X).begin(), (X).end()

typedef long long lint;
typedef pair<int, int> PII;
typedef pair<double, double> PDD;
typedef vector<int> VI;

template<class T> ostream &operator<<(ostream &os, vector<T> vec)
{
    os<<'{';
    REP(i, sz(vec)){
        os<<vec[i];
        if (i+1!=sz(vec)) os<<',';
    }
    os<<'}';
    return os;
}

template<class T1, class T2> ostream &operator<<(ostream &os, pair<T1, T2> par)
{
    os<<'('<<par.X<<','<<par.Y<<')';
    return os;
}

void solve(int test){
    int n;
    cin>>n;
    lint x=0, y=0, z=0, vx=0, vy=0, vz=0;
    REP(i, n){
        lint x1, y1, z1, vx1, vy1, vz1;
        cin>>x1>>y1>>z1>>vx1>>vy1>>vz1;
        x+=x1;
        y+=y1;
        z+=z1;
        vx+=vx1;
        vy+=vy1;
        vz+=vz1;
    }
    double d, t;
    if(vx==0 && vy==0 && vz==0 || vx*x + vy*y + vz*z>0){
        d=sqrt(1.0*x*x+1.0*y*y+1.0*z*z);
        t=0;
    }else{
        t=-(vx*x + vy*y + vz*z)/(1.0*vx*vx+1.0*vy*vy+1.0*vz*vz);
        d=sqrt((x+vx*t)*(x+vx*t) + (y+vy*t)*(y+vy*t) + (z+vz*t)*(z+vz*t));
    }
    d/=n;
    cout<<"Case #"<<test<<": "<<d<<" "<<t<<endl;
}

int main()
{
    freopen("1.in", "r",stdin);
    freopen("1.out", "w",stdout);
    cout<<fixed;
    cout.precision(8);
    int n;
    cin>>n;
    REP(test, n) solve(test+1);
    return 0;
}
