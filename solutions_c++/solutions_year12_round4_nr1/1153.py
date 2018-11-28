//#include "debug.h"
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
const double pi=acos(-1.0);//NOTES:pi
typedef long long i64;
typedef unsigned long long u64;
const int intmax=0x3f3f3f3f;//NOTES:intmax
//const i64 i64max=0x3f3f3f3f3f3f3f3fi64;//NOTES:i64max
double eps=1e-6;//NOTES:eps
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
template<class T> inline T sqr(T x){return x*x;}//NOTES:sqr
template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//NOTES:lowbit(
template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}//NOTES:countbit(
template<class T> inline T checkmod(T n,T m) {return (n%m+m)%m;}//NOTES:checkMod(
inline int rand(int a, int b) {if(a >= b) return a; return rand() % (b-a) + a;}//NOTES:rand(
//Numberic Functions
template<class T> inline T gcd(T a,T b)//NOTES:gcd(
{if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
template<class T> inline T lcm(T a,T b)//NOTES:lcm(
{if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
template<class T> inline T euclid(T a,T b,T &x,T &y)//NOTES:euclide(
{if(a<0){T d=euclid(-a,b,x,y);x=-x;return d;}
if(b<0){T d=euclid(a,-b,x,y);y=-y;return d;}
if(b==0){x=1;y=0;return a;}else{T d=euclid(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
template<class T> inline vector<pair<T,int> > factorize(T n)//NOTES:factorize(
{vector<pair<T,int> > R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}
i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
template<class T> inline bool isPrimeNumber(T n)//NOTES:isPrimeNumber(
{if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
template<class T> inline T eularFunction(T n)//NOTES:eularFunction(
{vector<pair<T,int> > R=factorize(n);T r=n;for (int i=0;i<R.size();i++)r=r/R[i].first*(R[i].first-1);return r;}
template<class T> inline int dblcmp(T a, T b){a-=b; return a>eps?1:(a<-eps?-1:0);}//NOTES:doublecmp
#define mem(a, val) memset(a, val, sizeof(a))//memset(
#define For(i, a, b) for(int i=a; i<b; ++i)//for
#define ff(i, b) for(int i=0; i<b; ++i)

const int N = 11000;

struct NODE{
    int d, l;
    bool operator<(const NODE &b)const{
        return d < b.d;
    }
}in[N], q[N];
int head, tail;

int maxl[N];
bool judge2(int n, int len){
    maxl[0] = in[0].d;
    for(int i=1; i<n; ++i){
        maxl[i] = 0;
        for(int j=0; j<i; ++j){
            if(in[j].d + maxl[j] >= in[i].d){
                checkmax(maxl[i], min(in[i].l, in[i].d-in[j].d));
            }
        }
    }
    for(int i=0; i<n; ++i){
        if(in[i].d + maxl[i] >= len) return true;
    }
    return false;
}
bool judge(int n, int len){
    if(in[0].d > in[0].l) return false;
    int p= 0, l = in[0].d;
    for(int i=1; i<n; ++i){
        if(in[i].d  > in[p].d+l) return false;
        int temp = 0;
        temp = in[i].d + min(in[i].d - in[p].d, in[i].l);
        if(temp > in[p].d + l){

            l = min(in[i].d - in[p].d, in[i].l);

            p = i;
        }
        //checkmax(maxl, in[i].d + in[i].l);
    }
    printf("%d %d %d\n", p, in[p].d, l);
   return in[p].d + l >= len; 
}
int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int cases;
    scanf("%d", &cases);
    for(int I=1; I<=cases; ++I)
    {
        int n;
        scanf("%d", &n);
        for(int i=0; i<n; ++i){
            scanf("%d%d", &in[i].d, &in[i].l);
        }
        int len;
        scanf("%d", &len);
        sort(in, in+n);
        if(judge2(n, len)) printf("Case #%d: YES\n", I);
        else printf("Case #%d: NO\n", I);
    }
    return 0;
}
