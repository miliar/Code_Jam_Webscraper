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
int N, M, L, K;

void run(int caseid) {
    i64 n, min1, pd, pg, z;
    cin >> n >> pd >> pg;

    z = gcd(pd, 100);
    min1 = 100 / z;

    if (min1 > n) {
        printf("Broken\n");
    } else if (min1 == 0) {
        printf("Possible\n");
    } else {
        if (pg == 100 && pd != 100) {
            printf("Broken\n");
        } else if (pg == 0 && pd != 0) {
            printf("Broken\n");
        } else {
            printf("Possible\n");
        }
    }
}

////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
    ////// A-small-0.in
    string pre0 = "R:\\codejam\\source\\";
    string pre1 = "A-";
    string pre2 = "large-";
    string pre3 = "0";
    string fileIn = pre0 + pre1 + pre2 + pre3 + ".in";
    string fileOut = pre0 + pre1 + pre2 + pre3 + ".out";
    freopen(fileIn.c_str(), "r", stdin); freopen(fileOut.c_str(), "w", stdout);

	int CaseNum; cin >> CaseNum;
    For(i, 1, CaseNum + 1) {
        printf("Case #%d: ",i);
        run(i);
        fflush(stdout);
    }
    return 0;
}

