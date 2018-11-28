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

int N;
vector<string> table;
vector<double> rpi;

void solve () {
  vi wins = vi(N,0), games = vi(N,0);
  vector<double> wp = vector<double> (N), owp = vector<double> (N), oowp = vector<double> (N);
  rpi = vector<double> (N);
  
  FOR(i,0,N) {
    FOR(j,0,N) {
      if (table[i][j] != '.')
        games[i]++;
      if (table[i][j] == '1')
        wins[i]++;
    }
    wp[i] = (1.0*wins[i])/(1.0*games[i]);
    //printf ("wp[%d] = %f\n", i, wp[i]);
  }
  
  FOR(i,0,N) {
    owp[i] = 0.0;
    FOR(j,0,N) {
      if (table[i][j] == '1') {
        owp[i] += (1.0*wins[j])/(1.0*(games[j] - 1));
        //printf ("%f\n", owp[i]);
      }
      else if (table[i][j] == '0') {
        owp[i] += (1.0*(wins[j] - 1))/(1.0*(games[j] - 1));
        //printf ("%f\n", owp[i]);
      }
    }
    //printf ("%f\n", owp[i]);
    owp[i] /= (1.0*games[i]);
    //printf ("owp[%d] = %f\n", i, owp[i]);
  }
  
  FOR(i,0,N) {
    oowp[i] = 0.0;
    FOR(j,0,N) {
      if (table[i][j] != '.')
        oowp[i] += owp[j];
    }
    oowp[i] /= games[i]*1.0;
    rpi[i] = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
  }
  
}

void imprime () {
  FOR(i,0,N) {
    printf ("%f\n", rpi[i]);
  }
}

int main () {
  int T;
  scanf("%d", &T);
  
  FOR (t,0,T) {
    scanf ("%d", &N);
    table = vector<string> (N);
    
    FOR(i,0,N) {
      char st[200];
      scanf ("%s", st);
      table[i] = string(st);
    }
    
    solve ();
    
    printf ("Case #%d:\n", t+1);
    imprime ();
  }
  return 0;
}

