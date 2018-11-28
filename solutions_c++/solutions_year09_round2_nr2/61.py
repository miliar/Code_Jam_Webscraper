#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
/*---------------------------------------------------------*/
#define INF 123456789
#define SI(A) ((int)(A).size())
#define ALL(A) A.begin(),A.end()
#define CL(A,v) memset(A, v, sizeof(A))
#define FOR(i,a,b) for ( int i = (a); i <= (b); ++i )
#define REP(i,N) for ( int i = 0; i < N; ++i )
#define IT(T,A,i) for ( T::iterator i = (A).begin(); i != (A).end(); ++i )
#define BIT(mask,i) (!!((mask) & (1 << (i))))
/*---------------------------------------------------------*/
int lowbit(int set) { return (set^(set-1))&set; }
int countbit(int set) { return (set==0)?0:(1+countbit(set-lowbit(set))); }
/*---------------------------------------------------------*/
template<class T> void print(vector<T> A,int n=-1){if(n==-1||n>SI(A))n=SI(A);cerr<<"VEC "<<n<<" {";REP(i,n)cerr<<A[i]<<" ";cerr<<"}"<<endl;}
template<class T> void print(T A[],int n){cerr<<"ARR "<<n<<"{";REP(i,n)cerr<<A[i]<<" ";cerr<<"}"<<endl;}
/*---------------------------------------------------------*/
typedef vector<int> VI;
typedef vector<string> VS;
typedef double LD;
typedef long long LL;

VS split(const char* s, const char* del)
{
    VS res;
    const char* beg = 0, *p;
    for(p = s; *p; ++p)
        if (strchr(del, *p))
        {
            if (beg) res.push_back(string(beg, p - beg));
            beg = 0;
        }
        else
            if (!beg) beg = p;
    if (beg) res.push_back(string(beg, p - beg));
    return res;
}
/*---------------------------------------------------------*/
const int maxn = 12345678;
int n;
char s[123];
string res;

void read()
{
    scanf("%s\n", &s);
    n = strlen(s);
    res = s;
    if (next_permutation(ALL(res)))
        return;
    res = "0" + string(s);
    next_permutation(ALL(res));

}

void solve()
{
}

int main()
{
    int ct;
    scanf("%d\n", &ct);
    for (int t = 1; t <= ct; ++t)
    {
        read();
        solve();
        printf("Case #%d: ", t);
        printf("%s\n", res.c_str());
    }
    return 0;
}


