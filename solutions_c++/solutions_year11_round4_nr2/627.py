#include <stdio.h>
#include <algorithm>
#define FOR(q,n) for(int q=0; q<n; q++)

#define MAX 600
int data[MAX][MAX];
long long int psum[MAX][MAX];
int r,c,d;
    
long long mx;
long long my;
long long m;

void add_mass(int cx, int cy, int x, int y) {
  mx += (x - cx) * data[x][y];
  my += (y - cy) * data[x][y];
  m += data[x][y];
}

void remove_mass(int cx, int cy, int x, int y) {
  mx -= (x - cx) * data[x][y];
  my -= (y - cy) * data[x][y];
  m -= data[x][y];
}


void solve() {
  scanf("%d %d %d", &r, &c, &d);
  //r = 500;
  //c = 500;
  //d = 1;
  FOR(q, r)  {
    FOR(w, c) {
      scanf("%1d", &data[q][w]);
      //data[q][w] = 0;
      data[q][w] += d;
    }
  }


  int best = 0;
  FOR(q, r) {
    FOR(w, c) {
      mx=my=m=0;

      for (int size = 2; ; size++) {
        if (size + q >= r) break;
        if (size + w >= c) break;
      
        add_mass(q, w, q, w);
        add_mass(q, w, q+size-1, w);
        add_mass(q, w, q, w+size-1);
        add_mass(q, w, q+size-1, w+size-1);

        for (int i = 0; i < size; i++) {
          add_mass(q, w, q+i, w+size);
          add_mass(q, w, q+size, w+i);
        }

        remove_mass(q, w, q, w);
        remove_mass(q, w, q+size, w);
        remove_mass(q, w, q, w+size);
         
        /*
        printf("%d %d %d %d %d %d\n",
              q, w, size, (int) m, (int) mx, (int) my);
              */

        if (size % 2 == 1 ) {
          // parna sirka
          int sh = size / 2;
          if (m % 2 == 0) {
          if (m * sh + m / 2 == mx && m * sh + m / 2 == my) {
            best = std::max(best, size + 1);
          }

          }
        } else {
          int sh = size / 2;
          if (m * sh == mx && m * sh == my) {
//            printf("%d %d %d\n", q, w, size);
//            printf("- %d %d %d\n", (int) m, (int) mx, (int) my);
            best = std::max(best, size + 1);
          }
        }
      }
    }
  }

  if (best < 3) {
    printf("IMPOSSIBLE\n");
  } else {
    printf("%d\n", best);
  }
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(q, t) {
    printf("Case #%d: ", q+1);
    solve();
  }

}
