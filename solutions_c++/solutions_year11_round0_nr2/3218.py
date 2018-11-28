#include <iostream>
#include <cstdlib>
#include <map>

using namespace std;

int main(int argc, char* argv[])
{
  int T, C, D, N;
  string str;
  int size = 'Z';
  char combineMap[size][size];
  bool oppose[size][size];
  char c, c1, c2;
  string elemList;
  bool erased = false;

  cin >> T;
  for (int i = 0; i < T; ++i) {
    elemList.clear();
    for (int k = 0; k < size; ++k) {
      for (int l = 0; l < size; ++l) {
        combineMap[k][l] = '0';
        oppose[k][l] = false;
      }
    }

    cin >> C;
    for (int j = 0; j < C; ++j) {
      cin >> str;
      combineMap[str[0]][str[1]] = str[2];
      combineMap[str[1]][str[0]] = str[2];
    }

    cin >> D;
    for(int j = 0; j < D; ++j) {
      cin >> str;
      oppose[str[0]][str[1]] = oppose[str[1]][str[0]] = true;
    }

    cin >> N;
    cin >> str;
    elemList.append(1, str[0]);
    for (int j = 1; j < N; ++j) {
      c1 = str[j];
      c2 = elemList[elemList.size() - 1];
      if ((c=combineMap[c1][c2]) != '0') {
        elemList[elemList.size() - 1] = c;
        continue;
      }

      erased = false;
      for (int k = 'A'; k < size; ++k) {
        if (oppose[c1][k]) {
          if (elemList.find(k) != string::npos) {
            elemList.clear();
            erased = true;
            break;
          }
        }
      }
      if (!erased)
        elemList.append(1, c1);
     
    }
    cout << "Case #" << (i+1) << ": [";
    int j;
    if (elemList.size()) {
        for (j = 0; j < elemList.size() - 1; ++j) {
            cout << elemList[j] << ", ";
        }
      cout << elemList[j];
    }
    cout << "]" << endl;
  }

  return 0;
}
