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

int a[110][110];
int g[110][110];
int r[110];
int were[110];

int dfs(int v, int n){
    if(were[v]) return 0;
    were[v]=1;
    REP(i, n) if(g[v][i]) {
        if(r[i]==-1 || dfs(r[i], n)){
            r[i]=v;
            return 1;
        }
    }
    return 0;
}

int pairs(int n){
    int ans=0;
    REP(j, n) r[j]=-1;
    REP(i, n){
        REP(j, n) were[j]=0;
        if(dfs(i, n)) ++ans;
    }
    return ans;
}

void solve(int test){
    int n, m;
    cin>>n>>m;
    REP(i, n){
        REP(j, m){
            cin>>a[i][j];
        }
    }
    REP(i, n){
        REP(j, n){
            g[i][j]=0;
        }
    }
    REP(i, n){
        REP(j, n){
            int b=1;
            REP(k, m){
                if(a[i][k]>=a[j][k]){
                    b=0;
                }
            }
            g[i][j]=b;
        }
    }
    int ans=n-pairs(n);
    cout<<"Case #"<<test<<": ";
    cout<<ans;
    cout<<endl;
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
