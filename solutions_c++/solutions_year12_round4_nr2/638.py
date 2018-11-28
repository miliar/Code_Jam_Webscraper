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

struct Box {
  int x, y, r;
  Box(int _x, int _y, int _r)
    :x(_x), y(_y), r(_r) {}
};
typedef vector<Box> VBOX;
typedef pair<int, int> PII;

int N, W, H;
VBOX placed;
VI arms;

bool intersect(int x1, int y1, int r1, int x2, int y2, int r2) {
  int rr = r1+r2;
  int xdiff = abs(x1-x2);
  int ydiff = abs(y1-y2);
  // printf("INTERSECT %d %d %d\n", xdiff, ydiff, rr);
  if (xdiff<rr&&ydiff<rr) return true;
  return false;
}

void solve(int caseNum) {
  arms.clear();
  placed.clear();

  cin>>N>>W>>H;
  REP(i, 0, N) {
    int arm; cin>>arm;
    arms.push_back(arm);
    // cout<<arm<<endl;
  }

  REP(i, 0, N) {
    // printf("%d...\n", i);
    int r = arms[i];
    int x = rand() % (W+1);
    int y = rand() % (H+1);
    Box box(x, y, r);
    bool ok = true;
    REP(j, 0, placed.size()) {
      const Box& oth = placed[j];
      if (intersect(box.x, box.y, box.r, oth.x, oth.y, oth.r)) {
        // printf("%d, %d, %d, %d, %d, %d\n", box.x, box.y, box.r, oth.x, oth.y, oth.r);
        ok = false;
        break;
      }
    }
    if (!ok) {
      --i; continue;
    } else {
      placed.push_back(box);
    }
    // printf("%d, %d\n", x, y);
  }

  printf("Case #%d: ", caseNum);
  REP(i, 0, placed.size()) {
    const Box& box = placed[i];
    printf("%d %d", box.x, box.y);
    if (i!=placed.size()-1) printf(" ");
  }
  printf("\n");
}

int main() {
  srand(time(NULL));
  unittest();

  int caseCount;
  cin>>caseCount;
  REP(i, 1, caseCount+1)
    solve(i);

  return 0;
}

void unittest() {
}

