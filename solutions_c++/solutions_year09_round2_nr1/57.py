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
char s[maxn];
char buf[maxn];
vector<VS> f;
struct TNode
{
    string f;
    double w;
    int yes;
    int no;
};

TNode tree[1234567];
VS pt;
int cnode;

int go(int& beg)
{
    if (beg >= SI(pt)) return -1;
    if (pt[beg] == "(")
    {
        int i = cnode++;
        tree[i].f = "";
        tree[i].yes = tree[i].no = -1;
        sscanf(pt[beg + 1].c_str(), "%lf", &tree[i].w);
        if (pt[beg + 2] == ")")
        {
            beg += 3;
            return i;
        }
        tree[i].f = pt[beg + 2];
        beg += 3;
        tree[i].yes = go(beg);
        tree[i].no = go(beg);
        ++beg;
        return i;
    }
    else cerr << "BUG " << beg << " " << pt[beg] <<  endl;
}

void parse(char* s)
{
    char* b = buf;
    for(const char* p = s; *p; ++p)
    {
        if (*p==')' || *p == '(') *b++ = ' ';
        *b++ = *p;
        if (*p==')' || *p == '(') *b++ = ' ';
    }
    *b = 0;
    pt = split(buf, " \n");
 //   print(pt);
    cnode = 0;
    int beg = 0;
    go(beg);
//    REP(i, cnode)
//        cerr << i << " [" << tree[i].w << " '"<<tree[i].f<<"' " << tree[i].yes << " " << tree[i].no << "]\n";

}

void read()
{
    int cl, ca;
    scanf("%d\n", &cl);
    char* p = s;
    REP(i, cl)
    {
        gets(p);
        p = strchr(p, 0);
    }
    scanf("%d\n", &ca);
    f = vector<VS>(ca);
    REP(i, ca)
    {
        scanf("%s", &buf);
        f[i].push_back(buf);
        int j;
        for (scanf("%d", &j);j;--j) 
        {
            scanf("%s", &buf);
            f[i].push_back(buf);
        }
    }
//    cerr << s << endl;
//    REP(i, ca) print(f[i]);
    parse(s);
}

double solve(VS v)
{
    int i = 0;
    set<string> ff(v.begin() + 1, v.end());
    double res = 1.0;
    while (i!=-1)
    {
        res *= tree[i].w;
        if(ff.find(tree[i].f) != ff.end())
            i = tree[i].yes;
        else
            i = tree[i].no;
    }
    return res;
}

int main()
{
    int ct;
    scanf("%d\n", &ct);
    for (int t = 1; t <= ct; ++t)
    {
        read();
        printf("Case #%d:\n", t);
        REP(i, SI(f))
        {
            double res = solve(f[i]);
            printf("%.7lf\n", res);
        }
    }
    return 0;
}


