#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<functional>
#include<sstream>
#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define allv(v) (v).begin(),(v).end()
#define rall(v) (v).begin(),(v).rend()
#define _foreach(it,b,e) for(__typeof__(b); it!=(e);++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;
const int maxn = 555;

int n,s,p;
int sum[maxn];
int best[maxn][maxn];
int dah[41][11][2];
int can(int a, int b, int c){
  if(dah[a][b][c]==-1){
    int ret = 0;
    for(int i=0;i<=10;i++){
      for(int j=0;j<=10;j++){
        int k = a - i - j;
        if(k<0 || k>10)continue;
        if(c==1){
          if(abs(i-j)<=2 && abs(i-k)<=2 && abs(k-j)<=2 && (abs(i-j)==2 || abs(i-k)==2 || abs(k-j)==2) && (i>=b || j>=b || k>=b))ret=1;
        }else{
          if(abs(i-j)<=1 && abs(i-k)<=1 && abs(k-j)<=1 && (i>=b || j>=b || k>=b))ret=1;
        }
        
      }
    }
    dah[a][b][c]=ret;
  }
  return dah[a][b][c];
}
int go(int a,int b){
  if(b<0)return -inf;
  if(a==n && b==0)return 0;
  else if(a==n) return -inf;
  if(best[a][b]<-inf){
    int ret = -inf;
    ret=max(ret, go(a+1,b));
    if(sum[a]>=2 && sum[a]<=28)
      ret=max(ret, go(a+1,b-1));      

    if(can(sum[a],p, 0))
      ret = max(ret,1+ go(a+1,b));
    if(can(sum[a],p, 1))
      ret = max(ret,1+ go(a+1,b-1));
    best[a][b] = ret;
  }
  return best[a][b];
}
int main ()
{
  int tt;
  scanf("%d",&tt);
  memset(dah,-1,sizeof(dah));

  
  for(int pp=1;pp<=tt;pp++)
    {
      for(int i=0;i<=n+5;i++)
        for(int j=0;j<=n+5;j++)
          best[i][j]= -(inf+1000);

      scanf("%d %d %d",&n,&s,&p);
      for(int i=0;i<n;i++)
        scanf("%d",&sum[i]);
      printf("Case #%d: %d\n",pp,go(0,s));
    }
  return 0;
}
