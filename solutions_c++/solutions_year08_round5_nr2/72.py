
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
typedef pair<int, int> TP;
typedef unsigned char ui8;
/*---------------------------------------------------------*/
const int DIR[4][2] = 
{
    {0, 1},
    {-1, 0},
    {0, -1},
    {1, 0}
};

int cR, cC, H;
char A[123][123];
TP S[123][123][4];
ui8 D[323456789];

int _hash(int r, int c, int r1, int c1, int d1, int r2, int c2, int d2)
{
    int res = r * cC + c;
    res = res * H + (r1 * cC + c1) * 4 + d1;
    res = res * H + (r2 * cC + c2) * 4 + d2;
    return res;
}

void _inv(int h, int& r, int& c, int& r1, int& c1, int& d1, int& r2, int& c2, int& d2)
{
    int t = h % H;
    d2 = t % 4;
    t /= 4;
    r2 = t / cC;
    c2 = t % cC;

    h /= H;
    t = h % H;
    d1 = t % 4;
    t /= 4;
    r1 = t / cC;
    c1 = t % cC;

    h /= H;
    r = h / cC;
    c = h % cC;
}

inline void Add(queue<int>& Q, int d, int h1)
{
    if ( D[h1] > d )
    {
//fprintf(stderr, "E: %d %d\n", d, h1);
        D[h1] = d;
        Q.push(h1);
    }
}

int solve()
{
    CL(D, -1);
    H = (cR + 1) * cC * 4;
    int r, c, r0, c0, r1, c1, r2, c2, d1, d2, dir, nr, nc;
    REP(r, cR) REP(c, cC)
    {
        if ( A[r][c] == 'O' ) 
        {
            r0 = r;
            c0 = c;
        }
        REP(dir, 4)
        {
            r1 = r;
            c1 = c;
            while ( 1 )
            {
                nr = r1 + DIR[dir][0];
                nc = c1 + DIR[dir][1];
                if ( nr < 0 || nr >= cR || nc < 0 || nc >= cC ) break;
                if ( A[nr][nc] == '#' ) break;
                r1 = nr;
                c1 = nc;
            }
            S[r][c][dir] = make_pair(r1, c1);
        }
    }
    queue<int> Q;
    int h = _hash(r0, c0, cR, 0, 0, cR, 0, 0), h1;
    int res = 12345678, d;
    Add(Q, 0, h);
    while ( !Q.empty() )
    {
        h = Q.front();
        Q.pop();
        d = D[h];
        if ( d >= res ) continue;        

        _inv(h, r0, c0, r1, c1, d1, r2, c2, d2);
        if ( A[r0][c0] == 'X' )
        {
            res = D[h];
            continue;
        }
//fprintf(stderr, "C: %d %d | %d %d %d | %d %d %d | %d %d\n", r0, c0, r1, c1, d1, r2, d2, c2, d, res);
        
        REP(dir, 4)
        {
            TP s = S[r0][c0][dir];
            h1 = _hash(r0, c0, s.first, s.second, dir, r2, c2, d2);
            Add(Q, d, h1);
            h1 = _hash(r0, c0, r1, c1, d1, s.first, s.second, dir);
            Add(Q, d, h1);
            if ( r0 == r1 && c0 == c1 && dir == d1 && r2 != cR )
            {
                h1 = _hash(r2, c2, r1, c1, d1, r2, c2, d2);
                Add(Q, d + 1, h1);
            }
            if ( r0 == r2 && c0 == c2 && dir == d2 && r1 != cR )
            {
                h1 = _hash(r1, c1, r1, c1, d1, r2, c2, d2);
                Add(Q, d + 1, h1);
            }
            nr = r0 + DIR[dir][0];
            nc = c0 + DIR[dir][1];

//fprintf(stderr, "D: %d %d %d\n", nr, nc, dir);
            if ( nr < 0 || nr >= cR || nc < 0 || nc >= cC ) continue;
            if ( A[nr][nc] == '#' ) continue;

            h1 = _hash(nr, nc, r1, c1, d1, r2, c2, d2);
            Add(Q, d + 1, h1);
        }
    }
    return res;
}

int main()
{
    int cT, t, r;

    //freopen("c:/temp/gcj/r3/b/1.err", "w", stderr);
    freopen("c:/temp/gcj/r3/b/1.out", "w", stdout);    
    freopen("c:/temp/gcj/r3/b/1.in", "r", stdin);
    scanf("%d", &cT);
    REP(t, cT)
    {
        scanf("%d%d\n", &cR, &cC);
        REP(r, cR) scanf("%s", &A[r]);
        int res = solve();
        if ( res < 0 || res > 12345 )
            printf("Case #%d: THE CAKE IS A LIE\n", t + 1);
        else
            printf("Case #%d: %d\n", t + 1, res);        
        fprintf(stderr, "%d\n", t);
    }
    fclose(stdout);
    return 0;
}
