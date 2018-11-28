/* All includes and defines required by the templates
 * Just add it at the beginning and all will work OOB */
#include<iostream>
#include<set>
#include<iomanip>
#include<sstream>
#include<fstream>
#include<stack>
#include<cstdio>
#include<cmath>
#include<cassert>
#include<queue>
#include<vector>
#include<list>
#include<algorithm>
#include<map>
#include<cstring>
#include<cctype>


using namespace std;
#define fe(e,C) for(__typeof((C).begin()) e = (C).begin(); e != (C).end(); e++)
#define fi(i,n) for(int (i) = 0, __end = (n); (i) < __end; i++)
#define ft(i,a,b) for(int (i) = (a), __end = (b); (i) <= __end; (i)++)
#define fd(i,a,b) for(int (i) = (a), __end = (b); (i) >= __end; (i)--)
#define fs(i,C) fi(i,SZ(C))
#define ALL(V) (V).begin(), (V).end()
#define SET(T, c) memset(T, c, sizeof(T))
#define VI vector<int>
#define PB push_back
#define PII pair<int, int>
#define SEC second
#define FST first
#define MP make_pair
#define SZ(C) ((int)(C).size())
#define SQR(a) ((a)*(a))
#define VII vector<PII>
#define SS stringstream

typedef unsigned long long ULL;
typedef long long LL;

int ri() { int n; scanf(" %d", &n); return n; }
void pi(int n) { printf("%d\n", n); }
string rs() { char buf[10000]; buf[9999]=-1; scanf(" %s ", buf); assert(buf[9999]==-1); return buf; }
void ps(const string &s) { printf("%s\n", s.c_str()); }
template<class R, class T>
R conv(const T &t) { stringstream ss; ss << t; R r; ss >> r; return r; }
LL gcd(LL a, LL b) { if(b == 0) return a; else return gcd(b, a % b); }
struct pt { int x, y; pt(int x, int y):x(x), y(y) {} };

void solve(int caseNo) {
    int X = ri(), S = ri(), R = ri(), t = ri(), N = ri();
    vector<PII> V;
    int sumLen=0;
    fi(i, N) {
        int b = ri(), e=ri(), w=ri();
        V.PB(MP(w, e-b));
        sumLen += e-b;
    }
    V.PB(MP(0, X - sumLen));

    sort(ALL(V));
    double T = t;

    double ovrT = 0;

    fe(e, V) {
        double w = e->first;
        double l = e->second;

        double runTime = l / (w + R);
        if(runTime > T) {
            double distMade = (w + R) * T;
            double distToGo = l - distMade;
            double walkTime = distToGo / (w + S);

            ovrT += T;
            T = 0;

            ovrT += walkTime;
        }
        else {
            T -= runTime;
            ovrT += runTime;
        }
    }

    printf("Case #%d: %lf\n", caseNo, ovrT);
}

int main(){
    fi(t,ri()) solve(t+1);
    return 0;
}

