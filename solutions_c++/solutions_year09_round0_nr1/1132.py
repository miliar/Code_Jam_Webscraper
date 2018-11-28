
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> W;

int count(string pattern) {
  int c = 0;
  for(int i = 0; i < W.size(); i++) {   
    for(int j = 0, k = 0; j < W[i].length(); j++) {
      bool ok = false;
      if(pattern[k] == W[i][j]) ok = true;
      else if(pattern[k] == '(') {
        for(; pattern[k] != ')'; k++) if(pattern[k] == W[i][j]) ok = true;
      }     
      if(!ok) break;
      if(j == W[i].length() -1) c++;
      k++;
    }
  }
  return c;
}

int main() {
  int L, D, N;
  cin >> L >> D >> N;
  for(int i = 0; i < D; i++) {
    string word;
    cin >> word;
    W.push_back(word);
  }

  for(int i = 1; i <= N; i++) {
    string pattern;
    cin >> pattern;
    cout << "Case #" << i << ": " << count(pattern) << endl;
  }
}
