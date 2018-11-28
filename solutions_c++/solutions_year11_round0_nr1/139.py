#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long int int64;
typedef vector<int> VI;
#define REP(i,a,b) for (int i=int(a); i<int(b); ++i)
void unittest();

int N;
bool sBlue[100];
int sPos[100];
int sCur;

int rGoal[2];
int rPos[2];

void scanGoal() {
  REP(r, 0, 2) {
    rGoal[r] = rPos[r]; // default = current pos
    REP(i, sCur, N) {
      if ((sBlue[i]?1:0)==r) {
        rGoal[r] = sPos[i];
        // printf("!!scanGoal %d %d: %d %d\n", sCur, int(r), i, rGoal[r]);
        break;
      }
    }
    // printf("scanGoal %d %d: %d\n", sCur, int(r), rGoal[r]);
  }
}

void solve(int caseNum) {
  cin>>N;
  REP(i, 0, N) {
    string color;
    int pos;
    cin>>color>>pos;
    if (color=="B") {
      sBlue[i] = true;
    } else {
      assert(color=="O");
      sBlue[i] = false;
    }
    sPos[i] = pos;
  }
  rPos[0] = rPos[1] = 1;

  sCur=0;
  scanGoal();
  int round = 0;

  while(sCur<N) {
    ++round;
    bool pushed = false;
    // printf("Round=%d, sCur=%d, pos=%d, %d\n", round, sCur, rPos[0], rPos[1]);
    REP(r, 0, 2) {
      int& myPos = rPos[r];
      if (!pushed && (sBlue[sCur]?1:0)==r && sPos[sCur]==myPos) {
        // printf("Push %d at %d by %d\n", sCur, myPos, r);
        pushed = true;
        ++sCur;
        scanGoal();
        continue;
      }
      if (myPos>rGoal[r])
        --myPos;
      else if (myPos<rGoal[r])
        ++myPos;
    }
  }

  printf("Case #%i: ", caseNum);
  printf("%i", round);
  printf("\n");
}

int main() {
  unittest();

  int caseCount;
  cin>>caseCount;
  REP(i, 1, caseCount+1)
    solve(i);

  return 0;
}

void unittest() {
  assert(true);
}

