#include<iostream>
#include<stdlib.h>
#include<map>
#include<string>
#include<vector>
#include<set>

using namespace std;

int main() {
  int T, C, D, N;
  cin >> T;
  for (int t = 0; t < T; t++) {
    map<string, char> combine;
    set<string> oppose;
    string input;
    vector<char> output;
    cin >> C;
    while (C--) {
      string s1, s2;
      cin >> s1;
      combine[s1.substr(0, 2)] = s1[2];
      s2 = s1.substr(1, 1);
      s2.push_back(s1[0]);
      combine[s2] = s1[2];
    }
    cin >> D;
    while (D--) {
      string s1, s2;
      cin >> s1;
      oppose.insert(s1);
      s2 = s1.substr(1, 1);
      s2.push_back(s1[0]);
      oppose.insert(s2);
    }
    cin >> N >> input;
    for (int n = 0; n < N; n++) {
      output.push_back(input[n]);
      int size = output.size();
      if (output.size() > 1) {
        string endpair(1, output[size - 1]);
        endpair.push_back(output[size - 2]);
        map<string, char>::const_iterator replacement = combine.find(endpair);
        if (replacement != combine.end()) {
          output.erase(output.end() - 2, output.end());
          output.push_back(replacement->second);
          continue;
        }
        for (int i = 0; i < size - 1; i++) {
          string clearpair(1, output[size - 1]);
          clearpair.push_back(output[i]);
          if (oppose.find(clearpair) != oppose.end()) {
            output.clear();
            break;
          }
        }
      }
    }
    cout << "Case #" << t + 1 << ": [";
    for (int i = 0; i < output.size(); i++) {
      if (i != 0)
        cout << ", ";
      cout << output[i];
    }
    cout << "]" << endl;
  }
  return 0;
}
