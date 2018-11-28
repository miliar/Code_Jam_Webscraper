#include <iostream>
#include <vector>

using namespace std;

const int MAX_CHAR = 128;

bool opposed(char a, const vector<char> &elemList, const bool oppose[][MAX_CHAR]) {
  for (vector<char>::const_iterator i = elemList.begin(); i != elemList.end(); ++i)
    if (oppose[a][*i])
      return true;
  return false;
  }

void invokeElem(char a, vector<char> &elemList, const char combos[][MAX_CHAR], const bool oppose[][MAX_CHAR]) {
  if (elemList.empty())
    elemList.push_back(a);
  else if (combos[a][elemList.back()])
    elemList.back() = combos[a][elemList.back()];
  else if (opposed(a, elemList, oppose))
    elemList.clear();
  else
    elemList.push_back(a);
  }

int main() {
  int T; cin >> T;
  for (int cNum = 1; cNum <= T; ++cNum) {
    
    char combos[MAX_CHAR][MAX_CHAR] = {{0}};
    int C; cin >> C;
    for (int i = 0; i < C; ++i) {
      char a, b, c; cin >> a >> b >> c;
      combos[a][b] = combos[b][a] = c;
      }

    bool oppose[MAX_CHAR][MAX_CHAR] = {{false}};
    int D; cin >> D;
    for (int i = 0; i < D; ++i) {
      char a, b; cin >> a >> b;
      oppose[a][b] = oppose[b][a] = true;
      }

    int N; cin >> N;
    vector<char> elemList;
    for (int i = 0; i < N; ++i) {
      char a; cin >> a;
      invokeElem(a, elemList, combos, oppose);
      }

    cout << "Case #" << cNum << ": [";
    for (vector<char>::const_iterator i = elemList.begin(); i != elemList.end(); ++i) {
      if (i != elemList.begin()) cout << ", ";
      cout << *i;
      }
    cout << "]\n";
      
    
    }
  }
