/*
  ID: nigo1
  LANG: C++
  TASK:
*/
#include <iostream>
#include <stdio.h>

#define pf printf
#define sf scanf
#define TIME pf("%f\n", (double)clock()/CLOCKS_PER_SEC);

using namespace std;

int N, P, Q, q[5], minn;
bool used[100];

void permute (int i, int sum) {
     if (i >= Q) minn = min(minn, sum);
     else {
          for (int j = 0; j < Q; j++)
              if (!used[q[j] - 1]) {
                 used[q[j] - 1] = 1;
                 int t = 0;
                 for (int k = q[j] - 2; k >= 0; k--)
                     if (used[k]) break;
                     else t++;
                 for (int k = q[j]; k < P; k++)
                     if (used[k]) break;
                     else t++;
                 permute (i + 1, sum + t);
                 used[q[j] - 1] = 0;
              }
          }
}
                 
int main()
{
    freopen ("C-small-attempt0.in", "r", stdin);
    freopen ("C-small-attempt0.out", "w", stdout);
    
    sf("%i", &N);
    for (int i = 0; i < N; i++) {
        sf("%i%i", &P, &Q);
        for (int j = 0; j < Q; j++)
            sf("%i", q + j);
        minn = INT_MAX;
        permute(0, 0);
        pf("Case #%i: %i\n", i + 1, minn);
    }    

    sf("%i", &N);
}
