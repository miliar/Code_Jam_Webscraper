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

int c[550][550];
int a[550][550];
int b[550];

void solve(int test){
    int n;
    scanf("%d", &n);
    int ans = b[n];
    cout<<"Case #"<<test<<": ";
    cout<<ans;
    cout<<endl;
}

void init(int N){
    REP(i, N+1){
        REP(j, i+1){
            if(i==0) c[i][j] = 1;
            else c[i][j] = ((j? c[i-1][j-1]: 0) + c[i-1][j]) % 100003;
        }
    }

    FOR(n, 1, N+1){
        b[n] = 0;
        FOR(k, 1, n){
            int ans=1;
            FOR(j, 1, k-1){
                ans = (ans + (lint) c[n-k-1][k-j-1] * a[k][j]) % 100003;
            }
            a[n][k] = ans;
            b[n] = (b[n] + a[n][k]) % 100003;
        }
    }
}

int main()
{
    init(500);
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int n;
    cin>>n;
    REP(test, n) solve(test+1);
    return 0;
}
