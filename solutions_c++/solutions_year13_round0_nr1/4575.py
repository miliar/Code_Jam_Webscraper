#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <cstring>
#include <set>
#include <cmath>

using namespace std;
typedef pair <int, int> P;
const int MAXN = 1000000;
const int O = 0;
const int X = 1;
const int DOT = 2;
const int T = 3;

int t;
char m[5][5];
int opts[20][4];

void update(int act, int x, int y);
void clean(int act);

int main() {
  scanf("%d", &t);
  int num = 0;
  while(t--) {
      ++num;
      for(int i = 1; i <= 4; ++i) {
	  scanf("%s", m[i]);
      }
      int act = 0;
      for(int i = 1; i <= 4; ++i) {
	  clean(act);  
	  for(int j = 1; j <= 4; ++j) {
	      update(act, i, j);
	  }
	  ++act;
      }
      for(int j = 1; j <= 4; ++j) {
	  clean(act);
	  for(int i = 1; i <= 4; ++i) {
	      update(act, i, j);
	  }
	  ++act;
      }
      clean(act), clean(act + 1);
      for(int i = 1; i <= 4; ++i) {
	  update(act, i, i);
	  update(act + 1, i, 5 - i);
      }
      act += 2;
      bool full = true;
      bool end = false;
      for(int i = 0; i < act; ++i) {
	  if(opts[i][X] + opts[i][O] + opts[i][T] < 4) {
	    full = false;
	    continue;
	  }
	  if(opts[i][X] + opts[i][T] == 4) {
	      end = true;
	      printf("Case #%d: X won\n", num);
	      break;
	  } else if(opts[i][O] + opts[i][T] == 4) {
	      end = true;
	      printf("Case #%d: O won\n", num);
	      break;
	  }
      }
      if(!end && full) printf("Case #%d: Draw\n", num);
      else if(!end) printf("Case #%d: Game has not completed\n", num);
  }
  return 0;
}

void update(int act, int x, int y) {
    if(m[x][y - 1] == 'X') opts[act][X]++;
    if(m[x][y - 1] == 'O') opts[act][O]++;
    if(m[x][y - 1] == '.') opts[act][DOT]++;
    if(m[x][y - 1] == 'T') opts[act][T]++;
}

void clean(int act) {
    opts[act][O] = opts[act][X] = opts[act][DOT] = opts[act][T] = 0; 
}