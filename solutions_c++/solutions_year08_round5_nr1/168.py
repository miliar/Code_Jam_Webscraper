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

#define BET(a,i,b) (((a)<=(i))&&((i)<(b)))
#define FOR(i,n)  for(int i=0;i<(int)(n);i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef complex<int> xy_t;
int dx[] = {0,1,0,-1};
int dy[] = {1,0,-1,0};
void solve()
{
  int L; cin >> L;
  vector<xy_t> p;
  p.push_back(xy_t(0,0));
  int dir = 0 ;
  xy_t pos(0,0);
  ll_t ans = 0 ;
  FOR(i,L)
    {
      string S ; int T;
      cin>>S>>T;
      FOR(j,T){
        FOR(k,SZ(S))
          {
            char c = S[k];
            if(c=='F')
              {
                pos += xy_t(dx[dir]*2,dy[dir]*2);
                p.push_back(pos);
              }
            else if(c=='L'){
              dir = (dir+1)%4;
            }else if(c=='R'){
              dir = (dir+3)%4;
            }else abort();
          }
      }
    }
  FOR(i,204) {
    int x = 2*(i-102)+1;
    FOR(j,204){
      int y = 2*(j-102)+1;
      int lx , rx , ly , ry;
      lx = rx = ly = ry = 0;
      FOR(k,SZ(p)){
        xy_t p1 = p[k];
        xy_t p2 = p[(k+1)%SZ(p)];
        if(p1.real() == x) abort();
        if(p1.imag() == y) abort();
        if(BET(p1.real(),x,p2.real()) || BET(p2.real(),x,p1.real())){
          if(p1.imag() < y) ly ++ ;
          else              ry ++ ; 
        }else if(BET(p1.imag(),y,p2.imag()) || BET(p2.imag(),y,p1.imag())){
          if(p1.real() < x) lx ++ ;
          else              rx ++ ; 
        }
      }
      bool b1 = lx && rx && lx%2==0 && rx%2==0 ; 
      bool b2 = ly && ry && ly%2==0 && ry%2==0 ; 
      if(b1 || b2) {
        //cout<<x << " " << y << endl;
        ans ++ ;
      }
    }
  }
  cout << ans << endl;
}

int main()
{
  int t; 
  cin>>t;
  FOR(case_no,t)
    {
      printf("Case #%d: " , case_no + 1 );
      solve();
    }
  return 0 ;
}
