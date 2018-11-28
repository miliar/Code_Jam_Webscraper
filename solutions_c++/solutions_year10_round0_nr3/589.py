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

int a[1100];
int r, k, n;
lint remans[1100];
lint remp[1100];

lint iterate(int &i){
    lint sum=0;
    REP(j, n){
        if(sum+a[i]>k) break;
        sum+=a[i];
        ++i;
        if(i==n) i=0;
    }
    return sum;
}

void solve(int test){
    scanf("%d%d%d", &r, &k, &n);
    deque<int> d;
    REP(i, n){
        scanf("%d", &a[i]);
        remans[i]=-1;
    }
    int i=0;
    lint ans=0;
    int p=0;
    do{
        remans[i]=ans;
        remp[i]=p;
        ++p;
        ans += iterate(i);
    } while(remans[i]==-1 && p<r);
    if(p<r){
        lint sump = ans-remans[i];
        lint itp = p-remp[i];
        r -= remp[i];
        ans = remans[i] + sump * (r / itp);
        REP(j, r % itp){
            ans += iterate(i);
        }
    }
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
