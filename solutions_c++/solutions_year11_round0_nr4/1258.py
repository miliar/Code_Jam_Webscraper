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

double S[1002];
double L[1002];

void solve(int caseNo) {
    int n = ri();
    int p[n];
    fi(i, n) p[i] = ri() - 1;
    bool used[n]; 
    SET(used, 0);
    double expect = 0;
    fi(i, n) {
        if(!used[i]) {
            int j = p[i];
            int cnt = 0;
            while(!used[j]) {
                cnt++;
                used[j] = true;
                j = p[j];
            }
            //cout<<"cycle len="<<cnt<<endl;
            expect += L[cnt];
        }
    }
    printf("Case #%d: %0.6lf\n", caseNo, expect);
}

int main(){
    ft(n,2,10) {
        ft(k,1,n-1)
            S[n] += (S[k] + S[n-k] + 1) / (n-1);
        //cout<<n<<" "<<S[n]<<endl;
        L[n] = S[n] + 1;
    }

    fi(t,ri()) solve(t+1);
    return 0;
}

