#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <complex>
#include <utility>
#include <iomanip>
#include <algorithm>
#include <functional>
using namespace std;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vst;
typedef pair<int,int> pint;
typedef long long ll;

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define all(s) (s).begin(),(s).end()
#define each(i,s) for (typeof((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define debug(x) cout<<#x<<" = "<<(x)<<" (L"<<__LINE__<<")"<<endl
template<class T> void print(T P[], int n) {cout<<"{ ";for(int i=0;i<n;++i){if(i>0)cout<<", ";cout<<P[i];}cout<<" }"<<'\n';}
template<class T> void print(T P[][100], int n, int m) {for(int i=0;i<n;++i){cout<<i<<" : ";print(P[i],m);}}
template<class T1, class T2> ostream& operator<<(ostream &s, pair<T1,T2> P){return s<<'<'<<P.first<<", "<<P.second<<'>';}
template<class T> ostream& operator<<(ostream &s, vector<T> P) {s<<"{ ";for(int i=0;i<P.size();++i){if(i>0)s<<", ";s<<P[i];}return s<<" }"<<endl;}

int N;
ll d[20000];
ll l[20000];
ll D;
bool used[20000];

string solve() {
    ll Max = 0;
    int mi = 0;
    queue<pair<int, ll> > que;
    que.push(mp(0, d[0]));   // fi:i番目、se:そこからの到達距離
    while (que.size()) {
        pair<int, ll> q = que.front();
//        debug(q);
        que.pop();
        used[q.fi] = true;
        Max = max(Max, d[q.fi] + q.se);
        if (Max >= D) return "YES";
        for (int i = mi; i < N; ++i) {
            if (!used[i] && d[i] <= Max) {
                que.push(mp(i, min(d[i]-d[q.fi], l[i])));
                mi = i+1;
            }
        }
    }
    
    return "NO";
}

int main() {
    freopen( "/Users/macuser/Downloads/A-large(1).in", "r", stdin );
    freopen( "/Users/macuser/Downloads/Al.txt", "w", stdout );
    
    int T;
    scanf("%d", &T);
    for (int id = 1; id <= T; ++id) {
        cin >> N;
        memset(d, 0, sizeof(d));
        memset(l, 0, sizeof(l));
        memset(used, 0, sizeof(used));
        for (int i = 0; i < N; ++i) {
            int dtemp, ltemp;
            cin >> dtemp >> ltemp;
            d[i] = dtemp;
            l[i] = ltemp;
        }
        cin >> D;
        
        printf("Case #%d: ", id);
        cout << solve();
        printf("\n");
    }
    
    return 0;
}








