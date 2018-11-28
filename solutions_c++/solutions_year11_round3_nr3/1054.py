#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <limits.h>

using namespace std;
typedef long long llong;

int getint() { int i; cin >> i; return i; }
llong getllong() { llong i; cin >> i; return i; }

string getline() { char line[1024];cin.getline(line,1024);return string(line); }

template<typename T> T MAX(const T&  a, const T & b) { return a>b?a:b; }
template<typename T> T MIN(T a, T b) { return a<b?a:b; }
template<typename T> T ABS(T a) { return a>0.0?a:-a; }

template<typename T> T GCD(T a, T b) {
    if (a==b)
        return a;
    if (a>b)
        return GCD(a-b,b);
    else
        return GCD(a,b-a);
}

template<typename T> T LCM(T a, T b) {
    T gcd = GCD(a,b);
    double x = log10(a) + log10(b) - log10(gcd);
    if (x > 20)
        return LLONG_MAX;
    return (a / gcd )* b;
}

/*
struct PosCompare {
    bool operator()(const Pos & a, const  Pos & b) {
        return a.P < b.P;
    }
};
*/


#define REP(V,COUNT) for(llong V = 0; V < COUNT; V++)
#define ZERO(X) memset(X, 0, sizeof(X) )
bool bigger[20000];

int main() {
    llong TESTCASES= getint();
    
    REP(testcase, TESTCASES) {

        llong N = getllong();
        llong L = getllong();
        llong H = getllong();
        vector<llong> freqs;
        ZERO(bigger);

        REP(i,N) {
            freqs.push_back( getllong() );
        }

        sort( freqs.begin(), freqs.end() );

        llong min = L;

        bool found = false;
        llong result = 0;

        for(llong x=L; x<=H;x++) {

            bool good = true;
            REP(i,N) {
                llong f = freqs[i];
                if (x > f) {
                    if ((x % f) !=0 ) {
                        good = false;
                        break;
                    }
                }
                if (x < f) {
                    if ((f % x) !=0 ) {
                        good = false;
                        break;
                    }
                }
            }
            if (good) {
                found = true;
                result = x;
                break;
            }
        }

        if (found)
            cout << "Case #" << testcase+1<<": " << result << endl;
        else
            cout << "Case #" << testcase+1<<": NO" << endl;
    }
}
