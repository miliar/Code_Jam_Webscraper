#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <utility>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <map>
using namespace std;
typedef pair<int,int> pii;
#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
#define FOR(i,c) for (__typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
const int DAY_IN_MINUTES = 24*60;

struct Trip {
  Trip(){}
  Trip(char src, int dt, int at): src(src),dt(dt),at(at){}
  char src;
  int dt, at;
};
bool operator<(const Trip &a, const Trip &b) {
  return a.dt < b.dt;
}

class TimeTable {
public:
  TimeTable():na_(0),nb_(0),trips_(0) {
    memset(ta_, 0, sizeof(ta_));
    memset(tb_, 0, sizeof(tb_));
  }
  void input() {
    int turnaround;
    scanf("%d\n", &turnaround);
    scanf("%d %d\n", &na_, &nb_);
    input_time(na_, 'A', turnaround);
    input_time(nb_, 'B', turnaround);
    sort(trips_.begin(), trips_.end());
  }

  pii calc() {
    int ra=0, rb=0;
    REP(i, trips_.size()) {
      //print_trip(trips_[i]);
      int *tsrc, *tdest;
      char src = trips_[i].src;
      switch (src) {
      case 'A':
        tsrc = ta_; tdest = tb_; break;
      case 'B':
        tsrc = tb_; tdest = ta_; break;
      default:
        assert(false);
      }
      bool flag = false;
      for (int t = trips_[i].dt; t < DAY_IN_MINUTES; ++t) {
        if (--tsrc[t] < 0) flag = true;
      }
      if (flag) {
        if (src == 'A') ++ra; else ++rb;
        //printf("Add %c : %d %d\n", src, ra, rb);
        for (int t = trips_[i].dt; t < DAY_IN_MINUTES; ++t) {
          ++tsrc[t];
        }
      }
      for (int t = trips_[i].at; t < DAY_IN_MINUTES; ++t) {
        ++tdest[t];
      }
    }
    return make_pair(ra, rb);
  }

  void print_trip(const Trip &t) {
    printf("%c # %d:%d -> %d:%d\n", t.src,
           t.dt/60, t.dt%60, t.at/60, t.at%60);
  }
  void print() {
    puts("\nTime Table:");
    REP(i, trips_.size()) {
      print_trip(trips_[i]);
    }
    puts("");
  }
private:
  void input_time(int n, char src, int t) {
    REP(i, n) {
      int dh, dm, ah, am;
      scanf("%d:%d %d:%d\n", &dh, &dm, &ah, &am);
      int dt = dh * 60 + dm;
      int at = ah * 60 + am;
      trips_.push_back(Trip(src, dt, at+t));
    }
  }
  int na_, nb_;
  deque<Trip> trips_;
  int ta_[DAY_IN_MINUTES];
  int tb_[DAY_IN_MINUTES];
};


int main() {
  int n;
  scanf("%d\n", &n);
  for (int t = 1; t <= n; ++t) {
    TimeTable tt;
    tt.input();
    pii r = tt.calc();
    printf("Case #%d: %d %d\n", t, r.first, r.second);
  }
}
