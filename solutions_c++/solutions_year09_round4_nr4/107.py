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

double x[44], y[44], r[44];

void solve(int test){
    int n;
    cin>>n;
    REP(i, n){
        cin>>x[i]>>y[i]>>r[i];
    }
    double ans;
    if(n==1){
        ans=r[0];
    }
    if(n==2){
        ans=max(r[0], r[1]);
    }
    if(n==3){
        ans=1e100;
        REP(i, 3){
            int j=(i+1)%3, k=(i+2)%3;
            ans=min(ans, max(r[i], (r[j]+r[k]+hypot(x[j]-x[k], y[j]-y[k]))/2));
        }
    }
    cout<<"Case #"<<test<<": ";
    cout<<ans;
    cout<<endl;
}

int main()
{
    cout.precision(8);
    cout<<fixed;
    freopen("1.in", "r",stdin);
    freopen("1.out", "w",stdout);
    int n;
    cin>>n;
    REP(test, n) solve(test+1);
    return 0;
}
