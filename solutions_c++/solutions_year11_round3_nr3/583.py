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

int N, L, H;
vi freq;

void imprime () {
}

int main () {
  int T;
  scanf("%d", &T);
  
  FOR (t,0,T) {
    scanf ("%d%d%d", &N, &L, &H);
    freq = vi(N);
    FOR(i,0,N)
      scanf("%d", &(freq[i]));
    
    int i;
    for (i = L; i <= H; i++) {
      int j;
      for (j = 0; j < N; j++) {
        if (i%freq[j] != 0 && freq[j]%i != 0)
          break;
      }
      if (j == N) {
        printf ("Case #%d: %d\n", t+1, i);
        break;
      }
    }
    if (i == H+1)
      printf ("Case #%d: NO\n", t+1);
    //imprime ();
  }
  return 0;
}

