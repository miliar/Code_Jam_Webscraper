#include <vector>
#include <stdio.h>
#include <string.h>

using namespace std;

int T;
int combine[130][130];
int oppose[130][130];
int N;
char c[110];
 
int main() {
  scanf("%d", &T);
  for (int TT=1;TT<=T;++TT) {
    memset(combine, 0, sizeof combine);
    memset(oppose, 0, sizeof oppose);
    memset(c, 0, sizeof c);
    int C;
    scanf("%d ", &C);
    for (int i=0;i<C;++i) {
      scanf("%s", c);
      combine[c[0]][c[1]] = c[2];
      combine[c[1]][c[0]] = c[2]; 
    }
    int D;
    scanf("%d ", &D);
    for (int i=0;i<D;++i) {
      scanf("%s", c);
      oppose[c[0]][c[1]] = 1;
      oppose[c[1]][c[0]] = 1;
    }
    scanf("%d ", &N);
    scanf("%s", c);
    vector<int> V;
    for (int i=0;i<N;++i) {
      if (V.empty()) {
	V.push_back(c[i]);
      } else {
	char last = V[V.size()-1];
	if (combine[last][c[i]]) {
	  V.pop_back();
	  V.push_back(combine[last][c[i]]);
	} else {
	  bool cleared = false;
	  for (int j = 0;j<V.size();++j)
	    if (oppose[V[j]][c[i]]) {
	      V.clear();
	      cleared = true;
	      break;
	    }
	  if (!cleared) {
	    V.push_back(c[i]);
	  }
	}
      }
    }
    printf("Case #%d: [", TT);
    if (V.size())
      printf("%c", V[0]);
    for (int i=1;i<V.size();++i)
      printf(", %c", V[i]);
    printf("]\n");
  }
  return 0;
}
