#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <list>
#include <set>
#include <vector>

using namespace std;

void handleCase(int casenum) {
  map<string, char> c;
  map<char, list<char> > d;

  int C;
  cin >> C;
  for(int i = 0; i < C; ++i) {
    string s;
    cin >> s;
    string pr = s.substr(0,2);
    char t = s[2];
    c[pr] = t;
    swap(pr[0], pr[1]);
    c[pr] = t;
  }

  int D;
  cin >> D;
  for(int i = 0; i < D; ++i) {
    string s;
    cin >> s;
    d[s[0]].push_back(s[1]);
    d[s[1]].push_back(s[0]);
  }

  int N;
  cin >> N;
  map<char, int> inSeq;
  vector<char> sequence;
  for(int i = 0; i < N; ++i) {
    char ch;
    cin >> ch;
    if(sequence.size() > 0) {
      const int lastI = sequence.size()-1;
      char last = sequence[lastI];
      string s;
      s.push_back(ch);
      s.push_back(last);
      if(c.find(s) != c.end()) {
        --inSeq[last];
        char tt = c[s];
        ++inSeq[tt];
        sequence[lastI] = tt;
      } else {
        ++inSeq[ch];
        sequence.push_back(ch);
      }
    } else {
      ++inSeq[ch];
      sequence.push_back(ch);
    }
    char last = sequence[sequence.size()-1];
    list<char>& ll = d[last];
    for(list<char>::const_iterator it = ll.begin(); it != ll.end(); ++it) {
      if(inSeq[*it] > 0) {
        inSeq.clear();
        sequence.clear();
        break;
      }
    }
  }
  const int ss = sequence.size();
  cout << "Case #" << casenum << ": [";
  if(ss > 0) {
    cout << sequence[0];
  }
  for(int i = 1; i < sequence.size(); ++i) {
    cout << ", " << sequence[i];
  }
  cout << "]\n";
}

int main() {
  int cases;
  cin >> cases;
  for(int i = 0; i < cases; ++i) {
    handleCase(i+1);
  }
}
