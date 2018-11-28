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

int len[10001];
string dd[10001];
bool ee[10001][256];
bool bb[10001];

void run(int caseid) {
    cin >> N >> M;

    memset(dd, 0, sizeof(dd));
    memset(len, 0, sizeof(len));
    memset(ee, 0, sizeof(ee));

    For(i, 0, N) {
        For(j, 0, 255) {
            ee[i][j] = false;
        }
        string s;
        cin >> s;
        dd[i] = s;
        len[i] = (int)s.length();
        For(j, 0, len[i]) {
            ee[i][ s[j] ] = true;
        }
    }

    For(mm, 0, M) {
        string je;
        cin >> je;
        //

        int maxi = 0;
        string maxs = dd[0];

        // use word i
        For(i, 0, N) {
            int nowi = 0;

            int len1 = len[i];
            memset(bb, 0, sizeof(bb));
            bool ex[256];
            memset(ex, 0, sizeof(ex));

            //elim
            For(j, 0, N) {
                if (len[j] != len1)
                    bb[j] = true;
                else {
                    For(k, 0, len[j]) ex[ dd[j][k] ] = true;
                }
            }

            for (int id = 0; id < je.length(); id++) {
                char c = je[id];
                if (ex[c] == false)  continue;
                if (ee[i][c] == false) {
                    nowi++;
                    // all words not have this char, bb==false first
                    memset(ex, 0, sizeof(ex));
                    For(j, 0, N) { 
                        if (bb[j] == false) {
                            if (ee[j][c] == false) {
                                For(k, 0, len[j]) ex[ dd[j][k] ] = true;
                            }
                            else {
                                bb[j] = true;
                            }
                        }
                    }
                }
                else { 
                    // all words not have this char, bb==false first
                    memset(ex, 0, sizeof(ex));
                    For(j, 0, N) {
                        if (bb[j] == false) { 
                            if (ee[j][c] == true) {
                                bool f = false;
                                For(k, 0, len[j])  {
                                    if (dd[i][k] == c && dd[j][k] != c)
                                        f = true;
                                    if (dd[i][k] != c && dd[j][k] == c)
                                        f = true;
                                }
                                if (f == false)
                                    For(k, 0, len[j])
                                        ex[ dd[j][k] ] = true;
                                else
                                    bb[j] = true;
                            }
                            else {
                                bb[j] = true;
                            }
                        }
                    }
                } // end if
            }
            if (nowi > maxi) {
                maxi = nowi;
                maxs = dd[i];
            }
        }
        cout << " " << maxs;
    }
    cout << endl;
}

////////////////////////////////////////////////////////////////////////////////////////////////
int main() {
    ////// A-small-0.in
    string pre0 = "R:\\codejam\\source\\";
    string pre1 = "B-";
    string pre2 = "small-";
    string pre3 = "4";
    string fileIn = pre0 + pre1 + pre2 + pre3 + ".in";
    string fileOut = pre0 + pre1 + pre2 + pre3 + ".out";
    freopen(fileIn.c_str(), "r", stdin); freopen(fileOut.c_str(), "w", stdout);

	int CaseNum; cin >> CaseNum;
    For(i, 1, CaseNum + 1) {
        cout << "Case #" << i << ":";
        run(i);
        fflush(stdout);
    }
    return 0;
}

