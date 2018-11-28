#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
  freopen("output.txt", "w", stdout);
  freopen("input.txt", "r", stdin);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    vector<vector<int> > replaces(26, vector<int>(26, -1));
    vector<vector<bool> > removes(26, vector<bool>(26));
    int C; 
    cin >> C;
    for (int i= 0; i < C; ++i) {
      string s;
      cin >> s;
      replaces[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
      replaces[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
    }
    int D; 
    cin >> D;
    for (int i= 0; i < D; ++i) {
      string s;
      cin >> s;
      removes[s[0] - 'A'][s[1] - 'A'] = true;
      removes[s[1] - 'A'][s[0] - 'A'] = true;
    }
    int N;
    cin >> N;
    string line;
    cin >> line;

    vector<int> elements;
    vector<int> pr(26);
    
    for (int i = 0; i < N; ++i) {
      int e = line[i] - 'A';
      if (elements.size() != 0 && replaces[e][elements.back()] != -1) {
        --pr[elements.back()];
        ++pr[replaces[e][elements.back()]];
        elements.back() = replaces[e][elements.back()];
      } else {
        elements.push_back(e);
        ++pr[e];
        for (int j = 0; j < 26; ++j) {
          if (pr[j] != 0 && removes[j][e]) {
            elements.clear();
            pr.assign(26, 0);
            break;
          }
        }
      }
    }
    cout << "Case #" << t << ": [";
    for (int i= 0; i < elements.size(); ++i) {
      if (i != 0) cout << ", ";
      cout << (char)(elements[i] + 'A');
    }
    cout << "]" << endl;

  }
}