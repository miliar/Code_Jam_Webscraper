#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof__(V.begin()) it = V.begin(); it != V.end(); ++it)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long LL;

void presult(char x) {
  if (x == 'X') {
    printf("X won\n");
  } else if (x == 'O') {
    printf("O won\n");
  } else if (x == 'D') {
    printf("Draw\n");
  } else if (x == 'G') {
    printf("Game has not completed\n");
  }
}

void testcase() {
  char buf[5][5];
  REP(i,4) scanf("%s", buf[i]);
  bool koniec = true;
  REP(i,4) {
    set<char> znaki;
    REP(j,4) znaki.insert(buf[i][j]);
    if (znaki.count('.')) {
      koniec = false;
      continue;
    }
    znaki.erase('T');
    if (znaki.size() != 1) {
      continue;
    }
    if (znaki.count('X')) {
      presult('X');
    } else {
      presult('O');
    }
    return;
  }

  REP(i,4) {
    set<char> znaki;
    REP(j,4) znaki.insert(buf[j][i]);
    if (znaki.count('.')) {
      koniec = false;
      continue;
    }
    znaki.erase('T');
    if (znaki.size() != 1) {
      continue;
    }
    if (znaki.count('X')) {
      presult('X');
    } else {
      presult('O');
    }
    return;
  }

  REP(i,2) {
    set<char> znaki;
    if (i == 0) {
      znaki.insert(buf[0][0]);
      znaki.insert(buf[1][1]);
      znaki.insert(buf[2][2]);
      znaki.insert(buf[3][3]);
    } else {
      znaki.insert(buf[0][3]);
      znaki.insert(buf[1][2]);
      znaki.insert(buf[2][1]);
      znaki.insert(buf[3][0]);
    }
    if (znaki.count('.')) {
      koniec = false;
      continue;
    }
    znaki.erase('T');
    if (znaki.size() != 1) {
      continue;
    }
    if (znaki.count('X')) {
      presult('X');
    } else {
      presult('O');
    }
    return;
  }
  if (!koniec) {
    presult('G');
  } else {
    presult('D');
  }
  
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(i,1,t) {
    printf("Case #%d: ", i);
    testcase();
  }
}
