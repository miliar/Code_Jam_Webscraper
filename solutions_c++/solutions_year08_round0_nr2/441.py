#include <iostream>
#include <string>
#include <stdio.h>
#include <vector>
#include <queue>
#include <set>
using namespace std;

struct TRAIN {
  int arrive;
  int start;
  bool astart;
  bool operator < (const TRAIN &a) const {
    if (arrive == a.arrive) {
      return start > a.start;
    }
    return arrive < a.arrive;
  }
};

int main() {
  int N;
  scanf("%d", &N);
  for (int iii = 0; iii < N; iii++) {
    int T;
    scanf("%d", &T);
    int NA, NB;
    scanf("%d %d", &NA, &NB);
    TRAIN a[NA+NB];
    for (int i = 0; i < NA + NB; i++) {
      int h, m;
      scanf("%02d:%02d", &h, &m);
      a[i].start = h * 60 + m;
      scanf("%02d:%02d", &h, &m);
      a[i].arrive = h * 60 + m;
      a[i].astart = i < NA;
    }
    sort(a, a + NA + NB);
    int ans_a = 0, ans_b = 0;

    //printf("Case %d\n", iii+1);
    multiset<int, greater<int> > aq, bq;
    for (int i = 0; i < NA + NB; i++) {
      //printf("%d\n", a[i].arrive);
      if (a[i].astart) {
        if (!aq.empty()){
          bool b = false;
          for (set<int>::iterator it = aq.begin(); it != aq.end(); it++) {
            if (*it <= a[i].start) {
              aq.erase(it);
              b = true;
              break;
            }
          }
          if (!b)
            ans_a++;
        } else {
          ans_a++;
        } 
        bq.insert(a[i].arrive + T);
        //printf("%d\n", a[i].arrive + T);
      } else {
        if (!bq.empty()){
          bool b = false;
          for (set<int>::iterator it = bq.begin(); it != bq.end(); it++) {
            if (*it <= a[i].start) {
              bq.erase(it);
              b = true;
              break;
            }
          }
          if (!b)
            ans_b++;
        } else {
          ans_b++;
        } 
        aq.insert(a[i].arrive + T);
        //printf("%d\n", a[i].arrive + T);
      }
    }
    printf("Case #%d: %d %d\n", iii+1, ans_a, ans_b);
  }
}
