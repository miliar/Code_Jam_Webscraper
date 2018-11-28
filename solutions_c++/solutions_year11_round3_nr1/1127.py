#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

bool debug = false;

int getint() { int i; cin >> i; return i; }
string getline() { char line[1024];cin.getline(line,1024);return string(line); }

template<typename T> T MAX(const T&  a, const T & b) { return a>b?a:b; }
template<typename T> T MIN(T a, T b) { return a<b?a:b; }
template<typename T> T ABS(T a) { return a>0.0?a:-a; }

#define COUT if (debug) cout

/*
struct PosCompare {
    bool operator()(const Pos & a, const  Pos & b) {
        return a.P < b.P;
    }
};
*/


#define REP(V,COUNT) for(int V = 0; V < COUNT; V++)
#define ZERO(X) memset(X, 0, sizeof(X) )

char data[100][100];
bool set(int r,int c,char v) {
    if (data[r][c]!='#')
        return false;
    data[r][c]=v;
    return true;
}
int main() {
    int TESTCASES= getint();
    
    REP(testcase, TESTCASES) {
        string result = "CIAO";
        ZERO(data);

        int R = getint();
        int C = getint();getline();
        COUT << "R:" << R << "C:" << C << endl;
        REP(r,R) {
            string line = getline();
            REP(c,C) {
                data[r][c] = line[c];
            }
        }
        bool good = true;
        REP(r,R) {
            if (!good)
                break;
            REP(c,C) {
                if (data[r][c]=='#') {
                    good &= set(r+0,c+0,'/');
                    good &= set(r+0,c+1,'\\');
                    good &= set(r+1,c+0,'\\');
                    good &= set(r+1,c+1,'/');
                }
                if (!good)
                    break;
            }
        }


        cout << "Case #" << testcase+1<<":" << endl;
        if (good) {
            REP(r,R) {
                REP(c,C) {
                    cout << data[r][c];
                }
                cout << endl;
            }
        } else{
            cout << "Impossible" << endl;
        }
    }
}
