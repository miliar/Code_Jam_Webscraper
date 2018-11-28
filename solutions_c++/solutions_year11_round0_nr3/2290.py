//0x
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
using namespace std;

#define CLR(a, n) memset((a), n, sizeof(a))
#define arlen(x) sizeof x / sizeof x[0]
#define len(a)  int((a).size())
#define all(x) (x).begin(), (x).end()
#define rall(c) (c).rbegin(), (c).rend()
#define has(s, val) (find(all(s), val)!=(s).end())
#define EXIST(s,e)  ((s).find(e)!=(s).end())
#define REMOVE(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define rep(i,n)  REP(i,0,n)
#define REP(i,a,b) for(int i=(a);i<(b);++i)
#define SORT(c) sort(all(c))
#define pb push_back
#define mp make_pair
const int INF=1<<29;
const double EPS=1e-9;
typedef long long ll;
typedef std::vector<ll> VI;

// #include <cout.hpp>

int T, N;
string intToString(ll number)
{
  stringstream ss;
  ss << number;
  return ss.str();
}

ll pat(VI v){
    ll ret=0;
    for(int i=21; i>=0; i--){
        int c=0;
        rep(j, len(v)){
            if((v[j] & (1 << i))){
                c++;
            }
        }
        if(c==1) ret+=(1<<i);
    }
    
    return ret;
}

bool equalpatric(VI seansv, VI patricksv){
    return pat(seansv) == pat(patricksv);
}

int main(){
    cin >> T;
    rep(t, T){
        // CLR(C, 0);
        cin >> N;
        vector<int> C(N);
        rep(i, N){
            cin >> C[i];
        }

        ll ans = -1;
        ll a, b, a2, b2;
        
        sort(all(C), greater<int>());
        REP(i, 1 , len(C)){
            a=0,  b=0;
            a2=-1, b2=-1;
            rep(x, i){
                a+=C[x];
                if(a2==-1) a2 = C[x];
                else a2 ^= C[x];
            }
            
            REP(x, i, len(C)){
                b += C[x];
                if(b2==-1) b2 = C[x];
                else b2 ^= C[x];
            }
            
            // a | b | a2 | b2
            if(a2 == b2){
                ans = max(ans, max(a, b));
                // ans
            }
        }
        printf("Case #%d: ", t+1);
        if(ans == -1){
            cout << "NO";
        }else{
            cout << ans;
        }
        cout << endl;
    }
}
