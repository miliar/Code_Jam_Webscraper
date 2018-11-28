#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <numeric>
#include <bitset>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

#define mem(a,b) (memset(a,b,sizeof(a)));
#define two(x) ((1)<<(x))
#define biti(a,i) (((a)>>(i)) & 1)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define foreach(i,a,b) for(int i=a;i<=b;i++)
#define rep(i,n) REP(i,0,n)
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

const int AMAX=1005;
int queueLenght;
int roundCnt;
LL A[AMAX];
LL sum[AMAX];
int acnt;

void init(){
    mem(A,0);
    mem(sum,0);
}

void calSum(){
    partial_sum(A,A+acnt,sum);
//    rep(i,acnt)cout<<sum[i]<<endl;
}

LL size(int i,int j){
    i%=acnt;
    j%=acnt;
    LL ret(0);
    if(j<i){
        ret+=sum[acnt-1]-sum[i]+A[i];
        ret+=sum[j];
    }else{
        ret+=sum[j]-sum[i]+A[i];
    }
    return ret;
}

int bSearch(int start,int end,int bound){
    int m;
    LL val(0);
    int l(start),r(end);
    while(l<=r){
        m=(l+r)/2;
        val=size(start,m);
//        cout<<l<<" "<<r<<"val:"<<val<<endl;
        if(val<=bound){
            l=m+1;
        }else{
            r=m-1;
        }
    }
    return r;
}

LL calAns(){
    LL ret(0);
    int l(0),r(acnt-1);
    rep(i,roundCnt){
        int pos=bSearch(l,r,queueLenght);
        ret+=size(l,pos);
//        cout<<l<<" "<<pos<<" "<<size(l,pos)<<endl;
        l=pos+1;r=l+acnt-1;
    }
    return ret;
}

int main(){
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int go;
    rint(go);
    for(int k=1;k<=go;k++){
        rint(roundCnt);
        rint(queueLenght);
        rint(acnt);
        rep(i,acnt){
            int t;
            rint(t);
            A[i]=t;
        }
        calSum();
        LL ans(0);
        ans=calAns();
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
	return 0;
}
