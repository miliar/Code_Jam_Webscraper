#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef pair<char, char> cc;

struct Case {
  vector<char> elements;
  map<char, int> element_chars;
  
  map<cc,char> combine;
  map<char, char> oppose;
  
  Case(int n) {
    read();
    int q; cin >> q;
    string s; cin >> s;
    process(s);
    printf("Case #%d: [", n);
    for (int i=0; i < elements.size(); i++) {
      if (i) printf(", ");
      printf("%c", elements[i]);
    }
    printf("]\n");
  }
  
  void process(string &s) {
    for (int i = 0; i < s.size(); i++) {
      elements.push_back(s[i]);
      element_chars[s[i]]++;

foo:     
      if (elements.size() >= 2) {
        int a = elements[elements.size()-1];
        int b = elements[elements.size()-2];
        if (combine.find(cc(a,b)) != combine.end()) {
          elements.pop_back();
          elements.pop_back();
          element_chars[a]--;
          element_chars[b]--;
          char t = combine[cc(a,b)];
          elements.push_back(t);
          element_chars[t]++;
          goto foo;
        }
      }      
      if (oppose.find(elements[elements.size()-1]) != oppose.end()) {
        if (element_chars[oppose[elements[elements.size()-1]]] > 0) {
          elements.clear();
          element_chars.clear();
          continue;
        }
      }

    }
  }
  
  void read() {
    int c; cin >> c; cin.ignore();
    for (int i=0; i < c; i++) {
      string s; cin >> s;
      char a = s[0];
      char b = s[1];
      char t = s[2];
      combine[cc(a,b)] = t;
      combine[cc(b,a)] = t;
    }
    int d; cin >> d; cin.ignore();
    for (int i=0; i < d; i++) {
      string s; cin >> s;
      char a = s[0];
      char b = s[1];
      oppose[a] = b;
      oppose[b] = a;
    }
  }
};

int main() {
  int t; cin >> t; cin.ignore();
  for (int i=1;i<=t;i++) {
    Case c(i);
  }
}