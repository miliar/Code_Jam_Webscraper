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

char CMB[30][30];
char &comb(int a, int b) {
    return CMB[a-'A'][b-'A'];
}

bool SPL[30][30];
bool &spoil(int a, int b) {
    return SPL[a-'A'][b-'A'];
}

void solve(int caseNo) {
    SET(CMB, 0);
    SET(SPL, 0);

    fi(i,ri()) {
        char e1, e2, t; scanf(" %c%c%c", &e1, &e2, &t);
        comb(e1, e2) = comb(e2, e1) = t;
    }

    fi(i,ri()) {
        char e1, e2; scanf(" %c%c", &e1, &e2);
        spoil(e1, e2) = spoil(e2, e1) = true;
    }

    int n = ri();
    char x[200]; scanf(" %s", x);

    char line[200]; int k = 0;

    fi(i, n) {
        char cmb;

        line[k] = x[i]; 
        while(k > 0 && (cmb = comb(line[k-1],line[k])) != 0) {
            k--;
            line[k] = cmb;
        }

        k++;

        fi(i, k)
            fi(j, k)
                if(spoil(line[i], line[j])) {
                    k = 0;
                    goto brk;
                }
brk:;
    }

    printf("Case #%d: [", caseNo);
    fi(i, k) {
        putchar(line[i]);
        if(i < k - 1)
            printf(", ");
    }
    printf("]\n");
}

int main(){
    fi(t,ri()) solve(t+1);
    return 0;
}

