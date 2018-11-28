
#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstring>
using namespace std;

int inList[200];
vector<int> list;

void clearList() {
  list.clear();
  memset(inList, 0, sizeof(inList));
}

bool opposed[1000][1000];
char combine[1000][1000];

void invoke(int elem) {
  if (!list.empty() && combine[list.back()][elem]) {
    // Combines
    int back = list.back();
    int c = (int)combine[list.back()][elem];
    list.pop_back();
    inList[back]--;
    list.push_back(c);
    inList[c]++;
    return;
  }
  // Search for opposed
  for (int i = 0; i < list.size(); i++) {
    if (opposed[list[i]][elem]) {
      clearList();
      return;
    }
  }
  // Add to list
  list.push_back(elem);
  inList[elem]++;
}

char getChar(int i) {
  return (char)list[i];
}

int main() {

  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {

    memset(opposed, 0, sizeof(opposed));
    memset(combine, 0, sizeof(combine));
    memset(inList, 0, sizeof(inList));
    list.clear();

    int C;
    cin >> C;
    for (int c = 0; c < C; c++) {
      char a, b, to;
      cin >> a >> b >> to;
      combine[(int)a][(int)b] = to;
      combine[(int)b][(int)a] = to;
    }

    int D;
    cin >> D;
    for (int d = 0; d < D; d++) {
      char a, b;
      cin >> a >> b;
      opposed[(int)a][(int)b] = true;
      opposed[(int)b][(int)a] = true;
    }

    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
      char elem;
      cin >> elem;
      invoke((int)elem);
    }

    cout << "Case #" << t << ": ";
    if (list.empty()) {
      cout << "[]" << endl;
    } else {
      cout << "[" << getChar(0);
      for (int i = 1; i < list.size(); i++) {
        cout << ", " << getChar(i);
      }
      cout << "]" << endl;
    }

  }

}

