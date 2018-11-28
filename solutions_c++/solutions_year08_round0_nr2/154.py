#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

struct event{
  int t;
  int type;
  event(int a, int b){
    t = a;
    type = b;
  }
  bool operator <(const event& other){
    return ((t < other.t) || ((t==other.t) && (type < other.type)));
  }
};

int na, nb, wt;
int aa, ab, ca, cb;

vector<event> V;

int main(){
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  int tnum, tst;
  scanf("%d", &tnum);
  for (tst=1; tst<=tnum; tst++){
    scanf("%d%d%d", &wt, &na, &nb);
    int i;
    ca = cb = aa = ab = 0;
    V.clear();
    for (i=1; i<=na; i++){
      int a, b;
      scanf("%d:%d", &a, &b);
      V.push_back(event(a*60+b, 2));
      scanf("%d:%d", &a, &b);
      V.push_back(event(a*60+b+wt, 3));
    }
    for (i=1; i<=nb; i++){
      int a, b;
      scanf("%d:%d", &a, &b);
      V.push_back(event(a*60+b, 4));
      scanf("%d:%d", &a, &b);
      V.push_back(event(a*60+b+wt, 1));
    }
    sort(V.begin(), V.end());
    for (i=0; i<(int)V.size(); i++){
      event e = V[i];
      if (e.type == 1) ca++;
      if (e.type == 3) cb++;
      if (e.type == 2){
        if (!ca) aa++;
        else ca--;
      }
      if (e.type == 4){
        if (!cb) ab++;
        else cb--;
      }
    }
    printf("Case #%d: %d %d\n", tst, aa, ab);
  }
  return 0;
}