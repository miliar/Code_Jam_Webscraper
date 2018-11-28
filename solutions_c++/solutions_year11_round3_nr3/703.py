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
typedef std::vector<int> VI;
typedef std::vector<VI> VVI;
typedef std::vector<string> VS;
typedef long long ll;

typedef pair<int,int> ii;
#define cons(x,y) make_pair((x),(y))
#define car(x) ((x).first)
#define cdr(x) ((x).second)
#define caar(x) (x).first.first
#define cdar(x) (x).first.second
#define cadr(x) (x).second.first
#define cddr(x) (x).second.second

//BEGINCUT
// (yas/expand-link "topcoder")
// (yas/expand-link "timer")
// (yas/expand-link "math")
// (yas/expand-link "tco2")
// (yas/expand-link "split")
// (yas/expand-link "join")
// (yas/expand-link "bigint")
// (yas/expand-link "pair_opr")
// (yas/expand-link "conversion")
// (yas/expand-link "myalgorithm")
#include <cout.hpp>
//ENDCUT

//NODEBUG
int T;
int main() {
    cin >> T;
    int N, L, H;
    rep(t, T){
        cin >> N >> L >> H;
        vector<int> notes(N);
        rep(i, N){
            cin >> notes[i];
        }
        
        // => notes
        ll ret=-1;
        ll tmp=0;
        REP(i, L, H+1){
            // => i
            bool ok=true;
            rep(j, N){
                // => notes[j] | i%notes[j]
                if(i>=notes[j]){
                    if(i%notes[j] != 0){ok=false; break; }
                }else{
                    if(notes[j]%i != 0){ok=false; break; }
                }
                
            }
            if(ok){
                ret=i;
                break;
            }
        }
        
        printf("Case #%d: ", t+1);
        if(ret == -1){
            cout << "NO";
        }else{
            cout << ret;
        }
        cout << endl;
    }
    return 0;
}
