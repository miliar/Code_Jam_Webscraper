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

#define FOR(i,n)  for(int i=0;i<(int)(n);i++)
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI;
typedef vector<VI> VVI;

ll_t dat[3][3];
int main()
{
  int t; 
  cin>>t;
  FOR(case_no,t)
    {
      ll_t n , A , B , C , D , x0 , y0 , M;
      cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
      vector<ll_t> X,Y;
      set<pair<ll_t,ll_t> > memo;
      memset(dat , 0 , sizeof(dat));
      {
        ll_t nx , ny;
        nx = x0;
        ny = y0;
        X.push_back(nx);
        Y.push_back(ny);
        memo.insert(MP(nx,ny));
        dat[nx%3][ny%3]++;
        FOR(i,n-1)
          {
            nx = (A * nx + B) % M;
            ny = (C * ny + D) % M;
            if(memo.find(MP(nx,ny)) != memo.end()) continue;
            memo.insert(MP(nx,ny));
            X.push_back(nx);
            Y.push_back(ny);
            dat[nx%3][ny%3]++;
          }
        n = SZ(X);
        //FOR(i,SZ(X)) cout << X[i] << " " << Y[i] << endl;
      }
      ll_t ans = 0;
      FOR(i,9){
        int xx = 0;
        int yy = 0;
        xx = i%3;
        yy = i/3;
        if(dat[xx][yy]==0) continue;
        FOR(j,i+1) {
          int xx2,yy2;
          xx2 = (j%3);
          yy2 = (j/3);
          if(dat[xx2][yy2]==0) continue;
          FOR(k,j+1)
            {
              int xx3 = k%3;
              int yy3 = k/3;
              if(dat[xx3][yy3]==0) continue;
              bool ok = (xx+xx2+xx3)%3==0 &&(yy+yy2+yy3)%3==0;
              if(ok){
                ll_t cnt = 1 ; 
                cnt *= dat[xx][yy] ; dat[xx][yy]--;
                cnt *= dat[xx2][yy2] ;dat[xx2][yy2]--;
                cnt *= dat[xx3][yy3] ;dat[xx3][yy3]--;
                dat[xx][yy]++;
                dat[xx2][yy2]++;
                dat[xx3][yy3]++;
                if(i==j && j==k) cnt /= 6;
                else if(
                        i==j || j==k || k==i
                        )
                  cnt /= 2;
                ans += cnt;
              }
            }
        }
      }
      printf("Case #%d: %lld\n" , case_no + 1 , ans);
    }
  return 0 ;
}
