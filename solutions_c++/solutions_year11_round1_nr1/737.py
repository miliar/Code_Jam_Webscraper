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

int N, Pd, Pg, res;

using namespace std;

void imprime () {
  if (res == 0)
    printf ("Broken\n");
  else
    printf ("Possible\n");
}

int main () {
  int T;
  scanf("%d", &T);
  
  FOR (t,0,T) {
    res = 0;
    scanf ("%d%d%d", &N, &Pd, &Pg);
    
    if (Pg == 100 && Pd < 100) {
      res = 0;
    }
    else if (Pg == 0 && Pd > 0) {
      res = 0;
    }
    else {
      if (Pd == 100)
        res = 1;
      if (100 <= N)
        res = 1;
      else if ((50*Pd)%100 == 0 && 50 <= N)
        res = 1;
      else if ((25*Pd)%100 == 0 && 25 <= N)
        res = 1;
      else if ((20*Pd)%100 == 0 && 20 <= N)
        res = 1;
      else if ((10*Pd)%100 == 0 && 10 <= N)
        res = 1;
      else if ((5*Pd)%100 == 0 && 5 <= N)
        res = 1;
      else if ((4*Pd)%100 == 0 && 4 <= N)
        res = 1;
      else if ((2*Pd)%100 == 0 && 2 <= N)
        res = 1;
    }
    
    printf ("Case #%d: ", t+1);
    imprime ();
  }
  return 0;
}

