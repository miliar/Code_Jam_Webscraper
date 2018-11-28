#include <iostream>
using namespace std;

int testcase;
long long Pg, Pd, N;

int gcd(int x, int y) {
  while (y != 0) {
    int temp = x%y;
    x = y;
    y = temp;
  }
  return x;
}

int main(int argc, char *argv[]) {
  cin >> testcase;
  for (int tn = 1; tn <= testcase; ++tn) {
    cin >> N >> Pd >> Pg;
    int flag = 0;
    if (Pd == 0 && Pg == 0)      flag = 2;
    else if(Pg == 0) {
      flag = 0;
    }
    else if(Pd == 0) {
      if (Pg != 100)
        flag = 2;
      else flag = 0;
    }
    else {
      long long Qd = 100 / gcd(100, Pd);
      long long Qg = 100 / gcd(100, Pg);
      if ((Qd <= N && Pg != 100) || Pd == 100){
        flag = 2;
      } else flag = 0;
      // for (int i = Qd; i <= N; i += Qd) {
      //   int step = 1;
      //   for (int j = i; ; j += step) {
      //     if (j%Qg == 0) step = Qg;
      //     else {
      //       continue;
      //     }
      //     if (j - j * Pg / 100 >= i - i * Pd / 100) {
      //       cout << "Case #" << tn << ": Possible" << endl;
      //       flag = 1;
      //       break;
      //     } else
      //       break;
      //   }
      //   if (flag == 1)
      //     break;
      // }
    }
    if (flag == 0)
      cout << "Case #" << tn << ": Broken" << endl;
    else if(flag == 2)
      cout << "Case #" << tn << ": Possible" << endl;
  }
  return 0;
}
