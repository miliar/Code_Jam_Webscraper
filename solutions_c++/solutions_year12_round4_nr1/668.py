#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>

using namespace std;

struct State {
  int pos;
  int vine;
  State(int p, int v):pos(p),vine(v){}

  bool operator<(State const& rhs) const {
    if(pos != rhs.pos)
      return pos<rhs.pos;
    return vine<rhs.vine;
  }
};
struct Vine {
  int d;
  int l;
  Vine(int d, int l):d(d),l(l){}
};

bool testcase() {
  int N;
  cin>>N;
  vector<Vine> vines;
  for(int i=0;i<N;++i) {
    int d, l;
    cin>>d>>l;
    vines.push_back(Vine(d, l));
  }
  int goal;
  cin>>goal;
  vines.push_back(Vine(goal, 0));

  queue<State> states;
  set<State> visited;
  State init(0, 0);
  states.push(init);
  visited.insert(init);

  while(!states.empty()) {
    State now = states.front();
    states.pop();

    int swing = vines[now.vine].d - now.pos;
    if(swing > vines[now.vine].l) {
      swing = vines[now.vine].l;
    }
    int reach = vines[now.vine].d + swing;
    for(int j=now.vine+1;j<=N;++j) {
      if(vines[j].d <= reach) {
        if(j == N) {
          return true;
        }
        State next(vines[now.vine].d, j);
        if(visited.find(next)==visited.end()) {
          visited.insert(next);
          states.push(next);
          //cerr<<"£ "<<now.vine<<" -> "<<j<<endl;
        }
      }
    }
  }

  return false;
}

int main(int argc, char** argv) {
  int N;
  cin>>N;
  for(int n=0;n<N;++n) {
    cout<<"Case #"<<n+1<<": ";
    bool res = testcase();
    if(res)
      cout<<"YES"<<endl;
    else
      cout<<"NO"<<endl;
  }

  return 0;
}
