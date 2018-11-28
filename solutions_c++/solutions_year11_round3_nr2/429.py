#include <stdio.h>

int L,t,N,C;
int D;
int nums[1001];
int sums[1001];

int main() {
  int T;
  scanf("%d", &T);
  for (int TT=1;TT<=T;++TT) {
    scanf("%d %d %d %d", &L, &t, &N, &C);
    for (int i=0;i<C;++i) {
      int d;
      scanf("%d", &d);
      int cur = i;
      while (cur<N) {
	nums[cur] = d;
	cur += C;
      }
    }
    sums[0] = nums[0];
    for (int i=0;i<N;++i)
      sums[i] = sums[i-1]+nums[i];
    double best = 2*sums[N-1];
    if (L == 2) {
    for (int f=0;f<N;++f)
      for (int s=f+1;s<N;++s) {
	double t1 = 0;
	if (f>0) t1 = 2*sums[f-1];
	if (t1 > t) {
	  t1 = 2*sums[N-1]-nums[f]-nums[s];
	  if (t1 < best) {
	    best = t1;
	  }
	  continue;
	}
	if (t1 + 2*nums[f] > t) {
	  t1 = t+nums[f]-(t-t1)/2;
	  t1 += 2*(sums[N-1]-sums[f])-nums[s];
	  if (t1 < best) {
	    best = t1;
	  }
	  continue;
	}
	if (t1 + 2*nums[f] <= t) {
	  t1 = 2*sums[s-1];
	  if (t1 > t) {
	    t1 = 2*sums[N-1]-nums[s];
	    if (t1 < best) {
	      best = t1;
	      
	    }
	    continue;
	  }
	  if (t1 + 2*nums[s] <= t) {
	    t1 = 2*sums[N-1];
	    if (t1 < best) {
	      best = t1;
	    }
	    continue;
	  }
	  t1 = t+nums[s]-(t-t1)/2;
	  t1 += 2*(sums[N-1]-sums[s]);
	  if (t1 < best) {
	    best = t1;
	  }
	  continue;
	}
      }
    } else if (L == 1) {
      for (int f=0;f<N;++f) {
	double t1 = 0;
	if (f>0) t1 = 2*sums[f-1];
	if (t1 > t) {
	  t1 = 2*sums[N-1]-nums[f];
	  if (t1 < best) {
	    best = t1;
	  }
	  continue;
	}
	if (t1 + 2*nums[f] > t) {
	  t1 = t+nums[f]-(t-t1)/2;
	  t1 += 2*(sums[N-1]-sums[f]);
	  if (t1 < best) {
	    best = t1;
	  }
	  continue;
	}
	if (t1 + 2*nums[f] <= t) {
	  t1 = 2*sums[N-1];
	  if (t1 < best) {
	    best = t1;
	    }
	  continue;
	}
      }
    }
    printf("Case #%d: %d\n", TT, (int)best);
  }
  return 0;
}
