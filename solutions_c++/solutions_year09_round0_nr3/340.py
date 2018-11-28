#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <iomanip>
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
typedef pair<int,int> PI;
typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VII;
template<class T>T sqr(T a){return a*a;}
template<class T>T gcd(T a,T b){return b==0?a:gcd(b,a%b);}
template<class T>inline bool checkmax(T&a,const T&b){return a<b?a=b,1:0;}
template<class T>inline bool checkmin(T&a,const T&b){return a>b?a=b,1:0;}
template<class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
template<class T>T dis(T x1,T y1,T x2,T y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
int lowbit(int x){return x&(-x);}
template<class T>void printbit(T a){cout<<bitset<17>(a)<<endl;}

const int AMAX=505;
const int BMAX=100;
char A[AMAX];
char B[]={" welcome to code jam"};
int acnt;
const int bcnt=19;
int D[AMAX][AMAX];
const int INF=100000000;
int mod=10000;

void dp(){
       for(int i=0;i<AMAX;i++)for(int j=0;j<AMAX;j++)D[i][j]=INF;
       D[0][0]=1;
       for(int a=1;a<=acnt;a++){
              for(int b=1;b<=bcnt;b++){
                     int val=0;
                     if(A[a]==B[b]){
                            for(int i=b-1;i<=a-1;i++){
                                   if(A[i]==B[b-1]){
                                          val+=D[i][b-1];
                                          val%=mod;
                                   }
                            }
                     }
                     D[a][b]=val;
              }
       }
}

void input(){
       A[0]=' ';
       gets(A+1);
       acnt=strlen(A+1);
}


int calAns(){
       int sum=0;
       for(int i=1;i<=acnt;i++){
              sum+=D[i][bcnt];
              sum%=mod;
       }
       return sum;
}


int main(){
//       freopen("in.txt","r",stdin);
//       freopen("out.txt","w",stdout);
       int go;
       scanf("%d\n",&go);
       for(int i=1;i<=go;i++){
              input();
              dp();
              int ans=calAns();
              printf("Case #%d: ",i);
              printf("%.4d",ans);puts("");//debug
       }

	return 0;
}
