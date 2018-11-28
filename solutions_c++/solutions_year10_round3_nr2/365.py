#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <stack>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

#define mem(a,b) (memset(a,b,sizeof(a)));
#define two(x) ((1L)<<(x))
#define biti(a,i) (((a)>>(i)) & 1)
#define foreach(i,a,b) for(int i=a;i<=b;i++)
#define rep(i,n) for(int i=0;i<n;i++)
#define SIZE(x) ((int)(x).size())
#define MP(x,y) make_pair(x,y)
#define rint(x) scanf("%d",&x)
#define rdbl(x) scanf("%lf",&x)
#define OUT(x) (cout << #x << " = " << x << endl)
#define  pi  acos(-1)

typedef pair<int,int> PI;
typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VII;
template <class T> void out(T x, int n){  for(int i = 1; i <= n; ++i)  cout <<setw(3)<< x[i] << ' ';    cout << endl;    }
template <class T> void out(T x, int n, int m){  for(int i = 1; i <= n; ++i)    out(x[i], m);    cout << endl;    }
template<class T>T sqr(T a){return a*a;}
template<class T>T gcd(T a,T b){return b==0?a:gcd(b,a%b);}
template<class T>inline bool checkmax(T&a,const T&b){return a<b?a=b,1:0;}
template<class T>inline bool checkmin(T&a,const T&b){return a>b?a=b,1:0;}
template<class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
template<class T>T dis(T x1,T y1,T x2,T y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
int lowbit(int x){return x&(-x);}
template<class T>void printbit(T a){cout<<bitset<17>(a)<<endl;}

const int INF=1000000000;

int num(int l,int n,int c){
    int cnt(0);
    while(1){
        int nn=n/c;
        if(n%c!=0)nn++;
        n=nn;
        cnt++;
        if(n<=l)return cnt;
    }
    return cnt;
}

int search(int a,int b,int c){
    LL k=num(a,b,c);
//    cout<<"k:"<<k<<endl;
    if(k<=1)return 0;
    int t=1;
    while(1){
        if(two(t-1)<k && k<=two(t))break;
        t++;
    }
    return t;
}

int main(){
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);

    int go;
    rint(go);
    foreach(gg,1,go){
        int a,b,c;
        rint(a);rint(b);rint(c);
        int ans=search(a,b,c);
        cout<<"Case #"<<gg<<": "<<ans<<endl;
    }
	return 0;	return 0;
}
