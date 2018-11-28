#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <ctime>
#include <cstdlib>

using namespace std;
int N;
double W, L;
int limit = 100;

struct Pos {
  double x;
  double y;
  double r;
  Pos(double x, double y, double r):x(x),y(y),r(r){}

  void print() const {
    cout.precision(10);
    cout<<" "<<x<<" "<<y;
  }
};

void print(vector<Pos> const& s) {
  for(int i=0;i<s.size();++i) {
    s[i].print();
  }
}
bool consistent(vector<Pos> const& s, Pos t) {
  for(int i=0;i<s.size();++i) {
      double dx = s[i].x - t.x;
      double dy = s[i].y - t.y;
      double rr = s[i].r + t.r;
      if(dx*dx + dy*dy < rr*rr) {
        //cerr<<"Radius: "<<rr<<"  Needed: "<<sqrt(dx*dx+dy*dy)<<endl;
        return false;
      }
  }
  return true;
}

bool random(vector<double> const& r, vector<Pos> & out) {
  out.clear();

  for(int i=0;i<N;++i) {
    bool ok=false;
    for(int j=0;j<limit/10;++j) {
      double x = rand() * W / RAND_MAX;
      double y = rand() * L / RAND_MAX;
      //cerr<<"Try "<<i<<" "<<r[i]<<" "<<x<<"("<<W<<") "<<y<<" ("<<L<<") --  "<<j<<" - "<<limit<<endl;
      Pos newp(x, y, r[i]);
      if(consistent(out, newp)) {
        ok = true;
        cerr<<"ok"<<endl;
        out.push_back(newp);
        break;
      }
    }
    if(!ok) {
      cerr<<"fail"<<endl;
      limit++;
      return false;
    }
  }
  return true;
}

void testcase() {
  cin>>N>>W>>L;
  vector<double> r;
  for(int i=0;i<N;++i) {
    double rr;
    cin>>rr;
    r.push_back(rr);
  }
  vector<Pos> solution;

  limit = 100;
  while(!random(r, solution)) {};
  print(solution);
}

int main(int argc, char** argv) {
  srand(time(0));
  int T;
  cin>>T;
  for(int n=0;n<T;++n) {
    cout<<"Case #"<<n+1<<":";
    testcase();
    cout<<endl;
  }

  return 0;
}
