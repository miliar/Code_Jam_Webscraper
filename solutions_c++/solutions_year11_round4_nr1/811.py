#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_N = 1000;

struct Walkway {
  int len;
  int speed;

  bool operator < (const Walkway& other) const
  {
    return speed < other.speed;
  }
};

int X, S, R, t, N;
Walkway ww[MAX_N + 1];

inline void
read_input()
{
  scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);

  for (int i = 0; i < N; ++i) {
    int b, e;
    scanf("%d %d %d", &b, &e, &ww[i].speed);

    ww[i].len = e - b;
  }
}

inline void
solve()
{
  double time = 0.;
  double run_time_left = (double)t;
  
  int normal_walk = X;
  
  for (int i = 0; i < N; ++i)
    normal_walk -= ww[i].len;
  
  ww[N].len = normal_walk;
  ww[N].speed = 0;

  sort(ww, ww + N + 1);

  for (int i = 0; i <= N; ++i) {
    double cur_len_run = min(run_time_left * (double)(R + ww[i].speed), (double)ww[i].len);
    double time_run = cur_len_run / (double)(R + ww[i].speed);
    time += time_run;
    time += ((double)(ww[i].len) - cur_len_run) / (double)(S + ww[i].speed);

    run_time_left -= time_run;
  }

  printf("%.08lf\n", time);
}

int
main()
{
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    printf("Case #%d: ", t);
    read_input();
    solve();
  }

  return (0);
}
