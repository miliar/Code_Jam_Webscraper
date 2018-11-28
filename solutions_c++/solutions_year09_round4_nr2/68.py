#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
using namespace std;
/*---------------------------------------------------------*/
#define INF 123456789
#define SI(a) ((int)(a).size())
#define ALL(a) a.begin(),a.end()
#define CL(a,v) memset(a, v, sizeof(a))
#define FOR(i,a,b) for ( int i = (a); i <= (b); ++i )
#define REP(i,n) for ( int i = 0; i < (n); ++i )
#define IT(T,a,i) for ( T::iterator i = (a).begin(); i != (a).end(); ++i )
#define BIT(mask,i) (!!((mask) & (1LL << (LL)(i))))
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
typedef pair<int, LL> TP;

const LD PI = 2.0 * acos(0.0);
const LD EPS = 1e-10;
/*---------------------------------------------------------*/
VS split(const char* s, const char* del = " ")
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

template<typename T, typename S> T cast(S s)
{
    stringstream ss;
    ss << s;
    T res;
    ss >> res;
    return res;
}
/*---------------------------------------------------------*/
template<typename T> T sqr(T a) { return a * a; }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }
/*---------------------------------------------------------*/
const int maxn = 123;
char buf[123456];
int n, cr, cc;
int res;
char a[maxn][maxn];
LL amask[maxn];
map<TP,int> dp;
set<TP> inq;

#define MP(a,b) make_pair(a,b)

void read()
{
    scanf("%d%d%d\n", &cr, &cc, &n);
    REP(r,cr) scanf("%s\n", a[r]);
}

void add(queue<TP>& q, int r1, int c1, LL m, int d)
{
    if (r1==-1) return;
    TP p = MP(r1 * cc + c1, m);
    map<TP,int>::iterator it = dp.find(p);
    if(it == dp.end() || it->second > d)
    {
        dp[p] = d;
        if (inq.find(p) == inq.end())
        {
            inq.insert(p);
            q.push(p);
        }
    }
}

void fall(int r, int c, int& r1, int& c1)
{
    r1=r + 1; c1=c;
    while(r1<cr && a[r1][c1] == '.') ++r1;
    --r1;
    if(r1-r>=n) r1=-1;
}

LL tomask(const char* s)
{
    LL m = 0;
    REP(i,cc)
        if (s[i] == '#')
            m |= 1LL << (LL)i;
    return m;
}

void solve()
{
    res = INF;
    REP(i,cr) amask[i] = tomask(a[i]);
    dp.clear();
    inq.clear();

//    cerr << cr << " " << cc << " " << n << "\n";  print(a,cr);

    TP p = MP(0,amask[0]);
    queue<TP> q;
    inq.insert(p);
    dp[p] = 0;
    q.push(p);
    while(!q.empty())
    {
        p = q.front();
        q.pop();
        inq.erase(p);
        int r = p.first / cc;
        int c = p.first % cc;
        LL mask = p.second;
        int d = dp[p], r1, c1;

//        cerr << r << " " << c << " " << mask << " " << d << "\n";
        if(r==cr-1)
        {
            res = min(res, d);
            continue;
        }

        if(a[r+1][c] == '.')
        {
            fall(r + 1,c,r1,c1);
            add(q,r1,c1,amask[r1], d);
            continue;
        }

        if(c>0 && !BIT(mask,c-1))
        {
            add(q,r,c-1,mask,d);
            LL m1 = amask[r + 1];
            for(int k = 1;c-k>=0 && !BIT(mask,c-k) && BIT(amask[r+1],c-k);++k)
            {
                m1 ^= 1LL << (LL)(c-k);
                fall(r+1,c-1,r1,c1);
                add(q,r1,c1,r1>r+1?amask[r1]:m1,d + k);
            }
        }
        if(c<cc-1 && !BIT(mask,c+1))
        {
            add(q, r, c + 1, mask,d);
            LL m1 = amask[r + 1];
            for(int k = 1;c+k<cc && !BIT(mask,c+k) && BIT(amask[r+1],c+k);++k)
            {
                m1 ^= 1LL << (LL)(c+k);
                fall(r+1,c+1,r1,c1);
                add(q,r1,c1,r1>r+1?amask[r1]:m1,d + k);
            }
        }
    }
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
        if(res < INF)
            printf("Yes %d\n", res);
        else
            printf("No\n");

    }
    return 0;
}


