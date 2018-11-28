#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

char combine[130][130];
bool oppose[130][130];


int main(void) {
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);


  int nCase;
  scanf("%d", &nCase);

  for (int c = 1; c <= nCase; ++c) {
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

    char input[105];

    int n;
    scanf("%d %s", &n, input);
    vector<char> curr;
    for (int i = 0; input[i]; ++i) {
      if (!curr.empty()) {
        char p = curr.back();

        if (combine[p][input[i]] != 0) {
          curr.pop_back();
          curr.push_back(combine[p][input[i]]);
        } else {
          for (int j = 0; j < curr.size(); ++j) {
            if (oppose[curr[j]][input[i]]) {
              curr.clear();
              break;
            }
          }

          if (!curr.empty()) {
            curr.push_back(input[i]);
          }
        }
      } else {
        curr.push_back(input[i]);
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