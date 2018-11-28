#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef pair<char, int> Pair;

int main() {
  setvbuf(stdin, NULL, _IOFBF, 10000);
  setvbuf(stdout, NULL, _IOFBF, 10000);

  int n_cases;
  scanf("%d", &n_cases);

  //  int o[100];
  //int b[100];
  Pair arr[100];
  for (int ctr = 0; ctr < n_cases; ++ctr) {
    int n;
    scanf("%d", &n);


    for (int i = 0; i < n; ++i) {
      char str[8];
      int x;
      
      scanf("%s", str);
      scanf("%d", &x);
      arr[i].first = str[0];
      arr[i].second = x;
    }

    int time = 0;
    int o_pos = 1;
    int b_pos = 1;
    int o_time = 0;
    int b_time = 0;

    char curr_bot = 'Y';
    int curr_seq = 0;
    for (int i = 0; i < n; ++i) {
      char bot = arr[i].first;
      int q = arr[i].second;

      int inc;
      if (bot != curr_bot) {
        // Settle
        int tmp = curr_seq;
        curr_seq = 0;
        if (bot == 'O') {
          inc = max(abs(q - o_pos) - tmp, 0) + 1;
          curr_seq += inc;
          time += inc;
          o_pos = q;
        } else {
          inc = max(abs(q - b_pos) - tmp, 0) + 1;
          curr_seq += inc;
          time += inc;
          b_pos = q;
        }
      } else {
        if (bot == 'O') {
           inc = abs(q - o_pos) + 1;
          time += inc;
          curr_seq += inc;
          o_pos = q;
        } else {
           inc = abs(q - b_pos) + 1;
          time += inc;
          curr_seq += inc;
          b_pos = q;
        }
      }
      curr_bot = bot;
    }
    printf("Case #%d: %d\n", ctr+1, time);
  }
  
  return 0;
}
