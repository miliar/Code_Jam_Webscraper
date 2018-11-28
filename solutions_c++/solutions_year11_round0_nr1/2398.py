#include <cstdio>
#include <vector>
#include <map>
using namespace std;

int zzabs(int a) {
  return a < 0 ? -a : a;
}

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int N;
    scanf("%d", &N);
    vector<int> ints(N);
    vector<char> chars(N);
    for(int i = 0; i < N; i++) {
      char aaa[30];
      scanf("%s%d", aaa, &ints[i]);
      chars[i] = aaa[0];
    }

    int orangepos = 1, bluepos = 1;
    int orangetime = 0, bluetime = 0;

    for(int done = 0; done < N; done++) {
//      printf("vykonavam %c %d\n", chars[done], ints[done]);
      if(chars[done] == 'O') {
        orangetime = max(bluetime + 1, orangetime + zzabs(orangepos-ints[done]) + 1);
        orangepos = ints[done];
      }
      else {
        bluetime = max(orangetime + 1, bluetime + zzabs(bluepos-ints[done]) + 1);
        bluepos = ints[done];
      }
//      printf("op %d ot %d bp %d bt %d\n", orangepos, orangetime, bluepos, bluetime);
    }

    printf("Case #%d: %d\n", t, orangetime > bluetime ? orangetime : bluetime);
  }
  return 0;
}

