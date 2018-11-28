#include <cstdio>
#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FOREACH(i,c) for(typeof(c.begin()) i=(c).begin();i!=(c).end();++i)
#define REP(i,n) FOR(i,0,n)

#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

#define eps (1e-6)

int solve()
{
  int R, C, D;
  cin >> R >> C >> D;

  vector<vector<int> > allD(R+1, vector<int>(C+1));
  vector<vector<int> > sumD(R+1, vector<int>(C+1));
  vector<vector<int> > sumDX(R+1, vector<int>(C+1));
  vector<vector<int> > sumDY(R+1, vector<int>(C+1));

  REP(i, R) {
    int sum = 0;
    int sumX = 0;
    int sumY = 0;
    REP(j, C) {
      char c;
      cin >> c;
      c -= '0';
      allD[i+1][j+1] = c;
      sum += c;
      sumX += c*(j+1);
      sumY += c*(i+1);
      sumD[i+1][j+1] = sumD[i][j+1] + sum;
      sumDX[i+1][j+1] = sumDX[i][j+1] + sumX;
      sumDY[i+1][j+1] = sumDY[i][j+1] + sumY;
    }
  }
  //cout << "lala\n";
  for(int K=MIN(R,C); K>=3; K--) {
    //cout << "K=" << K << endl;
    REP(y, R-K+1) {
      REP(x, C-K+1) {
        //cout << "y, x= " << y << ", " << x << endl;
#if 1
        int sum = sumD[y][x] + sumD[y+K][x+K] - sumD[y+K][x] - sumD[y][x+K];
        int sumX = sumDX[y][x] + sumDX[y+K][x+K] - sumDX[y+K][x] - sumDX[y][x+K];
        int sumY = sumDY[y][x] + sumDY[y+K][x+K] - sumDY[y+K][x] - sumDY[y][x+K];
#else
        int sum = 0;
        int sumX = 0;
        int sumY = 0;
        for(int yy=y+1;yy<=y+K;yy++)
          for(int xx=x+1;xx<=x+K;xx++) {
            sum += allD[yy][xx];
            sumX += allD[yy][xx] * xx;
            sumY += allD[yy][xx] * yy;
          }
        if(sum != sumD[y][x] + sumD[y+K][x+K] - sumD[y+K][x] - sumD[y][x+K]) {
          cout << "ERROR" << endl;
        }
        if(sumX != sumDX[y][x] + sumDX[y+K][x+K] - sumDX[y+K][x] - sumDX[y][x+K]) {
          cout << "ERROR" << endl;
        }
        if(sumY != sumDY[y][x] + sumDY[y+K][x+K] - sumDY[y+K][x] - sumDY[y][x+K]) {
          cout << "ERROR" << endl;
        }
#endif

        sum  -= allD[y+1][x+1]       + allD[y+K][x+K]       + allD[y+K][x+1]       + allD[y+1][x+K];
        sumX -= allD[y+1][x+1]*(x+1) + allD[y+K][x+K]*(x+K) + allD[y+K][x+1]*(x+1) + allD[y+1][x+K]*(x+K);
        sumY -= allD[y+1][x+1]*(y+1) + allD[y+K][x+K]*(y+K) + allD[y+K][x+1]*(y+K) + allD[y+1][x+K]*(y+1);

        if(sum*(x+1+x+K)==sumX*2 && sum*(y+1+y+K)==sumY*2) {
          //cout << "y, x= " << y << ", " << x << endl;
          return K;
        }
      }
    }
  }
  return 0;
}

int main()
{
  int T;
  cin >> T;
  for(int i=0;i<T;i++) {
    cout << "Case #" << (i+1) << ": ";
    int ans = solve();
    if(ans>0) {
      cout << ans;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }
}
