#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
#include <deque>
#pragma warning(disable: 4996)
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

int i,j,k,x,y,z,t,T,base;
char buf[1024];




set<int> history;
typedef map<char,int> MAP;
MAP mm;

int next(int x)
{
    if (x==1) return 0;
    if (x==0) return 2;
    return x+1;
}
int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    scanf("%d", &T);    
    gets(buf);
    
    
    int n;
    for(t=1;t<=T;++t)
    {
        int b=1;
        int64 result = 0;
        gets(buf);
        mm.clear();
        n=strlen(buf);
        for(i=0;i<n;++i)
        {
            if (mm.find(buf[i]) == mm.end())
            {
                mm[buf[i]] = b;
                b=next(b);
            }           
        }
        int base = mm.size();
        if (base==1) ++base;
        for(int i=0;i<n;++i)
        {
            result = result * base + mm[buf[i]];
        }
        printf("Case #%d: %I64d\n", t, result);
        fflush(stdout);
    }
}


