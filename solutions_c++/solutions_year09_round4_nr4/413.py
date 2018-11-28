#include <stdio.h>
#include <math.h>

int x[40], y[40], r[40];

double dist(int a, int b) {
  double ret = sqrt((x[a]-x[b])*(x[a]-x[b])+(y[a]-y[b])*(y[a]-y[b]));
  ret += (double)r[a] + (double)(r[b]);
  return ret / 2.0;
}


int main(void) {
  int cC, nC;

  scanf("%d", &nC);
  for (cC = 0; cC < nC; cC++) {
    int num_plants;

    scanf("%d", &num_plants);
    for (int i = 0; i < num_plants; i++)
      scanf("%d%d%d", &x[i], &y[i], &r[i]);

    double answer;
    if (num_plants == 3) {
      double min_dist = dist(0, 1);
      double other_rad = r[2];

      answer = (min_dist > other_rad) ? min_dist : other_rad;

      if (min_dist > dist(0, 2)) {
        min_dist = dist(0, 2);
        other_rad = r[1];
        double t_answer = (min_dist > other_rad) ? min_dist : other_rad;
        if (t_answer < answer) answer = t_answer;
      }
      if (min_dist > dist(1, 2)) {
        min_dist = dist(1, 2);
        other_rad = r[0];
        double t_answer = (min_dist > other_rad) ? min_dist : other_rad;
        if (t_answer < answer) answer = t_answer;
      }
    } else if (num_plants == 1) {
      answer = r[0];
    } else {
      answer = (r[0] > r[1]) ? r[0] : r[1];
    }
    printf("Case #%d: %.6f\n", cC + 1, answer);
  }
  return 0;
}
