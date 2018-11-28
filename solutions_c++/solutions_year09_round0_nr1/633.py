#include <stdlib.h>
#include <stdio.h>
#include <math.h>
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
#define FOR(i,a,b) for ( i = (a); i <= (b); ++i )
#define IFOR(i,a,b) for ( i = (a); i >= (b); --i )
#define REP(i,N) for ( i = 0; i < N; ++i )
#define IREP(i,N) for ( i = N - 1; i >= 0; --i )
#define IT(T,A,i) for ( T::iterator i = (A).begin(); i != (A).end(); ++i )
#define BIT(mask,i) ((mask) & (1 << (i)))
/*---------------------------------------------------------*/
int lowbit(int set) { return (set^(set-1))&set; }
int countbit(int set) { return (set==0)?0:(1+countbit(set-lowbit(set))); }
/*---------------------------------------------------------*/
template<class T> void print(vector<T> A,int n=-1){if(n==-1||n>A.size())n=A.size();cout<<"{";for (int i=0;i<n;i++)cout<<A[i]<<" ";cout<<"}"<<endl;}
template<class T> void print(T A[],int n){cout<<"{";for (int i=0;i<n;i++)cout<<A[i]<<" ";cout<<"}"<<endl;}
/*---------------------------------------------------------*/
typedef vector<int> VI;
typedef vector<string> VS;
typedef double LD;
typedef long long LL;
/*---------------------------------------------------------*/
const int maxn = 12345;
char Dict[maxn][23];
int n, D, L;
char s[maxn];

void read()
{
    scanf("%s", &s);
}
typedef vector<vector<bool> > TMat;

int match(const char* s, TMat a)
{
    int i;
    REP(i, L)
        if (!a[i][s[i] - 'a'])
            return 0;
    return 1;
}

void solve()
{
    n = 0;
    TMat a(L, vector<bool>(26));
    int i = -1, ins = 0;
    for(const char* p = s; *p; ++p)
    {
        if (*p == '(')
        {
            ins = 1;
            ++i;
        }
        else
            if (*p == ')')
            {
                ins = 0;
            }
            else
            {
                if (!ins) ++i;
                a[i][*p - 'a'] = 1;
            }
    }
    REP(i, D)
        n += match(Dict[i], a);
}

int main()
{
    int ct, i;
    scanf("%d%d%d\n", &L, &D, &ct);
    REP(i, D)
        scanf("%s\n", Dict[i]);
    for (int t = 1; t <= ct; ++t)
    {
        read();
        solve();
        printf("Case #%d: ", t);
        printf("%d\n", n);
    }
    return 0;
}

