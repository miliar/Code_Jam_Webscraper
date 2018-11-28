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
#define fi(i,n) for(int i = 0, i##end = (n); i < i##end; i++)
#define ft(i,a,b) for(int i = (a), i##end = (b); i <= i##end; i++)
#define fd(i,a,b) for(int i = (a), i##end = (b); i >= i##end; i--)
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

int C[101][256];
void solve(int t) {
    int D=ri(), I=ri(), M=ri(), N=ri();
    ft(p, 1, N) {
        int vl = ri();
        fi(v, 256) {
            //usun
            C[p][v] = D + C[p-1][v];
            //zmien
            ft(i, max(0, v - M), min(v + M, 255))
                C[p][v] = min(C[p][v], abs(vl - v) + C[p-1][i]);
        }

        bool change = true;
        while(change) {
            change = false;
            fi(v, 256) {
                //dodaj
                ft(i, max(0, v - M), min(v + M, 255)) {
                    int nc = I + C[p][i];
                    if(nc < C[p][v]) {
                        change = true;
                        C[p][v] = nc;
                    }
                }
            }
        }
    }
    int mc = C[N][0];
    fi(i, 256)
        mc = min(mc, C[N][i]);
    printf("Case #%d: %d\n", t, mc);
}

int main(){
    fi(t,ri()) solve(t+1);
    return 0;
}

