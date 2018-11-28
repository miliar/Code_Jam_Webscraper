#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main(int argc, char **argv) {

  char *filename = argv[1];

  ifstream file(filename);

  long int T;
  file >> T;

  long int c = 1000000000;

  long int R, k, N, g;
  
  for (long int i = 1; i <= T; i++) {
    file >> R >> k >> N;

    queue<long int> q;
    for (long int j = 0; j < N; j++) {
      file >> g;
      q.push(g);
    }

    long int s, tot = 0, tmp, h;
    while (R > 0) {
      h = 0, s = 0;
      while (h < N && s <= k) { 
        tmp = q.front(); 
        if (s + tmp <= k) {
          q.pop();
          s += tmp;
          q.push(tmp);
          h++;
        } else {
          break;
        }
      }
      tot += s;
      R--;
    }

    cout << "Case #" << i << ": " << tot << endl;
  }

  file.close();
}
