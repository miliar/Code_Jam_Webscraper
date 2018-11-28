#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

const double PI = acos(-1.0);
const int MAXINT = 0x7FFFFFFF;
typedef long long int64;
const int64 MAXINT64 = 0x7FFFFFFFFFFFFFFFLL;

#define PS(x) (cout<<#x<<": "<<endl)
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define MST(t,v) memset(t,v,sizeof(t))
#define SHOW1(a,n) (PS(a),_show1(a,n))
#define SHOW2(a,r,c) (PS(a),_show2(a,r,c))

template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;} 
template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}


int K, ret;
char str[50024];
char str2[50024];
int a[20];
bool V[20];
void F()
{
    int i, r;
    for(i = 0; i < strlen(str); ++i)
    {
        str2[i] = str[(i - i % K) + a[i % K]];
    }
    str2[i] = '\0';
    r = 1;
    for(i = 1; i < strlen(str); ++i)
        if(str2[i] != str2[i - 1]) ++r;
    if(r < ret) ret = r;
}
void A(int p)
{
     if(p >= K) F();
     else
     {
         int i;
         for(i = 0; i < K; ++i)
             if(!V[i])
             {
                 V[i] = 1;
                 a[p] = i;
                 A(p + 1);
                 V[i] = 0;
             }
     }
}
int main()
{
    int t, ctr;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    for(ctr = 1; ctr <= t; ctr++)
    {
        scanf("%d", &K);
        scanf("%s", str);
        memset(V, 0, sizeof(V));
        ret = strlen(str);
        A(0);
        printf("Case #%d: %d\n", ctr, ret);
    }
}