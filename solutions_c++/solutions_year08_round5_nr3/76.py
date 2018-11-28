
#pragma warning (disable:4786)
#include <string.h>
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
const int MAX = 12;
const int MAX2 = 5000;

int m;
int n;
char s[MAX][MAX];
int val[MAX2];
int P[MAX2];
int P1[MAX2];

int check1(int mask, char s[MAX])
{
    int i;
    REP(i, n)    
    {
        if (s[i] == 'x' && BIT(mask, i))
            return 0;
        if( (i<n-1) && BIT(mask, i) && BIT(mask, i+1))
            return 0;
    }
    return 1;
}

int check(int mask1, int mask2)
{
    int i;
    REP(i, n-1)
        if (BIT(mask1, i) && BIT(mask2, i+1) || 
            BIT(mask1, i+1) && BIT(mask2, i))
            return 0;

    return 1;
}

int solve()
{
    int i, j, k;
    CL(P, 0);
    CL(P1, 0);    
    REP(i,1<<n) P[i] = check1(i, s[0]) ? val[i] : 0;
    FOR(k,1,m-1)
    {        
        REP(i,1<<n)
        {
            if(check1(i, s[k]))
            {
                int max = 0;
                int m0;
                REP(j,1<<n)
                {
                    m0  = val[i] + P[j];
                    if (max < m0 && check(i, j))
                        max = m0;
                }
                P1[i] = max;
            }
            else
                P1[i] = 0;
        }        
        REP(i,1<<n)
        {
            P[i] = P1[i];
            P1[i] = 0;
        }
    }
    return *max_element(P, P + (1<<n));
}

void build()
{
    int i, j;
    REP(i,(1<<(MAX-1)))
    {
        int num = i;
        REP(j, 20)        
        {
            val[i] += num % 2;
            num /= 2;
        }
    }
}

int main()
{
    int cT, t, i;

    build();
    freopen("c:/temp/gcj/r3/c/1.out", "w", stdout);    
    freopen("c:/temp/gcj/r3/c/1.in", "r", stdin);
    scanf("%d", &cT);
    REP(t, cT)
    {        
        CL(s, 0);
        scanf("%d%d", &m, &n);
        REP(i,m) scanf("%s", s[i]);
        int res = solve();
        printf("Case #%d: %d\n", t + 1, res);
    }
    fclose(stdout);
    return 0;
}
