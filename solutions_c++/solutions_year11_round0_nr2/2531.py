#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

char combine[200][200];
bool oppose[200][200];


int main(void) {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);


  int ncase;
  scanf("%d", &ncase);

  for (int c = 1; c <= ncase; ++c) {
    int nc, nd;

    memset(combine, 0, sizeof(combine));
    memset(oppose, 0, sizeof(oppose));


    char combstr[5];
    scanf("%d", &nc);
    while (nc--) {
      scanf(" %s", combstr);

      combine[combstr[0]][combstr[1]] = combstr[2];
      combine[combstr[1]][combstr[0]] = combstr[2];
    }

    char oppstr[5];
    scanf("%d", &nd);
    while (nd--) {
      scanf(" %s", oppstr);

      oppose[oppstr[0]][oppstr[1]] = true;
      oppose[oppstr[1]][oppstr[0]] = true;
    }

    char in[105];

    int n;
    scanf("%d %s", &n, in);
    vector<char> curr;
    for (int i = 0; in[i]; ++i) {
      // combine
      if (!curr.empty()) {
        char p = curr.back();

        if (combine[p][in[i]] != 0) {
          curr.pop_back();
          curr.push_back(combine[p][in[i]]);
        } else {
          for (int j = 0; j < curr.size(); ++j) {
            if (oppose[curr[j]][in[i]]) {
              curr.clear();
              break;
            }
          }

          if (!curr.empty()) {
            curr.push_back(in[i]);
          }
        }
      } else {
        curr.push_back(in[i]);
      }
    }

    printf("Case #%d: [", c);
    for (int i = 0; i < curr.size(); ++i) {
      if (i)
        printf(", ");

      printf("%c", curr.at(i));
    }
    printf("]\n");
  }

}