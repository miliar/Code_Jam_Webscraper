#include <string>
#include <iostream>
#include <sstream>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <cmath>

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define gp(ans) {cout << "Case #" << ((test)+1) << ": " << (ans) << endl;}

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

struct Div {
  int speed;
  int len;
};

class L {
public:
    bool operator()(const Div& a, const Div& b)
    {
        return a.speed < b.speed;
    }
};

bool comp (const Div& a, const Div& b) {
  if (a.speed > b.speed) return true;
  else return false;
}

bool operator<(const Div& left, const Div& right)
{
  return left.speed < right.speed ;
}

bool operator>(const Div& left, const Div& right)
{
  return left.speed > right.speed ;
}

int main () {
  int test, T;

  cin >> T;
  REP (test, T) {
    int x,s,r,t,n;
    int i,j;
    cin >> x >> s >> r >> t >> n;
    Div divs_real[n+1];
    vector<Div> divs;
    int total = 0;
    REP(i,n){
      int b,e,w;
      cin >> b >> e >> w;
      struct Div div = {w, e-b};
      divs.push_back(div);
      total += (e-b);
    }
    int walklen = x-total;
    struct Div walkdiv = {0, walklen};
    divs.push_back(walkdiv);

    sort(divs.begin(), divs.end(), L());
    double res=0;
    double dt = t;
    REP(i,n+1){
      Div div = divs[i];
      double rspeed = div.speed + r;
      double wspeed = div.speed + s;
      double time = (double)div.len / rspeed;
      double rtime = min(time, dt);
      // rtime for run and rest is normal speed
      double wlen = (double)div.len - rtime*rspeed;
      double wtime = wlen / wspeed;
      res += rtime + wtime;
      dt -= rtime;
      //printf("runt: %f, walkt: %f, speed: %d, len: %d\n", rtime, wtime, div.speed, div.len);
    }
    //gp(res);
    printf("Case #%d: %.12f\n", test+1, res);
  }
  return 0;
}

