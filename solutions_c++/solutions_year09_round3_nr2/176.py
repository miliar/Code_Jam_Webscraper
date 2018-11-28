#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<queue>
#include<stack>
#include<deque>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<set>
#include<map>
#include<fstream>
#include<complex>
#include<cassert>
#include<climits>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;
const double PI = 3.14159265;
const int M = 500;

double vx[M][3], x[M][3], gx[3], vgx[3];

int main()
{
  int T;
  cin >> T;
  REP(turn, T){
    int N;
    cin >> N;
    REP(i,3){
      gx[i] = vgx[i] = 0;
    }

    REP(i, N){
      REP(j,3){
        cin >> x[i][j];
        gx[j] += x[i][j];
      }
      REP(j,3){
        cin >> vx[i][j];
        vgx[j] += vx[i][j];
      }
    }
    REP(i,3){
      gx[i] /= N;
      vgx[i] /= N;
    }
    double a = 0, b = 0;
    REP(i, 3){
      a += gx[i] * vgx[i];
      b += vgx[i] * vgx[i];
    }
    //cerr << a << b << endl;
    double t = 0;
    if(b != 0){
      t = - a / b;
    }
    if(t < 0){
      t = 0;
    }
    //assert(t > 0);
    double d = 0;
    REP(i, 3){
      double xt = gx[i] + t * vgx[i];
      d += xt * xt;
    }
    d = sqrt(d);
    printf("Case #%d: %.9f %.9f\n", turn+1, d, t);
    //cout << d << ',' << t << endl;
  }
  return 0;
}

