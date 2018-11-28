#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

int main()
{
      map < string, bool > dict;
      int T, N, M;

      scanf("%d", &T);
      for (int i = 1; i <= T; i++) {
            scanf("%d %d", &N, &M);

            string act;
            for (int j = 1; j <= N; j++) {
                  cin >> act;
                  int k = 1;
                  string new_word = "";
                  while (k < act.size()) {
                        while (act[k] != '/' && k < act.size()) {
                              new_word.insert(new_word.end(), act[k]);
                              k++;
                        }
                        k++;
                        dict[new_word] = 1;
                 //       cout << "new_word: " << new_word << endl;
                  }
            }

            int result = 0;
            for (int j = 1; j <= M; j++) {
                  cin >> act;
                  int k = 1;
                  string new_word = "";
                  while (k < act.size()) {
                        while (act[k] != '/' && k < act.size()) {
                              new_word.insert(new_word.end(), act[k]);
                              k++;
                        }
                        k++;
                        if (dict[new_word] != 1) {
                              result++;
                              dict[new_word] = 1;
                        }
//                        cout << "missed_word: " << new_word << endl;
                  }
            }
            printf ("Case #%d: %d\n", i, result);

            dict.clear();
      }

      return 0;
}
