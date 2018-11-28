#include <iostream>
#include <vector>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <cstdlib>
#include <string.h>
#include <memory.h>
using namespace std;
template <class T> void OUT(T x, int n){  for(int i = 1; i <= n; ++i)  cout << x[i] << ' ';    cout << endl;    }
template <class T> void OUT(T x, int n, int m){  for(int i = 1; i <= n; ++i)    OUT(x[i], m);    cout << endl;    }
template <class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
#define  eps 1e-8
#define  LL long long
inline LL mod(LL x, LL y) { return x - floor(1.0 * x / y+eps) * y; }
#define  out(x) (cout << #x << " = " << x << endl)
#define  Set(a,b)  memset(a,b,sizeof(a))
#define  Sqr(x) ((x) * (x))
#define  pi  acos(-1.0)
const int maxn = 1005,INF = (1<<29);
LL n,m;

LL gcd(LL a,LL b){
	return b?gcd(b,a%b):a;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k,t,T,x,y,sum,index;
    cin>>T;
    int pd,pg;
    bool fail=0;
    for(t=1;t<=T;t++){
        cin>>n>>pd>>pg;
        if(pg==0&&pd!=0) fail=1;
        else if(pg==0&&pd==0) fail=0;
        else if(pg==100&&pd!=100) fail=1;
        else {
            x=gcd(100,pd);
//            out(100/x);
            if((100/x)<=n)  fail=0;
            else fail=1;
        }
        if(!fail) printf("Case #%d: Possible\n",t);
        else printf("Case #%d: Broken\n",t);
    }
    return 0;
}
