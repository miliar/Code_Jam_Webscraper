/*
  Name:
  Author:
  Date: 06-04-12 21:47
  Description:
  Time Limit:
*/

#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define FOR(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define FORD(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define REP(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define REPD(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

#define BIT(n) (1<<(n))
#define AND(a,b) ((a) & (b))
#define OR(a,b) ((a) | (b))
#define XOR(a,b) ((a) ^ (b))
#define sqr(x) ((x) * (x))

#define PI 3.1415926535897932385
#define INF 1000111222
#define EPS 1e-7
#define MAXN 100000

#define INP "C-small-attempt0.in"
#define OUT "C-small-attempt0.out"

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

int a, b, c, d, e, f, g, h, T;
bool Free[10000];

//bool hoanvi(int i, int j){
//    vi a, b;
//    while(i){
//        a.pb(i%10);
//        i/=10;
//        }
//    while(j){
//        b.pb(j%10);
//        j/=10;
//        }     
//    sort(all(a));
//    do{
//        if(a == b) return true;
//        //for(int i = 0; i < a.size(); i++) cout << a[i] << endl;
//        }while(next_permutation(all(a)));
//    return false;   
//    }
    
//bool hoanvi2(int i){
//    //bool res = false;
//    int res = 0;
//    vi v;
//    int tmp = i;
//    while(tmp){
//        v.pb(tmp%10);
//        tmp/=10;
//        }
//    sort(all(v));
//    do{
//        int tmp2 = 0;
//        FORD(j, v.size() - 1, 0){
//            tmp2 = tmp2 * 10 + v[j];
//            }
//        if(tmp2 > i && tmp2 <= b && tmp2 >= a){
//            //res = true;
//            res++;
//            Free[tmp2] = false;
//            }
//        }while(next_permutation(all(v)));   
//   return res; 
//}

int getCount(int c){
    memset(Free, true, sizeof Free);
    Free[c] = false;
    if(c < 10) return 0;
    int res = 0;
    vi v;
    int tmp = c;
    while(tmp){
        v.pb(tmp % 10);
        tmp /= 10;
        }
    FOR(j, 0, v.size() - 2){
        int tmp2 = 0;
        FORD(k, j, 0) tmp2 = tmp2 * 10 + v[k];
        FORD(k, v.size() - 1, j + 1) tmp2 = tmp2  * 10 + v[k];
        if(Free[tmp2] && tmp2 > c && tmp2 >= a && tmp2 <= b) {res++; Free[tmp2] = false;}
        }
    return res;
    }

void solve(){
    int res = 0;
    //memset(Free, true, sizeof Free);
    //FOR(i, a, b - 1) FOR(j, i + 1, b){
        //if(hoanvi(i, j)) res++;    
    //}
    //FOR(i, a, b){
        //if(Free[i]) {Free[i] = false; 
        //if(hoanvi2(i)) res++;
        //res+=hoanvi2(i);
        //}    
    //} 
    
    //take 3
    FOR(i, a, b){
        res+= getCount(i);
        }   
    printf("%d\n", res);
}

int main () {
    freopen(INP, "r", stdin); freopen(OUT, "w", stdout);
    scanf("%d", &T);
    FOR(i, 1, T){
        scanf("%d%d", &a, &b);   
        printf("Case #%d: ", i); 
        solve();
    }

    return 0;
    }
