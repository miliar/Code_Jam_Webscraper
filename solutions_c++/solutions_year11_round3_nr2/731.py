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
    ll L, tm, N, C;
    rep(t, T){
        // => T
        cin >> L >> tm >> N >> C;
        // => L | tm | N | C
        vector<int> a(C);
        vector<int> stars(N);
        rep(i, C) cin >> a[i];
        
        rep(i, N){
            stars[i]=a[i%C];
        }

        ll hours=0;
        int idx=0;

        if(L!=0){
//        // => L | tm | stars
        
        int distance_til_completed = tm*0.5;

//        // => distance_til_completed
        
        int distance_til_completed_1 = distance_til_completed;
        int s=0;
        rep(i, N){
            idx=i;
            s += stars[i];
//            // => s | distance_til_completed
            if(distance_til_completed>=s){
//                // => "ひく"
                distance_til_completed-=s;
                rep(j, i+1){
                    stars[j]=0;
                }
                s=0;
            }else{
//                // => "とちゅうまで"
                stars[i] -= distance_til_completed;
                distance_til_completed = 0;
                break;
            }
            // => stars | distance_til_completed
        }
        
        hours = tm;
        // => idx | stars | distance_til_completed | hours
        }
        
        //残りに対してスピードアップさせてから
        vector<int> stars2(stars.begin()+idx, stars.end());
        
        
        // => stars2
        sort(all(stars2), greater<int>());
        
//        // => stars2 | L | hours
        rep(i, len(stars2)){
            if(L){
                //"booost"
                hours += stars2[i];
                L--;
            }else{
                hours += stars2[i]*2;
            }
        }

//        // => hours
        
        printf("Case #%d: %d\n", t+1, hours);
    }
    return 0;
}
