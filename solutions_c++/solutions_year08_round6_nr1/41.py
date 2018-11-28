#include<iostream>
#include<sstream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>

using namespace std;

#define BET(a,i,b) (((a)<=(i))&&((i)<=(b)))
#define FOR(i,n)  for(int i=0;i<(int)(n);i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
int N,M;
int X[1010];
int Y[1010];
bool b[1010];

bool is_bird(int x , int y) // bird ->ok
{
  int x1,x2,y1,y2;
  x1 = x2 = x ; 
  y1 = y2 = y ; 
  FOR(i,N) if(b[i]){
    x1 <?= X[i];
    y1 <?= Y[i];
    x2 >?= X[i];
    y2 >?= Y[i];
  }
  FOR(i,N) if(!b[i]){
    if(BET(x1,X[i],x2)&&BET(y1,Y[i],y2)){
      return false;
    }
  }
  return true;
}

bool is_not_bird(int x , int y) // not ->ok
{
  int x1,x2,y1,y2;
  x1 = y1 = 1<<28; 
  x2 = y2 = 0;
  FOR(i,N) if(b[i]){
    x1 <?= X[i];
    y1 <?= Y[i];
    x2 >?= X[i];
    y2 >?= Y[i];
  }
  if(BET(x1,x,x2) && BET(y1,y,y2)){
    return false;
  }
  return true;
}

void solve()
{

  cin>>N;
  FOR(i,N)
    {
      string s;
      cin>>X[i]>>Y[i]>>s;
      if(s=="BIRD")
        b[i] = true;
      else{
        b[i] = false;
        cin>>s;
      }
    }
  int M ; 
  cin>>M;
  FOR(i,M)
    {
      int a,b;
      cin>>a>>b;
      bool b1 =is_bird(a,b) ;
      bool b2 =is_not_bird(a,b) ;
      if(b1&&b2){
        puts("UNKNOWN");
      }else if(is_not_bird(a,b)){
        puts("NOT BIRD");
      }else{
        puts("BIRD");
      }
    }
}

int main()
{
  int t; 
  cin>>t;
  FOR(case_no,t)
    {
      printf("Case #%d:\n" , case_no + 1 );
      solve();
    }
  return 0 ;
}
