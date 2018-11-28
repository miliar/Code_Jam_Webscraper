#include <stdio.h>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

struct v {
  int d, l;
  bool operator<(const struct v& o) const {
    return d < o.d;
  }
};

int N, T, D;
struct v s[10000];

int fd, fl;

/*bool solve()
{
  fd = s[0].d;

  sort(s, s+N);

  int j = 1, i = 0;
  int l = fd;

  while( i < N ) {
    int max_d = s[i].d + min(s[i].l, l);
    int next_i = -1;
    int next = -1;
    printf("max_d %d @ (%d, %d), l = %d\n", max_d, s[i].d, s[i].l, l);
    if(max_d >= D) {
      return true;
    }
    for(j = i + 1; j < N; j++) {
      printf("j: %d, d: %d\n", j, s[j].d);
      if(s[j].d <= max_d) {
        int cur_d = s[j].d + min(s[j].d - s[i].d, s[j].l);
        if(next < cur_d) {
          next = cur_d;
          next_i = j;
        }
      } else {
        break;
      }
    }
    if(next_i == -1) {
      return false;
    }

    l = min(s[next_i].d - s[i].d, s[next_i].l);
    i = next_i;
  }
  return i == N;
}*/


bool solve()
{
  int max_l[10000];
  memset(max_l, -1, sizeof(max_l));
  max_l[0] = s[0].d;

  for(int i = 0; i < N; i++)
  {
    if(max_l[i] == -1) {
      return false;
    }
    max_l[i] = min(s[i].l, max_l[i]);
    int max_d = s[i].d + max_l[i];
    //printf("(%d, %d): maxd %d, maxl %d\n", s[i].d, s[i].l, max_d, max_l[i]);
    if(max_d >= D) {
      return true;
    }

    for(int j = i+1; j < N; j++) {
      if(s[j].d <= max_d) {
        max_l[j] = max(max_l[j], s[j].d - s[i].d);
      } else {
        break;
      }
    }

  }
  return false;
}



int main()
{
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
      scanf("%d%d", &s[i].d, &s[i].l);
    }
    scanf("%d", &D);
    printf("Case #%d: %s\n", t, solve() ? "YES" : "NO");
  }

  return 0;
}

