#include <iostream>
#include <string>
using namespace std;

int sumsq(int j, int b) {
  int digit;
  int ans = 0;
  while(j > 0) {
    digit = j % b;
    ans += digit*digit;
    j = j / b;
  }
  return ans;
}

int main(int argc, char *argv[]) {
  int T,B;
  int j,jj;
  int bases[9];
  int happy[10000][11];
  char ch;
  bool ok;
  for(int b =2; b <= 10; b++) {
    happy[1][b] = 1;
    for(int i = 2; i<10000; i++) {
      happy[i][b] = 0;
    }
    for(int i = 2; i<10000; i++) {
      j = i;
      while(happy[j][b] == 0) {
        happy[j][b] = -1;
        j = sumsq(j,b);
      }
      if(happy[j][b] == 1) {
        j = i;
        while(happy[j][b] == -1) {
          happy[j][b] = 1;
          j = sumsq(j,b);
        }
      }
    }
  }

  cin >> T >> ws;
  for (int t = 1; t <= T; t++) {
    B = 0;
    while(true) {
      cin >> bases[B];
      B++;
      cin.get(ch);
      if(ch == '\n') {
        cin >> ws;
        break;
      }
    }
    ok = false;
    j = 1;
    while(!ok) {
      j++;
      ok = true;
      for (int b = 0; b < B; b++) {
        if(j >= 10000) {
          jj = sumsq(j, bases[b]);
        } else {
          jj = j;
        }
        if(happy[jj][bases[b]] == -1) {
          ok = false;
          break;
        }
      }
    }
    cout << "Case #" << t << ": " << j << endl;
  }
  return 0;
}

