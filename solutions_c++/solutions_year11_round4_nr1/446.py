#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <math.h>
#include <time.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <bitset>
#include <vector>
#include <deque>
#include <utility>
#include <complex>
#include <list>
#include <sstream>
#include <iostream>
#include <functional>
#include <numeric>
#include <algorithm>
#include <iomanip>
using namespace std;


template<class T>inline T iabs(const T& v) {return v<0 ? -v : v;}
template<class T>inline T strTo(string s){istringstream is(s);T v;is>>v;return v;}
template<class T>inline string toStr(const T& v){ostringstream os;os<<v;return os.str();}
template<class T>inline int cMin(T& a, const T& b){return b<a?a=b,1:0;}
template<class T>inline int cMax(T& a, const T& b){return a<b?a=b,1:0;}
template<class T>inline int cBit(T n){return n?cBit(n&(n-1))+1:0;}


#define DEBUG(a)     printf("%s = %s\n", #a, toStr(a).c_str())

#define two(i)       (1<<(i))
#define two64(i)     (1LL<<(i))
#define contain(s,i) (((s)>>(i))&1)
#define testBit(s,i) (((s)>>(i))&1)
#define setBit(s, i) (s |= two(i))
#define unSetBit(s,i) (s &= ~two(i))
#define MP(a,b)      make_pair(a,b)
#define CLR(arr,v)   memset(arr, v, sizeof(arr))
#define FOR(i,s,e)   for(int i(s),__(e); i<=__; ++i)
#define FORD(i,s,e)  for(int i(s),__(e); i>=__; ++i)
#define REP(i,n)     for(int i(0),__(n); i< __; ++i)
#define REPD(i,n)    for(int i((n)-1);   i>= 0; --i)

typedef int                 i32;
typedef unsigned int        u32;
typedef long long           i64;
typedef unsigned long long  u64;
typedef pair<int,int>       PII;
typedef vector<int>         VI;
typedef vector<string>      VS;

const int NN = 1024;
int  X, S, R, t, N;
int  B[NN], E[NN], W[NN], idx[NN];

bool cmp2(const int& a, const int& b) {
    return W[a] < W[b];
}

double calc() {
    int  preX = 0;
    double srcT = 0;
    double  Len = 0;
    REP(ii, N) {
        int  i = idx[ii];
        srcT += (B[i] - preX) / double(S);
        Len += B[i] - preX;
        preX = E[i];
        srcT += (E[i] - B[i]) / double(S + 0.0 + W[i]);
    }
    Len += X - preX;
    srcT += (X - preX) / double(S);
    
   // printf("srcT = %f, Len=%f\n", srcT, Len);
    REP(i, N) idx[i] = i;
    sort(idx, idx+N, cmp2);
    double  delta = 0;
    double  curT = t;
    
  //  DEBUG(curT);
    
    double  ct = Len / double(R);
    ct = min(ct, curT);
    delta += ct * double(R-S) / double(S);
    curT -= ct;
    REP(ii, N) {
        int  i = idx[ii];
        //printf("(%d, %d, %d)\n", B[i], E[i], W[i]);
        //if(curT <= 0.0000000001) break;
        double  ct = double(E[i] - B[i]) / double(R + W[i]);
        ct = min(ct, curT);
        delta += ct * double(R-S) / double(S + W[i]);
        curT -= ct;
    }
   // printf("delta = %.9f\n", delta);
    return  srcT - delta;
}



bool cmp(const int& a, const int& b) {
    return B[a] < B[b];
}

int main(int argc, char* argv[]) {
    int  testcase;
    freopen("A-large.in" , "r", stdin);
    freopen("output.out" , "w", stdout);
    scanf("%d", &testcase);
    FOR(it, 1, testcase) {
        scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
        REP(i, N) {
            scanf("%d%d%d", B+i, E+i, W+i);
            idx[i] = i;
        }
        sort(idx, idx+N, cmp);
        printf("Case #%d: %.9f\n", it, calc());
    }
    return 0;
}

