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

int d[1005];
int C;
int N;
int citPassed;
int ditor = 0;

int nextDist() {
    if(citPassed == N)
        return -1;
    citPassed++;
    int r = d[ditor];
    ditor = (ditor + 1) % C;
    return r;
}

void solve(int caseNo) {
    int L = ri(); 
    
    double T; scanf("%lf", &T);

    N = ri();
    C = ri();
    citPassed = ditor = 0;
    fi(i, C)
        d[i] = ri();

    double t = 0;

    vector<double> distLeft;
    distLeft.reserve(C);

    while(true) {
        double dst = nextDist();
        ///cout<<"got d"<<dst<<endl;
        if(dst == -1)
            break;
        double timeToPass = dst * 2;
        if(timeToPass + t > T) {
            double distPassedTillT = (T - t) * 0.5;
            distLeft.PB(dst - distPassedTillT);
            t = T;
        }
        else {
            t += timeToPass;
        }
    }
    //cout<<"t="<<t<<endl;;

    //fe(e, distLeft)
    //    cout << *e << ' ';
    //cout<<endl;

    sort(ALL(distLeft), greater<double>());
    fi(i, min(distLeft.size(), (size_t)L))
        distLeft[i] /= 2;

    double sum = 0;
    fe(e, distLeft)
        sum += *e;

    t += sum * 2;
    long long tt = (t + 0.25);
    printf("Case #%d: %lld\n", caseNo, tt);
}

int main(){
    fi(t,ri()) solve(t+1);
    return 0;
}

