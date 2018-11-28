#include <stdio.h>
#include <stdlib.h>

const int MAXN = 20000;

struct walkway {
  int s,t;
  int speed;
  int len;
} walkways[MAXN];


int walkway_cmp(const void *p1, const void *p2) {
  const walkway *a = (const walkway*)p1;
  const walkway *b = (const walkway*)p2;
  return (a->speed) - (b->speed);
}


int main() {

  int Tcases;
  scanf("%d", &Tcases);

  for(int casen = 0; casen < Tcases; ++casen) {
    int len, n;
    double t, walk, run;
    scanf("%d %lf %lf %lf %d", &len, &walk, &run, &t, &n);
    int ydist = 0;
    for(int i = 0; i < n; ++i) {
      scanf("%d %d %d", &walkways[i].s, &walkways[i].t, &walkways[i].speed);
      walkways[i].len = walkways[i].t - walkways[i].s;
      ydist += walkways[i].len;
    }
    qsort(walkways, n, sizeof(walkway), walkway_cmp);

    double time = 0;
    
    if(len - ydist >= t * run) {
      //printf("running on floor for all time %lf\n", t);
      time += t + (len - ydist - t * run) / walk;
      t = 0;
    } else {
      double x = (len - ydist) / run;
      t -= x;
      time += x;
      //printf("running on floor for time %lf\n", x);
    }
    for(int i = 0; i < n; ++i) {
      int s = walkways[i].speed;
      if(walkways[i].len >= t * (run + s)) {
	double x = t + (walkways[i].len - t * (run + s)) / (walk + s);
	time += x;
	t = 0;
	//printf("running on walkway %d(%d,%d,~%d) for time %lf and walking the rest for time %lf\n", i, walkways[i].s, walkways[i].t, walkways[i].speed, t, x-t);
      } else {
	double x = walkways[i].len / (run + s);
	t -= x;
	time += x;
	//printf("running on walkway %d(%d,%d,~%d) for time %lf\n", i, walkways[i].s, walkways[i].t, walkways[i].speed, x);
      }
    }

    printf("Case #%d: %.09lf\n", 1+casen, time);
  }

}
