#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

bool comp(const pair < int, int > &a, const pair < int, int > &b) {
      if (a.first == b.first) {
            return a.second < b.second;
      } else {
            return a.first < b.first;
      }
}

int main()
{
      int N, T;
      pair < int, int > tab[1005];

      scanf("%d", &T);
      for (int i = 1; i <= T; i++) {
            scanf("%d", &N);
            for (int j = 0; j < N; j++) {
                  scanf("%d %d", &tab[j].first, &tab[j].second);
            }

            sort(tab, tab + N, comp);
            int result = 0;
            for (int j = 0; j < N; j++) {
                  for (int k = j + 1; k < N; k++) {
                        if (tab[j].first < tab[k].first && tab[j].second > tab[k].second) {
//                              cout << tab[j].first << " " << tab[j].second << "       " << tab[k].first << " " << tab[k].second << endl;
                              result++;
                        }
                  }
            }
            printf("Case #%d: %d\n", i, result);
      }

      return 0;
}
