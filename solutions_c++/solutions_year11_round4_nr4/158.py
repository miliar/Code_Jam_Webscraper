// Author: Wei Xueliang
// EMail: wei.xueliang@gmail.com

#include <iostream>
#include <string>
#include <cmath>
#include <list>
#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <cmath>
using namespace std; 

//////////////////////////////////////////////////////////////////////  Template
typedef long long i64;                                              // int64;
typedef unsigned long long ui64;                                    // uint64
typedef vector<int> VI;                                             // VI,   
typedef VI::iterator VI1;                                           // VI1
typedef vector< string > VS;                                        // VS
typedef VS::iterator VS1;                                           // VS1

template<class X> inline void setmin(X &a, X b){ if(b<a) a=b; }     // setmin(result, curvalue)
template<class X> inline void setmax(X &a, X b){ if(b>a) a=b; }     // setmax(result, curvalue) 

#define For(i,a,b)       for(int i = (a); i < (b); ++i)             // For(i, start, end)
#define Foreach(it,end)  for(;it != end; ++it)                      // Foreach(it, vec.end() )
// #define pow2(X)     ((i64)1 << (X))   // pow2(X) = 2^X 

bool upper(char c) { return (c >= 'A') && (c <= 'Z');}              // upper('X')
bool lower(char c) { return (c >= 'a') && (c <= 'z');}              // lower('x'
bool digit(char c) { return (c >= '0') && (c <= '9');}              // digit('9')
char toLower(char c) { return (upper(c)) ? (c + 32) : c;}           // toLower('X')
char toUpper(char c) { return (lower(c)) ? (c - 32) : c;}           // toUpper('x')

template<class T> string toStr(T data){                             //toStr(Anytype);
    ostringstream oss; oss << data; oss.flush(); 
    return oss.str(); }
template<class T> T str2(string s) {                                //str2<int>(s)
    T data = 0; istringstream inss(s); inss >> data; 
    return data; }

template<class T> void str2arr(string s, int &n, T arr[]) {           //str2arr(s, n, array)
    n = 0; T value; istringstream inss(s);
    for(; inss >> value; arr[n++] = value); } 

inline i64 gcd(i64 a,i64 b){
    if(a<0) return gcd(-a,b);
    if(b<0) return gcd(a,-b);
    return (b==0)?a:gcd(b,a%b);
}


////////////////////////////////////////////////////////////////////////////////////////////////

int TestCase;
int N, M, L, K, P, W;


int ww[401][2010];

int route[401];

int cur[401][2];
const int max1 = 1024000;
int  f[max1][2]; // 

//int qa[1024][3];    //[0]: length, [1]: threaten, [2]: unused
bool g[max1][401];       //[0]: first node, [1]: second node on path
int  q[max1];

void run(int caseid) {
    //scan
    scanf("%d %d", &P, &W);
    // cin >> P >> W;
    memset(ww, 0, sizeof(ww));
    memset(f, 0, sizeof(f));
    memset(g, 0, sizeof(g));
    memset(q, 0, sizeof(q));
    memset(cur, 0, sizeof(cur));
    for (int i = 0; i < W; i++) {
        int x, y;
        scanf("%d,%d", &x, &y);
        ww[x][0] += 1;
        ww[y][0] += 1;
        ww[x][ ww[x][0] ] = y;
        ww[y][ ww[y][0] ] = x;

        // Get started;
    }
    for (int i = 0; i < 401; i++) {
        f[i][0] = 10000;
        f[i][1] = 10000;
        cur[i][0] = 10000;
        cur[i][1] = 10000;
    }
    int q0 = 0;
    f[0][0] = 0;
    f[0][1] = 0;
    g[0][0] = true; // threaten
    for (int j = 1; j <= ww[0][0]; j++) {
        f[0][1] += 1;
        g[0][ ww[0][j] ] = true;
    }
    cur[0][0] = 0;
    cur[0][1] = f[0][1];

    int q1 = 1;

    q[0] = 0;
    int min1 = 1000;
    int max2 = -1;
    while (true) {
        int x = q[q0]; // next;

        if (f[q0][0] > min1) {
            break;
        }

        if (f[q0][0] > cur[x][0]) {
            continue;
        }

        if (g[q0][1] == true) {
            if (f[q0][0] < min1 || (
                f[q0][0] == min1 
                && f[q0][1] > max2)) 
            {
                min1 = f[q0][0];
                max2 = f[q0][1];
            }
        }
        for (int i = 1; i <= ww[x][0]; i++) {
            int y = ww[x][i];
            int cc = f[q0][1] - 1;

            for (int j = 1; j <= ww[y][0]; j++) {
                if ( g[q0][ ww[y][j] ] == false ) {
                    cc += 1;
                }
            }

            if (f[q0][0] + 1 <= cur[y][0]) {
                q[q1] = y;
                f[q1][0] = f[q0][0] + 1;
                f[q1][1] = cc;

                cur[y][0] = f[q1][0];
                cur[y][1] = f[q1][1];

                for(int j = 0; j <= P; j++) {
                    g[q1][j] = g[q0][j];
                }
                for (int j = 1; j <= ww[y][0]; j++) {
                    g[q1][ ww[y][j] ] = true;
                }
                q1 += 1;
            }
        }
        q0 += 1;
    }
    cout << min1 << " " << max2 << endl;
}

////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
    ////// A-small-0.in
    string pre0 = "R:\\codejam\\source\\";
    string pre1 = "D-";
    string pre2 = "small-";
    string pre3 = "attempt2";
    string fileIn = pre0 + pre1 + pre2 + pre3 + ".in";
    string fileOut = pre0 + pre1 + pre2 + pre3 + ".out";
    freopen(fileIn.c_str(), "r", stdin); freopen(fileOut.c_str(), "w", stdout);

	int CaseNum; 
    scanf("%d", &CaseNum);
    //cin >> CaseNum;

    For(i, 1, CaseNum + 1) {
        cout << "Case #" << i << ": ";
        run(i);
        fflush(stdout);
    }
    return 0;
}

