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

char buf[110];

void solve(int test){
    set<string> s;
    int n, m;
    scanf("%d%d", &n, &m);
    REP(i, n){
        scanf(" %s", buf);
        s.insert(buf);
    }
    int ans=-sz(s);
    REP(i, m){
        scanf(" %s", buf);
        for(int j=0; buf[j]; ){
            ++j;
            while(buf[j]!='/' && buf[j]!=0) ++j;
            char ch = buf[j];
            buf[j]=0;
            s.insert(buf);
            buf[j]=ch;
        }
    }
    ans+=sz(s);
    cout<<"Case #"<<test<<": ";
    cout<<ans;
    cout<<endl;
}

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int n;
    cin>>n;
    REP(test, n) solve(test+1);
    return 0;
}
