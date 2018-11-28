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




struct Fract {
	i64 top, low;
	Fract():top(0),low(1){}
	Fract(const i64& T, const i64& L=1):top(T),low(L){reduce();}
	bool operator <(const Fract& v) const {return top*v.low < v.top*low;}
	bool operator<=(const Fract& v) const {return top*v.low <= v.top*low;}
	bool operator==(const Fract& v) const {return top==v.top && low==v.low;}
	bool operator!=(const Fract& v) const {return top!=v.top || low!=v.low;}
	bool operator >(const Fract& v) const {return top*v.low > v.top*low;}
	bool operator>=(const Fract& v) const {return top*v.low >= v.top*low;}
	Fract operator+(const Fract& v) {return Fract(top*v.low+v.top*low, low*v.low);}
	Fract operator-(const Fract& v) {return Fract(top*v.low-v.top*low, low*v.low);}
	Fract operator*(const Fract& v) {return Fract(top*v.top, low*v.low);}
	Fract operator/(const Fract& v) {return Fract(top*v.low, low*v.top);}
	Fract& operator-() {top=-top; return *this;}
	Fract& operator+=(const Fract& v) {
		top = top*v.low + v.top*low;  low*=v.low; reduce();
		return *this;
	}
	Fract& operator-=(const Fract& v) {
		top = top*v.low - v.top*low;  low*=v.low; reduce();
		return *this;
	}
	Fract& operator*=(const Fract& v) {
		top *= v.top;  low*=v.low; reduce();
		return *this;
	}
	Fract& operator/=(const Fract& v) {
		top *= v.low;  low*=v.top; reduce();
		return *this;
	}
	void reduce() {
		if(low < 0) {top=-top; low=-low;}
		i64 a=iabs(top), b=iabs(low);
		if(a == 0) {low=1; return;}
		while(b) {a%=b;a^=b;b^=a;a^=b;}
		top/=a;  low/=a;
	}
};

const int NN = 512;

int  R, C, D;
char mask[NN][NN];
i64  Xv[NN][NN], Yv[NN][NN], Sv[NN][NN];
i64  sumTopX[NN][NN], sumTopY[NN][NN];
i64  sumLow[NN][NN];

i64  get(i64 s[NN][NN], int Rs, int Cs, int K) {
    return  s[Rs+K][Cs+K] - s[Rs][Cs+K] - s[Rs+K][Cs] + s[Rs][Cs];
}

bool calc(int Rs, int Cs, int K) {
    i64  Low = get(sumLow, Rs, Cs, K);
    i64  TopX = get(sumTopX, Rs, Cs, K);
    i64  TopY = get(sumTopY, Rs, Cs, K);
    
    Low -= Sv[Rs][Cs];
    Low -= Sv[Rs][Cs+K-1];
    Low -= Sv[Rs+K-1][Cs];
    Low -= Sv[Rs+K-1][Cs+K-1];
    
    TopX -= Xv[Rs][Cs];
    TopX -= Xv[Rs][Cs+K-1];
    TopX -= Xv[Rs+K-1][Cs];
    TopX -= Xv[Rs+K-1][Cs+K-1];
    
    TopY -= Yv[Rs][Cs];
    TopY -= Yv[Rs][Cs+K-1];
    TopY -= Yv[Rs+K-1][Cs];
    TopY -= Yv[Rs+K-1][Cs+K-1];
    
    
    if((2LL*Rs+K)*Low == TopX && (2LL*Cs+K)*Low == TopY)
        return true;
    return false;
}

void init() {
    memset(sumLow, 0, sizeof(sumLow));
    memset(sumTopX, 0, sizeof(sumTopX));
    memset(sumTopY, 0, sizeof(sumTopY));
    REP(i, R) REP(j, C) {
        i64  v = D + mask[i][j] - '0';
        Sv[i][j] = v;
        
        Xv[i][j] = v * (2LL*i + 1LL);
        Yv[i][j] = v * (2LL*j + 1LL);
        
        sumLow[i+1][j+1] = sumLow[i][j+1]
         + sumLow[i+1][j] - sumLow[i][j] + v;
         
        sumTopX[i+1][j+1] = sumTopX[i][j+1]
         + sumTopX[i+1][j] - sumTopX[i][j] + v*(2LL*i + 1LL);
         
        sumTopY[i+1][j+1] = sumTopY[i][j+1]
         + sumTopY[i+1][j] - sumTopY[i][j] + v*(2LL*j + 1LL);
    }
}

int main(int argc, char* argv[]) {
    int  testcase;
    freopen("B-large.in" , "r", stdin);
    freopen("output.out" , "w", stdout);
    scanf("%d", &testcase);
    FOR(it, 1, testcase) {
        scanf("%d%d%d", &R, &C, &D);
        REP(i, R) scanf("%s", mask[i]);
        init();
        int  ans = min(R, C);
        for(; ans>=3; --ans) {
            for(int i=0; i+ans<=R; ++i)
                for(int j=0; j+ans<=C; ++j)
                    if(calc(i, j, ans)) goto End;
        } End:
        printf("Case #%d: ", it);
        if(ans < 3) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
        //printf("Case #%d: %d\n", it, ans);
    }
    return 0;
}

