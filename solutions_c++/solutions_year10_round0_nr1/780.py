#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <iostream>
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> T min(T& a, T& b) { if (b < a) return b; return a; }
template<typename T> T max(T& a, T& b) { if (b > a) return b; return a; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }

int main() 
{
    int t,n;
    uint64 k;
    cin>>t;
    FOR(i,1,t){
        cin>>n>>k;
        uint64 p=1; FOR(j,1,n) p*=2;
        if (k%p==p-1) cout<<"Case #"<<i<<": ON"<<endl;
        else cout<<"Case #"<<i<<": OFF"<<endl;
    }    

	exit(0);
}
