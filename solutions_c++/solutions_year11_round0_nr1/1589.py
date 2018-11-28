#include <iostream>
#include <vector>

using namespace std;

/*

3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

*/

int main() {
  int i, n, m, button, seconds, pos_orange, pos_blue, idx_orange, idx_blue;
  string ordem, robot;
  vector<int> orange;
  vector<int> blue;
  i = 1;
  cin >> n;
  while (i <= n) {
    seconds = 0;
    ordem = "";
    blue.clear();
    orange.clear();
    idx_orange = idx_blue = 0;
    pos_orange = pos_blue = 1;
    cin >> m;
    for (int j = 0; j < m; j++) {
      cin >> robot;
      cin >> button;
      robot == "O" ? orange.push_back(button) : blue.push_back(button);
      ordem += robot;
    }
/*
    OBBO
    o -> 24
    b -> 12

    o = 2
    b = 1
    s = 3
    po = 4
    pb = 2
*/
    for (int k = 0; k < ordem.size(); k++) {
      if (ordem[k] == 'O') {
        while (pos_orange != orange[idx_orange]) {
          pos_orange < orange[idx_orange] ? pos_orange++ : pos_orange--;
          if (pos_blue != blue[idx_blue]) 
            pos_blue < blue[idx_blue] ? pos_blue++ : pos_blue--;
          seconds++;
        }
        if (pos_blue != blue[idx_blue]) 
          pos_blue < blue[idx_blue] ? pos_blue++ : pos_blue--;
        seconds++;
        idx_orange += 1;
      }
      else {
        while (pos_blue != blue[idx_blue]) {
          pos_blue < blue[idx_blue] ? pos_blue++ : pos_blue--;
          if (pos_orange != orange[idx_orange])
            pos_orange < orange[idx_orange] ? pos_orange++ : pos_orange--;
          seconds++;
        }
        if (pos_orange != orange[idx_orange])
          pos_orange < orange[idx_orange] ? pos_orange++ : pos_orange--;
        seconds++;
        idx_blue += 1;
      }
    }
    cout << "Case #" << i << ": " << seconds << endl; 
    i++;
  }
}
