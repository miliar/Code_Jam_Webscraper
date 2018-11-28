// qual - 2011, Problem A. Bot Trust
// result:
#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <iostream>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;

//const char input[] = "a-input.txt";  const char output[] = "a-output.txt";
//const char input[] = "A-small-attempt0.in";  const char output[] = "A-small-attempt0.out";
const char input[] = "A-large.in";  const char output[] = "A-large.out";

template <typename T>
static T Abs(T a) {
  return a > 0 ? a : -(a);
}

const bool D = false;
//const bool D = true;

const int N = 200;
int c[N], x[N];
int n;

int other(int cur) { return (cur + 1) % 2; }
int next(int a, int i) {
  ++i;
  while (i < n && c[i] != a) {
    ++i;
  }
  return i;
}

void run(const int t) {
  cin >> n;
  int pos[2] = {1, 1};
  int res = 0;
  assert (n < N);

  for (int i = 0; i < n; ++i) {
    char cc;
    cin >> cc >> x[i];
    c[i] = cc == 'O' ? 0 : 1;
  }

  for (int i = 0; i < n; ++i) {
    int cur = c[i];
    //if (D) cout << pos[cur] << "  " << x[i] << "   " << (pos[cur] != x[i]) << endl;  
    //return;
    while (pos[cur] != x[i]) {
      //cout << "ABC\n";
      if (pos[cur] < x[i]) {
        ++pos[cur];
        ++res;

        if (D) cout << "M1: " << pos[cur] << "->" << x[i] << " " << pos[other(cur)] << " " << res << endl;

        int onext = next(other(cur), i);
        if (onext < n) {
          if (pos[other(cur)] < x[onext])
            ++pos[other(cur)];
          else if (pos[other(cur)] > x[onext])
            --pos[other(cur)];
        }

      } else if (pos[cur] > x[i]) {
        --pos[cur];
        ++res;

        if (D) cout << "M2: " << pos[cur] << "->" << x[i] << " " << pos[other(cur)] << " " << res << endl;

        int onext = next(other(cur), i);
        if (onext < n) {
          if (pos[other(cur)] < x[onext])
            ++pos[other(cur)];
          else if (pos[other(cur)] > x[onext])
            --pos[other(cur)];
        }

      } 
    }



    // now  pos[cur] == x[i]
    ++res;        // we have to push the button
    {             // in meantime, others could move to the target pos...
        int onext = next(other(cur), i);
        if (onext < n) {
          if (pos[other(cur)] < x[onext])
            ++pos[other(cur)];
          else if (pos[other(cur)] > x[onext])
            --pos[other(cur)];
        }
    }

    if (D) cout << "P : " << pos[cur] << "->" << x[i] << " " << pos[other(cur)] << " " << res << endl;

  }

  cout << "Case #" << t << ": " << res << endl;
}

int main() {
  freopen(input, "rt", stdin);
  freopen(output, "wt", stdout);

  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    run(t);
//break;
  }
  return 0;
}



