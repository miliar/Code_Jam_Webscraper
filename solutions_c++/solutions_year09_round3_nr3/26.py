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

int a[110];
int d[110][110];

void solve(int test){
    int n, m;
    cin>>n>>m;
    REP(i, m){
        cin>>a[i+1];
    }
    a[0]=0;
    a[m+1]=n+1;
    REP(l, m+2){
        if(l<=1){
            REP(i, m-l+2){
                d[i][i+l]=0;
            }
            continue;
        }
        REP(i, m-l+2){
            int x=1000000000;
            REP(k, l-1){
                x=min(x, d[i][i+k+1]+d[i+k+1][i+l]);
            }
            d[i][i+l]=x+a[i+l]-a[i]-2;
        }
    }
    int ans=d[0][m+1];
    cout<<"Case #"<<test<<": "<<ans<<endl;
}

int main()
{
    freopen("1.in", "r",stdin);
    freopen("1.out", "w",stdout);
    int n;
    cin>>n;
    REP(test, n) solve(test+1);
    return 0;
}
