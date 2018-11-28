#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
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

#include<windows.h>
#include<process.h>

using namespace std;
#define BET(a,b,c) ((a)<=(b)&&(b)<(c))
#define FOR(i,n) for(int i=0,i##_end=(int(n));i<i##_end;i++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;
const double PI = 4.0*atan(1.0);

string WELCOME = "welcome to code jam";

int memo[550][50];

int dfs(string& s , int p1 = 0 , int p2 = 0)
{
  if(p2==SZ(WELCOME)) return 1;
  if(p1==SZ(s)) return 0 ;
  int& ret = memo[p1][p2];
  if(ret != -1) return ret;
  int val = 0 ;
  val = dfs(s , p1+1 , p2);
  if(s[p1]==WELCOME[p2]){
    val += dfs(s , p1+1 , p2+1);
  }
  return ret=val % 10000;
}

int main() {
  int t,case_no=1;
  cin>>t;
  string line;
  getline(cin,line);
  while(t--){
    int ans = 0 ; 
    getline(cin,line);
    memset(memo , -1 , sizeof(memo));
    ans = dfs(line);
    printf("Case #%d: %04d\n", case_no++ , ans);
  }
  return 0 ;
}
