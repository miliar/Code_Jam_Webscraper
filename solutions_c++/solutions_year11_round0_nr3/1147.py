#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

#include <set>
#include <map>

using namespace std;

#define REP(I, N) for (int I=0;I<int(N);I++)
#define FOR(I, A, B) for (int I=int(A);I<int(B);I++)
#define DWN(I, B, A) for (int I=int(B-1);I>=int(A);I--)

//#define REP(I, N) for (int I=1;I<=int(N);I++)
//#define FOR(I, A, B) for (int I=int(A);I<=int(B);I++)
//#define DWN(I, B, A) for (int I=int(B);I>=int(A);I--)

#define ALL(A) A.begin(), A.end()
#define CLR(A) memset(A, 0, sizeof(A))
#define CPY(A, B) memcpy(A, B, sizeof(A))
#define INS(A, P, B) A.insert(A.begin() + P, B)
#define ERS(A, P) A.erase(A.begin() + P) 
#define SRT(A) sort(ALL(A))
#define BSC(A, x) find(ALL(A), x) // != A.end()

#define SZ(A) int(A.size())
#define PB push_back
#define MP(A, B) make_pair(A, B)

#define IT iterator
#define VI vector<int>
#define VS vector<string>
#define SI set<int>
#define SS set<string>
#define MI map<int, int>
#define MS map<string, int>

typedef long long LL;
typedef double DB;


const int dx[] = {-1, 0, 1, 0}, dy[] = {0, 1, 0, -1};   // 4 ..
//const int dx[] = {-1, -1, 0, 0, 1, 1}, dy[] = {-1, 0, -1, 1, 0, 1}; // 6 ..
//const int dx[] = {-1, -1, -1, 0, 0, 1, 1, 1}, dy[] = {-1, 0, 1, -1, 1, -1, 0, 1}; // 8 ..
//const int dx[] = {-2, -2, -1, -1, 1, 1, 2, 2}, dy[] = {-1, 1, -2, 2, -2, 2, -1, 1}; // Knight ..

//const double PI = acos(-1.0);
//const double EPS = 1e-9;
//const double INF = 1e20;

//const LL INF = 1ll<<60;

const int MOD = 1000000007;
const int INF = 0x7fffffff;

template<class T> inline void checkMin(T &a, T b){if (b<a) a=b;};
template<class T> inline void checkMax(T &a, T b){if (b>a) a=b;};
template<class T> inline T sqr(T a){return a*a;};

template<class T> inline T gcd(T a, T b){return b==0?a:gcd(b,a%b);};
template<class T> inline T lcm(T a, T b){return a*b/gcd(a, b);};


const int N = 1000;
int a[N], s, n;

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    
    int T; cin >> T; 
    REP(t, T){
        cin >> n; s = 0;
        
        REP(i, n) {cin >> a[i]; s ^= a[i];}
        
        
        printf("Case #%d: ", t+1);
        if (s!=0) {
            cout << "NO" << endl;
            continue;
        }
        
        sort(a, a+n), s = 0;
        FOR(i, 1, n) s += a[i];
        cout << s << endl;
    }
    
}













