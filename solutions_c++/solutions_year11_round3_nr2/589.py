#include <iostream>
#include <string>
#include <cmath>
#include <climits>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <ctime>
#include <iomanip>
#include <map>
#include <memory.h>
using namespace std;

typedef long long int64; // 2 ^ 63 - 1 = 9223372036854775807.
typedef unsigned long long uint64; // 2 ^ 64 - 1 = 18446744073709551615.
const double EPS = 1e-8;
const double PI = acos(-1.0);
const int INT_INF = INT_MAX / 2;
const int64 INT64_INF = 1LL << 61;
#define mem(a, b) memset(a, b, sizeof(a))
#define Sqr(x) ((x) * (x))
template <class T> inline T Max(T a, T b) { if (a < b) a = b; return a; }
template <class T> inline T Min(T a, T b) { if (a > b) a = b; return a; }
template <class T> inline void Swap(T & a, T & b) { T t = a; a = b; b = t; }
inline int64 MOD(int64 x, int64 y) { return x - (floor)(1.0 * x / y + EPS) * y; }
inline int mod(int a, int b) { a %= b; return a < 0 ? a + b : a; }
inline int sgn(const double & a)
{ // 返回1表示大于0，0表示等于0，-1表示小于0.
    return (a > EPS) - (a < -EPS);
}

template <class T> void out(T x, int n) { for(int i = 0; i < n; ++i) cout << x[i] << ' '; cout << endl; }
template <class T> void out(T x, int n, int m) {  for(int i = 0; i < n; ++i) out(x[i], m); cout << endl; }
#define Out(x) (cout << #x << " = " << x << " ")
#define Outendl(x) (cout << #x << " = " << x << endl)

long long T,L,t,N,C;
long long a[1010];
long long b[1010],p;

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    long long h,i,j,k;
    scanf("%d",&T);
    for(h=1;h<=T;++h)
    {
        cout<<"Case #"<<h<<": ";
        cin>>L>>t>>N>>C;
        for(i=0;i<C;++i)
        {
            cin>>a[i];
            a[i]<<=1;
        }
        long long sum=0,tot;
        for(i=0,j=0;sum<t&&j<N;i=(i+1)%C,++j)
            sum+=a[i];
        if(sum>=t)
        {
            tot=sum;
            p=0;
            b[p++]=sum-t;
            for(;j<N;i=(i+1)%C,++j)
            {
                tot+=a[i];
                b[p++]=a[i];
            }
            if(p<=L)
            {
                cout<<tot/2<<endl;
            }
            else
            {
                sort(b,b+p);
                sum=0;
                for(i=p-1;i>=p-L;--i)
                    sum+=b[i];
                cout<<sum/2+tot-sum<<endl;
            }
        }
        else
        {
            cout<<sum<<endl;
        }
    }
}
