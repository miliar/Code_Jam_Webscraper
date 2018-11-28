#include <iostream>
#include <vector>
#include <algorithm>

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

typedef int64_t num;

struct tuple {
  num radius;
  num index;
  double x;
  double y;
};

struct radius_cmp {
  bool operator()(const tuple& l, const tuple& r) const {
    return l.radius > r.radius;
  }
};

struct index_cmp {
  bool operator()(const tuple& l, const tuple& r) const {
    return l.index < r.index;
  }
};

double gen_rand(double x) {
  int i = rand();
  return x * (((double)i) / (1 + (double)RAND_MAX));
}

int main() {
  int num_cases;
  std::cin >> num_cases;
  for (int casenum = 1; casenum <= num_cases; ++casenum) {
    num n, w, l;
    std::cin >> n >> w >> l;

    std::vector<tuple> r;
    for (num i = 0; i < n; ++i) {
      num ri;
      std::cin >> ri;
      tuple p;
      p.radius = ri;
      p.index = i;
      p.x = -1;
      p.y = -1;
      r.push_back(p);
    }

    std::sort(r.begin(), r.end(), radius_cmp());

    srand(12345);

    if (n >= 1) {
      r[0].x = 0;
      r[0].y = 0;
    }
    if (n >= 2) {
      r[1].x = w;
      r[1].y = l;
    }

    // we have enough space that maybe being random will work

    bool try_successful = false;
    for (int tryy = 0; tryy < 100; ++tryy) {
      bool this_run = true;
      for (num i = 2; i < n; ++i) {
        double x, y;

        bool found = false;
        for (int j = 0; j < 100; ++j) {
          x = gen_rand(w);
          y = gen_rand(l);

          bool good = true;
          for (int k = 0; k < i; ++k) {
            double xd = r[k].x - x;
            double yd = r[k].y - y;
            double dsq = (r[k].radius + r[i].radius);
            if (xd * xd + yd * yd < dsq * dsq) {
              good = false;
              break;
            }
          }

          if (good) {
            found = true;
            break;
          }
        }

        if (!found) {
          this_run = false;
          break;
        }

        r[i].x = x;
        r[i].y = y;
      }

      if (this_run) {
        try_successful = true;
        break;
      }
    }

    if (!try_successful) {
      std::cerr << "FAILURE FAILURE" << std::endl;
      exit(-1);
    }

    std::cout << "Case #" << casenum << ":";

    std::sort(r.begin(), r.end(), index_cmp());

    // check solution

    for (int i = 0; i < n; ++i) {
      if (r[i].x == -1 || r[i].y == -1) {
        std::cerr << "neg\n";
        exit(-1);
      }

      if (r[i].x < 0 || r[i].x > w) {
        std::cerr << "outside width\n";
        exit(-1);
      }

      if (r[i].y < 0 || r[i].y > l) {
        std::cerr << "outside length\n";
        exit(-1);
      }

      for (int j = 0; j < i; ++j) {

        double xd = r[i].x - r[j].x;
        double yd = r[i].y - r[j].y;
        double rd = r[i].radius + r[j].radius;
        if (xd * xd + yd * yd <= rd) {
          std::cerr << "overlaps\n";
          exit(-1);
        }

      }

    }

    for (int i = 0; i < n; ++i) {
      printf(" %.8f %.8f", r[i].x, r[i].y);

    }
    std::cout << std::endl;

  }

}
