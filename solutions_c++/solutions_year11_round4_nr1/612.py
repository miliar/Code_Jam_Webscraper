
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

struct Walkway {
  int begin;
  int end;
  int speed;
  bool operator<(const Walkway& other) const {
    if (speed != other.speed) return speed < other.speed;
    return (end-begin) < (other.end - other.begin);
  }
};

int main() {
  setvbuf(stdin, NULL, _IOFBF, 10000);
  setvbuf(stdout, NULL, _IOFBF, 10000);

  Walkway walk[1024];
  int n_cases;
  scanf("%d", &n_cases);
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int x;
    int s;
    int r;
    long double t;
    int n;
    scanf("%d %d %d %Lf %d", &x, &s, &r, &t, &n);
    int total = 0;
    long double take = 0;
    for (int i = 0; i < n; ++i) {
      scanf("%d %d %d", &walk[i].begin, &walk[i].end, &walk[i].speed);
      int dx = (walk[i].end - walk[i].begin);
      total += dx;
    }
    sort(walk, walk+n);
    long double left = x - total;
    long double time = left/(long double)(r);
    if (t < time) {
      take += t;
      take += (left - t*(r))/(long double)(s);
      t = 0;
    } else {
      t -= time;
      take += time;
    }
    for (int i = 0; i < n; ++i){
      int dx = (walk[i].end - walk[i].begin);
      long double time = dx/(long double)(r + walk[i].speed);
      if (t < time) {
        take += t;
        take += (dx - t*(r + walk[i].speed))/(long double)(s + walk[i].speed);
        t = 0;
      } else {
        t -= time;
        take += time;
      }
    }
    printf("Case #%d: %.7Lf\n", ctr+1, take);
  }
  
  return 0;
}
