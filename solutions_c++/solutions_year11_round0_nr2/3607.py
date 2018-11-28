#include <cstdio>
#include <cstdlib>
#include <stack>
#include <vector>
#include <map>
using namespace std;

int main(int argc, const char *argv[])
{
  int T;            //Number of cases

  scanf("%d\n", &T);
  for (int i = 0; i < T; i++) {
    int C = 0;      //Num of combine elements
    int D = 0;      //Num of opp elements
    int N = 0;      //Number of series of base elements
    char combine[26][26];
    bool opposite[26][26];
    vector<char> base;

    fprintf(stderr, "===case::%d===\n", i+1);

    for (int j = 0; j < 26; j++) {
      for (int k = 0; k < 26; k++) {
        combine[j][k] = '.';
      }
    }
    for (int j = 0; j < 26; j++) {
      for (int k = 0; k < 26; k++) {
        opposite[j][k] = false;
      }
    }

    scanf("%d ", &C);
    for (int j = 0; j < C; j++) {
      char e[4];
      scanf("%s ", e);
      fprintf(stderr, "com::%s\n", e);
      combine[e[0]-65][e[1]-65] = e[2];
      combine[e[1]-65][e[0]-65] = e[2];
    }
    scanf("%d ", &D);
    for (int j = 0; j < D; j++) {
      char e[3];
      scanf("%s ", e);
      fprintf(stderr, "opp::%s\n", e);
      opposite[e[0]-65][e[1]-65] = true;
      opposite[e[1]-65][e[0]-65] = true;
    }

    scanf("%d ", &N);
    for (int j = 0; j < N; j++) {
      char e;
      scanf("%c", &e);
      if (base.size() > 0) {
        char non_base = combine[e-65][base.back()-65];
        if (non_base != '.') {
          base.pop_back();
          base.push_back(non_base);
        } else {
          base.push_back(e);
          for (vector<char>::reverse_iterator it = base.rbegin(); it < base.rend(); ++it) {
            if (opposite[e-65][*it-65]) {
              base.clear();
              //base.erase(it.base()-1, base.end());
              break;
            }
          }
        }
      } else {
        base.push_back(e);
      }
      fprintf(stderr, "Add::%c\t", e);
      for (vector<char>::iterator it2=base.begin(); it2 < base.end(); ++it2) {
        fprintf(stderr, "%c, ", *it2);
      }
      fprintf(stderr, "\n");
    }


    printf("Case #%d: [", i+1);
    for (vector<char>::iterator it=base.begin(); it < base.end(); ++it) {
      if (it != base.begin()) {
        printf(", ");
      }
      printf("%c", *it);
    }
    printf("]\n");
  }

  return 0;
}
