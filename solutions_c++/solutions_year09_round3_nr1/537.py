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

int H[257];
int base;
int val;
int cnt;

void initH(char* s){
       base=0;
       val=1;
       cnt=0;
       mem(H,-1);
       while(*s){
              char c=*s;
              if(H[c]==-1){
                     base++;
                     if(cnt==0){
                            cnt++;
                            val=1;
                            H[c]=val++;
                     }else if(cnt==1){
                            cnt++;
                            H[c]=0;
                     }else{
                            cnt++;
                            H[c]=val++;
                     }
              }
              s++;
       }
       if(cnt==1){
              base=2;
       }
}

LL convert(char* s){
       LL ret=0;
       int len=strlen(s);
       for(int i=0;i<len;i++){
              ret=ret*base+H[*s];
              s++;
       }
       return ret;
}

char buf[1000];
void sol(){
       gets(buf);
       initH(buf);
       LL ans=convert(buf);
       static int go=0;
       go++;
       cout<<"Case #"<<go<<": "<<ans<<endl;
}

int main(){
//       freopen("in.txt","r",stdin);
//       freopen("out.txt","w",stdout);
       int t;
       rint(t);
       getchar();
       while(t--){
              sol();
       }
	return 0;
}
