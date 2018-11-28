#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#define vi vector<int>
#define ll long long
#define SZ(A) (int)(A).size()
#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)
#define pb push_back

using namespace std;

int L, t, N, C;
vi a, dist;

void imprime () {
}

int main () {
  int T;
  scanf("%d", &T);
  
  FOR (u,0,T) {
    scanf ("%d%d%d%d", &L, &t, &N, &C);
    a = vi(C);
    FOR(i,0,C)
      scanf ("%d", &(a[i]));
    dist = vi(N);
    for (int k = 0; k*C < N;k++) {
      for (int i = 0; i < C; i++)
        dist[k*C+i] = a[i];
    }
    
    if (L == 0) {
      int sum = 0;
      FOR(i,0,N)
        sum += dist[i]*2;
      printf ("Case #%d: %d\n", u+1, sum);
    }
    else if (L == 1) {
      int minSum = 2000000000;
      FOR(l,0,N) {
        double sum = 0.0;
        FOR(i,0,N) {
          if (l == i) {
            if (sum >= t)
              sum += dist[i];
            else if (sum < t && sum + dist[i] < t)
              sum += dist[i]*2;
            else
              sum += dist[i] + (t-sum)/2.0;
          }
          else
            sum += 2*dist[i];
        }
        if (sum < minSum)
          minSum = (int) sum;
      }
      printf ("Case #%d: %d\n", u+1, minSum);
    }
    else if (L == 2) {
      int minSum = 2000000000;
      FOR(l1,0,N) {
        FOR(l2,0,N) {
          double sum = 0;
          FOR(i,0,N) {
            if (l1 == i || l2 == i) {
              if (sum >= t)
                sum += dist[i];
              else if (sum < t && sum + dist[i] < t)
                sum += dist[i]*2;
              else
                sum += dist[i] + (t-sum)/2.0;
            }
            else
              sum += 2*dist[i];
          }
          if (sum < minSum)
            minSum = (int) sum;
        }
      }
      printf ("Case #%d: %d\n", u+1, minSum);
    }
    
    //FOR(i,0,N)
    //  printf ("%d ", dist[i]);
    //printf ("\n");
    //printf ("Case #%d: \n", u+1);
    imprime ();
  }
  return 0;
}

