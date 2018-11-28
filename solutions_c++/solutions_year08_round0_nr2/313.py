#include <cstdio>
#include <utility>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int,int> P;
typedef priority_queue<P, vector<P>, greater<P> > PQ;
#define MP make_pair




P calc(PQ Ago, PQ Bgo, int delta) {
  priority_queue<int,vector<int>,greater<int> > Aready, Bready;
  int a = 0, b = 0;
  for (int t = 0; t < 24*60; ) {
    if (!Ago.empty() && Ago.top().first == t) {
      if (!Aready.empty() && Aready.top() <= t) Aready.pop();       
      else ++a;     
      int end = Ago.top().second + delta;
      Ago.pop();
      Bready.push(end);
    } else if (!Bgo.empty() && Bgo.top().first == t) {
      if (!Bready.empty() && Bready.top() <= t) Bready.pop();
      else ++b;
      int end = Bgo.top().second + delta;
      Bgo.pop();
      Aready.push(end);
    } else ++t;
  }
  return MP(a, b);
}



int main() {
  freopen("B.in", "r", stdin);
  freopen("B.out", "w", stdout);

  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    int delta;
    int na, nb;
    PQ Ago, Bgo;
    scanf("%d", &delta);
    scanf("%d %d", &na, &nb);

    for (int i = 0; i < na; ++i) {
      int h1, m1, h2, m2;
      scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
      Ago.push(MP(h1*60+m1, h2*60+m2));      
    }
    for (int i = 0; i < nb; ++i) {
      int h1, m1, h2, m2;
      scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);      
      Bgo.push(MP(h1*60+m1, h2*60+m2));      
    }   
    
    P ans = calc(Ago, Bgo, delta);    

    printf("Case #%d: %d %d\n", t, ans.first, ans.second);
   

  }

  return 0;
}