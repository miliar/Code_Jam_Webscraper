#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <list>
#include <stack>
#include <numeric>
#include <bitset>
#include <list>
using namespace std;
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define ST first
#define ND second
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(i,x) for(__typeof((x).begin()) i=(x).begin();i != (x).end();++i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define VAR(v,n) __typeof(n) v = n
#define sgn(x) (x > 0) ? 1 : ((x < 0) ? -1 : 0)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define SZ(x) int((x).size()) 
#define SIZE(x) (int)x.size()
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,w) memset((x),w,sizeof (x))
// string -> char* : string a; a.c_str();
// char* -> string : char a[N]; string(a);
// int -> char* : int a; char b[N]; sprintf(b, "%d", a);
// char* -> int : int a; char b[N]; sscanf(b, "%d", &a);
// char* -> int podstawa base : char a[N]; strtol(a, NULL, base)
// porowananie char* : strcmp(char*,char*) np return strcmp(&c[a],&c[b])<0;
// bitset: cout << bitset<20> (100000) << endl;
// iostream: cin, getline(cin, string); stdio: scanf, gets(char *), getchar()
// sort(ALL(v),less<int>()) rosnaca, sort(ALL(v),greater<int>()) malejaca
// struct T {string name; lli X,Y;};
// bool operator<(T a,T b){return a.X*a.X+b.Y*b.Y < a.X*a.X+b.Y*b.Y;}
typedef vector<int> vi, VI;
typedef pair<int, int> pii, PII;
typedef pair<pii, int> piii;
typedef vector<pii> vii;
typedef long long int lli, LL;
typedef vector<lli> vl;
typedef pair<lli, lli> pll;
typedef vector<pll> vll;
#define MAXN 105  

int t, n, s, p, ret;
int dan[120];

int main(){

    cin >> t;
    REP(k,t){
        cin >> n >> s >> p;
        ret = 0;
        REP(l,n) cin >> dan[l];
        sort(dan, dan + n);
        FORD(i, n-1, 0){
            if(dan[i]/3 + (dan[i]%3?1:0) >= p) ret++;
            else if(dan[i] == 0) (p==0?ret++:ret);
            else if (s > 0 && (dan[i]/3 + (dan[i]%3==2?2:1) >= p)) {ret++; s--;}
                   
        }

        cout << "Case #" << k+1 << ": " << ret << endl;
    }
    
    return 0;
}












