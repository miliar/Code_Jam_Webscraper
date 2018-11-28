#include <iostream>
#include <list>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <set>
using namespace std;

struct dir {
  vector<dir*> subdirs;
  string name;
};

int main() {
  ifstream cin("A-large (1).in");
  ofstream cout("out.txt");
  int T = 0;
  cin >> T;
  for(int t = 0; t < T; t++) {
    cout << "Case #" << t+1 << ": ";
    int N, M;
    cin >> N >> M;
    set<string> exist;
    vector<string> need;
    string str;
    for(int i = 0 ; i < N; i++) {
      cin >> str;
      exist.insert(str);
    }
    for(int i = 0; i < M; i++) {
      cin >> str;
      need.push_back(str);
    }
    exist.insert("/");
    for(int i = 0; i < M; i++) {
      str = need[i];
      for(int j = 1; j <= str.length(); j++) {
        if(str[j] != '/' && j != str.length())
          continue;
        exist.insert(str.substr(0, j));
      }
    }
    cout << exist.size() - N - 1 << endl;
  }
}
