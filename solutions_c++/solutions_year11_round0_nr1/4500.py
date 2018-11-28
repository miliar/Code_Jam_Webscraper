#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

int
main(int agrc, char *argv[]) {
  int num;
  char r;
  int b;
  int line = 0;

  ifstream fin("data2.txt");
  int dummy;
  fin >> dummy;

  while (fin) {
    fin >> num;
    if (fin.fail())
      break;

    int robot[2] = { 1, 1 };
    int step[2]  = { 0, 0 };
    char last_r = -1;

    for (int i = 0; i < num; ++i) {
      fin >> r >> b;
      
      // cout << num << ' '
      //    << r << ' '
      //    << b << endl;

      if (last_r == r) {
        if (r == 'O') {
          step[0] += abs(b - robot[0]) + 1;
          robot[0] = b;

        } else if (r == 'B') {
          step[1] += abs(b - robot[1]) + 1;
          robot[1] = b;
        }

      } else {
        if (r == 'O') {
          step[0] += abs(b - robot[0]) + 1;
          step[0] = std::max(step[0], step[1] + 1);
          robot[0] = b;
        } else if (r == 'B') {
          step[1] += abs(b - robot[1]) + 1;
          step[1] = std::max(step[1], step[0] + 1);
          robot[1] = b;
        }
      }
      
      // cout << step[0] << ", " << step[1] << endl;
      last_r = r;
    }

    cout << "Case #" << ++line << ": ";
    cout << std::max(step[0], step[1]) << endl;
  }
  fin.close();

  return 0;
}
