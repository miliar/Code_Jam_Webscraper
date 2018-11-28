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

int d;
string words[5500];
int c[20][256];

void solve(int test){
    int ans=0;
    string s;
    cin>>s;
    int p=0;
    REP(j, sz(s)){
        REP(i, 256) c[p][i]=0;
        if(s[j]=='('){
            ++j;
            for(;s[j]!=')';++j) c[p][s[j]]=1;
        }else{
            c[p][s[j]]=1;
        }
        ++p;
    }
    REP(j, d){
        int b=1;
        REP(k, sz(words[j])){
            if(!c[k][words[j][k]]) b=0;
        }
        ans+=b;
    }
    cout<<"Case #"<<test<<": "<<ans<<endl;
}

int main()
{
    freopen("1.in", "r",stdin);
    freopen("1.out", "w",stdout);
    int l;
    cin>>l>>d;
    int n;
    cin>>n;
    REP(i, d){
        cin>>words[i];
    }
    REP(test, n) solve(test+1);
    return 0;
}
