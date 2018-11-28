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
#define REP(x) for(int i=0;i<x;i++)
#define IREP(i,x) for(int i=0;i<x;i++)
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

const int INF=1000000000;


const int VMAX=INF;
//bool V[INF];
//bitset<INF> V;
map<int,int> V;
//want 0 to be ¡°0¡± instead of ¡°¡±, unseal
//or ¡°avoid¡± n being 0
void decToBase(int n,int base,char* R){
       int len=0;
       while(n){
              R[len]="0123456789ABCDEFG"[n%base];
              len++;
              n/=base;
       }
       reverse(R,R+len);
       R[len++]=0;
}

int baseToDec(char* n,int base){
       int ret=0;
       for(;*n;n++){ret=ret*base+(*n)-'0';}
       return ret;
}

int sum(char*s){
       int ret=0;
       while(*s){
              int t=*s-'0';
              t*=t;
              ret+=t;
              s++;
       }
       return ret;
}

char A[10000];
char B[10000];
int test(int n,int base){
       V.clear();
       while(1){
              decToBase(n,base,A);
//              cout<<"num: "<<A<<endl;
              n=sum(A);
//              cout<<n<<endl;
//              puts("...");
              if(n==1)return 1;
              if(V[n]==1)return 0;
              V[n]=1;
       }
}

int base_seed[20];
int basecnt;

int search(){
       for(int i=2;i<INF;i++){
              int found=1;
              for(int j=0;j<basecnt;j++){
                     if(test(i,base_seed[j])==0){
                            found=0;break;
                     }
              }
              if(found)return i;
       }
}

void init(){
}

char* eatWhite(char*s){
       while(*s && (*s==' ' || *s=='\t'))s++;
       return s;
}

char* read(char* s,char* r){
       s=eatWhite(s);
       int i=0;
       for(;*s && *s!=' ' && *s!='\t';s++,i++){
              r[i]=*s;
       }
       r[i]=0;
       return s;
}


char buf[1000];
char num[10];
void sol(){
       gets(buf);
//       cout<<buf<<endl;
       char*s =buf;
       basecnt=0;
       while(*s){
              s=read(s,num);
              int n;
//              if(sscanf(s,"%d",&n)==1)
//              cout<<s<<endl;
//              cout<<num<<endl;
//              int n;
              if(sscanf(num,"%d",&n)==1){
                     base_seed[basecnt++]=n;
//                     cout<<n<<endl;
              }
       }
//       out(base_seed-1,basecnt);
       static int t=0;
       t++;
       printf("Case #%d: ",t);
       int ans=search();
       printf("%d",ans);puts("");//debug
}


int main(){
//       freopen("in.txt","r",stdin);
//       freopen("out.out","w",stdout);
       int t;
       rint(t);getchar();
       while(t--){
              sol();
       }
	return 0;
}
