#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
  int C, N, M;
  scanf("%d", &C);
  vector<vector<int> > adj;
  vector<vector<double> > cap;

  for (int cnum = 1; cnum <= C; cnum++) {
    scanf("%d%d", &M, &N);

    vector<vector<bool> > mlike(N, M), ulike(N, M);
    vector<int> mnum(N, 0), unum(N, 0);
    vector<bool> malt(M, 0);
    vector<bool> good(N, 0);
    
    /** input **/
    for (int i = 0; i < N; i++) {
      int tnlike, flavor, type;
      scanf("%d", &tnlike);
      for (int j = 0; j < tnlike; j++) {
	scanf("%d%d", &flavor, &type);
	if (type == 0) {
	  ulike[i][flavor-1] = true;
	  unum[i]++;
	}
	if (type == 1) {
	  mlike[i][flavor-1] = true;
	  mnum[i]++;
	}
      }
    }

    bool impossible = false;
    bool found = true;
    while(!impossible && found) {
      found = false;
      for (int i = 0; i < N; i++) {
	if (good[i])
	  continue;
	if (unum[i] == 0 && mnum[i] == 0) {
	  impossible = true;
	  break;
	}
	else if (unum[i] == 0) {
	  found = true;
	  for (int j = 0; j < M; j++) {
	    if (mlike[i][j]) {
	      malt[j] = true;
	      for (int k = 0; k < N; k++) {
		if (mlike[k][j]) {
		  good[k] = true;
		}
		if (ulike[k][j]) {
		  unum[k]--;
		}
	      }
	      break;
	    }
	  }
	  break;
	}
      } 
    }

    printf("Case #%d:", cnum);
    if (impossible) {
      printf(" IMPOSSIBLE\n");
    }
    else {
      for (int i = 0; i < M; i++) {
	printf(" %d", malt[i] ? 1 : 0);
      }
      printf("\n");
    }

  }

  return 0;
}
