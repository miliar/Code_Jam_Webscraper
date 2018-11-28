#include <iostream>
#include <cstring>
#include <map>

using namespace std;

int L, D, N;
string Dic[6000];
string pattern;
map<char, bool> pm[20];

void buildMap() {
  int k = 0;

  for (int i = 0; i < L; i++) {    
    pm[i].clear();
    if (pattern[k] != '(') {
      pm[i][pattern[k++]] = true;
    } else {
      k++;
      while (pattern[k] != ')') {
	pm[i][pattern[k++]] = true;
      }
      k++;
    }
  }
}

int solve() {
  int c = 0;
  bool found;

  buildMap();

  for (int i = 0; i < D; i++) {
    found = true;
    for (int j = 0; j < L; j++) {
      if (pm[j][Dic[i][j]] != true) {
	found = false;
	break;
      }
    }

    if (found) {
      
      c++;
    }
  }

  return c;
}

int main() {
  int t = 1;
  
  cin >> L >> D >> N;

  for (int i = 0; i < D; i++) {
    cin >> Dic[i];
  }

  while (N) {
    cin >> pattern;

    cout << "Case #" << t++ << ": " << solve() << endl;
    N--;
  }
  

  return EXIT_SUCCESS;
}
