#include <iostream>
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
#define two(x) ((1)<<(x))
#define REP(i,a,b) for(int i=a;i<b;i++)
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
template <class T> void out(T x, int n){  for(int i = 1; i <= n; ++i)  cout << x[i] << ' ';    cout << endl;    }
template <class T> void out(T x, int n, int m){  for(int i = 1; i <= n; ++i)    out(x[i], m);    cout << endl;    }
template<class T>T sqr(T a){return a*a;}
template<class T>T gcd(T a,T b){return b==0?a:gcd(b,a%b);}
template<class T>inline bool checkmax(T&a,const T&b){return a<b?a=b,1:0;}
template<class T>inline bool checkmin(T&a,const T&b){return a>b?a=b,1:0;}
template<class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
template<class T>T dis(T x1,T y1,T x2,T y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
int lowbit(int x){return x&(-x);}
template<class T>void printbit(T a){cout<<bitset<17>(a)<<endl;}

const int INF=1e9;


const int NMAX=10;
int A[NMAX];
int acnt;
const int BMAX=150;
int bcnt;
bool B[BMAX];

int calAns(int A[]){
       int ret=0;
       mem(B,0);
       rep(i,acnt){
              int sp=A[i];
              int cnt=0;
              for(int p=sp-1;p>=0;p--){
                     if(B[p]!=0){
                            break;
                     }else{cnt++;}
              }
              for(int p=sp+1;p<bcnt;p++){
                     if(B[p]!=0){
                            break;
                     }else{cnt++;}
              }
              ret+=cnt;
              B[sp]=1;
//              cout<<cnt<<endl;
//              out(B-1,bcnt);
       }
       return ret;
}

int search(){
       sort(A,A+acnt);
       int best=INF;
       do{
              int cur=calAns(A);
//              out(A-1,acnt);
              checkmin(best,cur);
       }while(next_permutation(A,A+acnt));
       return best;
}

void sol(){
       rint(bcnt);
       rint(acnt);
       rep(i,acnt){
              rint(A[i]);
              A[i]--;
       }
       int ans=search();
       static int go=0;
       go++;
       cout<<"Case #"<<go<<": "<<ans<<endl;
}


int main(){
//       freopen("in.txt","r",stdin);
//       freopen("out.txt","w",stdout);
       int t;
       rint(t);
       while(t--){
              sol();
       }
	return 0;
}
