// compile with "g++ XXX.cc -mno-cygwin -O2" in Cygwin

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

int N,M;

int S[50][50],W[50][50],T[50][50];

struct data_t{
  int row , col;
  ll_t step;
};

bool operator<(const data_t& d1 , const data_t& d2){
  return d1.step > d2.step;
}

bool visited[100][100];

int dx[]={0,1,0,-1};
int dy[]={1,0,-1,0};

bool is_crossroad(int r1, int c1 , int r2 , int c2)
{
  int r = min(r1,r2) , c = min(c1,c2);
  if(r1==r2){
    return c%2==0;
  }else{
    return r%2==0;
  }
}

ll_t reg(ll_t x , ll_t mod)
{
  if(x < 0){
    return (x%mod+mod)%mod;
  }else{
    return x % mod;
  }
}

ll_t next_available(int r1, int c1 , int r2 , int c2 , ll_t now_time)
{
  //cout << "now_time : " << now_time << endl;
  if(!is_crossroad(r1,c1,r2,c2)) {
    //cout << "ok" << endl;
    return now_time;
  }else{
    int r = r1/2 , c = c1/2;
    ll_t cycle = S[r][c] + W[r][c] ;
    ll_t t = T[r][c] % cycle;
    int p = reg(now_time-t , cycle);
    // S - W - S - W
    if(r1==r2){      
      if(p >= S[r][c]) return now_time;
      assert((S[r][c]-p)>=0);
      //cout << "@" << now_time << " " << S[r][c]-p << endl;
      return now_time + S[r][c] - p ; 
    }else{
      if(p < S[r][c]) return now_time;
      assert((cycle - p) >= 0);
      //cout << "@" << now_time << " " << cycle - p << endl;
      return now_time + cycle - p ;
    }
  }
  return now_time;
}

int cost(int r1, int c1 , int r2 , int c2)
{
  if(is_crossroad(r1,c1,r2,c2)) return 1;
  return 2;
}

int solve()
{
  int S_row = 2*N-1 , S_col=0;
  int G_row = 0 , G_col = 2*M-1;
  priority_queue<data_t> qu;
  qu.push((data_t){S_row,S_col,0});
  memset(visited , 0 , sizeof(visited));
  while(!qu.empty()){
    data_t now = qu.top() ; qu.pop();
    if(visited[now.row][now.col]) continue;
    //cout << now.row << " " << now.col << " " << now.step << endl;
    visited[now.row][now.col]=true;
    if(now.row==G_row && now.col==G_col){
      return now.step;
    }
    FOR(k,4){
      int nr = now.row + dy[k];
      int nc = now.col + dx[k];
      if(BET(0,nr,2*N) && BET(0,nc,2*M)){
        ll_t next = next_available(now.row,now.col,nr,nc,now.step);       
        //cout << "! " << next << " " << now.step << endl;
        //assert(next >= now.step) ;
        qu.push((data_t){nr,nc,next+cost(now.row,now.col,nr,nc)});
      }
    }
  }
  abort();
  return -1;
}

int main() {
  int t,case_no=1;
  cin>>t;
  string line;
  while(t--){
    int ans = -1 ;
    cin>>N>>M;
    FOR(i,N){
      FOR(j,M){
        cin>>S[i][j]>>W[i][j]>>T[i][j];
      }
    }
    ans = solve();
    printf("Case #%d: %d\n" , case_no++ , ans);
  }
  return 0 ;
}
