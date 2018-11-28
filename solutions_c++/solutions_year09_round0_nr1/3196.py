#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
  int L;
  int D;
  int N;
  string curWord;
  string s;

  ifstream inFile("A-large.in");

  vector<string> dictionary;
  vector<vector<string> > cases;
  vector<string> tmpstr;
  string subs;

  dictionary.clear();
  cases.clear();
  tmpstr.clear();

  if (!inFile.is_open())
    return 1;

  inFile >> L;
  inFile >> D;
  inFile >> N;

  for (int c = 0; c < D; c++ ) {
    inFile >> curWord;
    dictionary.push_back(curWord);
  }

  for (int c = 0; c < N; c++ ) {
    bool in_paren = false;
    subs.clear();
    tmpstr.clear();
    s.clear();
    inFile >> curWord;

    for (unsigned int d = 0; d < curWord.size(); d++) {
      if (in_paren) {
        if (curWord[d] != '(' && curWord[d] != ')') {
          s = curWord[d];
          subs.append( s );
        }
        else if (curWord[d] == ')') {
          in_paren = false;
          tmpstr.push_back(subs);
          subs.clear();
          s.clear();
        }
        else {
          cout << "ERROR" << endl;
        }
      }
      else {
        if (curWord[d] == '(') {
          in_paren = true;
        }
        else if (curWord[d] == ')') {
          cout << "ERROR" << endl;
        }
        else {
          s = curWord[d];
          tmpstr.push_back(s);
          s.clear();
        }
      }
    }
    cases.push_back(tmpstr);
  }

  inFile.close();
  ofstream outFile("A-large.out");
  for (unsigned int n = 0; n < cases.size(); n++) {
    int match_count = 0;

    for (int d = 0; d < D; d++) {
      bool no_match = false;
      int i = 0;
      string tmpWord = dictionary[d];
      string tmpPhrase;

      while ((i < L) && (!no_match)) {
        no_match = true;
        unsigned int c = 0;

        while ((c < cases[n][i].size()) && (no_match)) {
          if ( cases[n][i][c] == tmpWord[i] ) {
            no_match = false;
          }
          c++;
        }
        i++;
      }
      if (!no_match) {
        match_count++;
      }
    }
    //ofstream outFile("A-small.out");
    //cout << "Case #" << (n + 1) << ": " << match_count << endl;
    outFile << "Case #" << (n + 1) << ": " << match_count << endl;
  }
  outFile.close();

  return 0;
}
