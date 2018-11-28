#include <iostream>
#include <vector>
#include <string>

using namespace std;


typedef long long int LL;

int main() {
  LL L, D, N;
  vector<string> words;
  
  cin >> L >> D >> N;
  string s;
  getline(cin, s);

  for (int i = 0; i < D; i++) {
    getline(cin, s);
    words.push_back(s);
  }
  
  for (int i = 0; i < N; i++) {
    string s;
    getline(cin, s);
    cout << "Case #" << i+1 << ": ";

    int ct = 0;
    for (int j = 0; j < D; j++) {
      bool bad = false;
      int p = 0;
      for (int k = 0; !bad && k < L; k++) {
	if (s[p] == '(') {
	  bool found = false;
	  while (true) {
	    ++p;
	    if (s[p] == words[j][k]) found = true;
	    if (s[p] == ')') break;
	  }
	  if (!found) bad = true;
	  
	} else {
	  if (s[p] != words[j][k]) bad = true;
	}
	++p;
      }
      if (!bad) ct++;
    }
    
    cout << ct << endl;
  }
  
}
