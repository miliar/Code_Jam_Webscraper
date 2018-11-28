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
const int maxn = 223;
const int lowb = 103;
const int upb = 203;
int n, cq;
char a[23][23];
int q[123];

const int DIR[4][2] = {
    {1,0},
    {-1,0},
    {0,1},
    {0,-1}
};
void read()
{
    scanf("%d%d\n", &n, &cq);
    REP(i,n) gets(a[i]);
    REP(i,cq) scanf("%d", &q[i]);
}

string dp[23][23][lowb + upb + 9];

void pmin(string& a, string b)
{
    if(b=="")return;
    if(a=="" || (SI(b)<SI(a)) || (SI(b)==SI(a) && b<a))
        a = b;
}

string res[123];
void solve()
{
    REP(r,n)REP(c,n)
    {
        FOR(s,-lowb,upb)dp[r][c][s+lowb] = "";
        if(isdigit(a[r][c])) dp[r][c][a[r][c] - '0'+lowb] = a[r][c];
    }
    int r1, c1, r2, c2, s1;
    REP(t, maxn)
        REP(r,n)REP(c,n)if(isdigit(a[r][c]))
        FOR(s,-lowb,upb)if(dp[r][c][s+lowb] != "")
        {
            REP(d,4)
            {
                r1=r+DIR[d][0];
                if(r1<0||r1>=n)continue;
                c1=c+DIR[d][1];
                if(c1<0||c1>=n)continue;
                REP(d1,4)
                {
                    r2=r1+DIR[d1][0];
                    if(r2<0||r2>=n)continue;
                    c2=c1+DIR[d1][1];
                    if(c2<0||c2>=n)continue;
                    s1 = s + (a[r1][c1] == '+' ? 1 : -1) * (a[r2][c2] - '0');
                    if(s1<-lowb||s1>upb)continue;
                    string tt = dp[r][c][s + lowb] + a[r1][c1] + a[r2][c2];
                    pmin(dp[r2][c2][s1 + lowb],tt);
                }
            }
        }
    REP(i,cq)
    {
        res[i] = "";
        REP(r,n) REP(c,n)
            pmin(res[i], dp[r][c][q[i]+lowb]);
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
        printf("Case #%d:\n", t);
        REP(i,cq)
            printf("%s\n", res[i].c_str());
    }
    return 0;
}


