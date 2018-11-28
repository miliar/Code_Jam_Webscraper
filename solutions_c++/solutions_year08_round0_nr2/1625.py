#include <algorithm>
#include <cstdio>
#include <vector>
#define PB push_back
#define X first
#define Y second
#define PII pair<int, int>

using namespace std;

vector<PII > as;
vector<PII > bs;
vector<int> arrivinga;
vector<int> arrivingb;

struct Comparator {
  bool operator()(const int a, const int b) const {
   return a > b;
  }
};

int main() {
  int n;
  char str[10];

  scanf("%d", &n);
  for (int casei = 0; casei < n; ++casei) {
    int t, na, nb;
    int atrains = 0, btrains = 0;
    int trainsata = 0, trainsatb = 0;
    int apos = 0, bpos = 0; 

    scanf("%d", &t);
    scanf("%d %d", &na, &nb);

    as.clear();
    for (int i = 0; i < na; ++i) {
      int hour, min, stime, etime;
      scanf("%s", str);
      sscanf(str,"%d:%d", &hour, &min);
      stime = hour * 60 + min;
      scanf("%s", str);
      sscanf(str,"%d:%d", &hour, &min);
      etime = hour * 60 + min;
      if (stime > etime)
        etime += 60*24;
      as.PB(make_pair(stime, etime));
    }
    sort(as.begin(), as.end());

    bs.clear();
    for (int i = 0; i < nb; ++i) {
      int hour, min, stime, etime;
      scanf("%s", str);
      sscanf(str,"%d:%d", &hour, &min);
      stime = hour * 60 + min;
      scanf("%s", str);
      sscanf(str,"%d:%d", &hour, &min);
      etime = hour * 60 + min;
      if (stime > etime)
        etime += 60*24;
      bs.PB(make_pair(stime, etime));
    }
    sort(bs.begin(), bs.end());

    arrivinga.clear();
    arrivingb.clear();

    for (int time = 0; time < 60*24; ++time) {
      while (arrivinga.size() > 0 && arrivinga.front() == time) {
        pop_heap(arrivinga.begin(), arrivinga.end(), Comparator());
        arrivinga.pop_back();
        ++trainsata;
      }

      while (arrivingb.size() > 0 && arrivingb.front() == time) {
        pop_heap(arrivingb.begin(), arrivingb.end(), Comparator());
        arrivingb.pop_back();
        ++trainsatb;
      }

      while (apos < as.size() && as[apos].X == time) {
        if (trainsata == 0) 
          atrains += 1;
        else 
          --trainsata;
        
        arrivingb.PB(as[apos].Y + t);
        push_heap(arrivingb.begin(), arrivingb.end(), Comparator());

        ++apos;
      }

      while (bpos < bs.size() && bs[bpos].X == time) {
        if (trainsatb == 0) 
          btrains += 1;
        else
          --trainsatb;
        
        arrivinga.PB(bs[bpos].Y + t);
        push_heap(arrivinga.begin(), arrivinga.end(), Comparator());

        ++bpos;
      }

    }

    printf("Case #%d: %d %d\n", casei+1, atrains, btrains);
  }
  return 0;
}
