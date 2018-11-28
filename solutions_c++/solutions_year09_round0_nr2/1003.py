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
char c[110][110];
char letter;

char dfs(int x, int y, int n, int m){
    if(c[x][y]) return c[x][y];
    int wx[]={-1, 0, 0, 1};
    int wy[]={0, -1, 1, 0};
    int iMin=-1;
    REP(i, 4){
        if(x+wx[i]>=0 && y+wy[i]>=0 && x+wx[i]<n && y+wy[i]<m && (iMin==-1 || a[x+wx[i]][y+wy[i]]<a[x+wx[iMin]][y+wy[iMin]])){
            iMin=i;
        }
    }
    if(a[x+wx[iMin]][y+wy[iMin]]>=a[x][y]){
        c[x][y]=letter;
        ++letter;
        return c[x][y];
    }
    return c[x][y]=dfs(x+wx[iMin], y+wy[iMin], n, m);
}

void solve(int test){
    int n, m;
    cin>>n>>m;
    REP(i, n){
        REP(j, m){
            cin>>a[i][j];
            c[i][j]=0;
        }
    }
    letter='a';
    REP(i, n){
        REP(j, m){
            dfs(i, j, n, m);
        }
    }
    cout<<"Case #"<<test<<":"<<endl;
    REP(i, n){
        REP(j, m){
            if(j) cout<<" ";
            cout<<c[i][j];
        }
        cout<<endl;
    }
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
