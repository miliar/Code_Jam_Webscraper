#include <cstdio>
#include <assert.h>
#include <vector>
#include <string>
#include <iostream>

using namespace  std;

int n;

int solve(const string& line, const string& pattern) {
  typedef vector< vector<int> > PosVec;
  PosVec posVec;
  posVec.resize(256);
  for (int i = pattern.size() - 1; i >= 0 ; --i) {
    posVec[pattern[i]].push_back(i+1);
  }
  
  vector<int> resultVec;
  resultVec.resize(pattern.size()+1, 0);
  resultVec[0] = 1;
  for (string::const_iterator it = line.begin(); it != line.end(); ++it) {
    int c = *it;
/*    printf("xxxx %c %d -> ", (char)(c), posVec[c].size());
    for (int i = 0; i < posVec[c].size(); ++i) {
      printf ("%d ", posVec[c][i]);
    }
    printf("\n");*/

    for (vector<int>::const_iterator it2 = posVec[c].begin(); it2 != posVec[c].end(); ++it2) {
      assert(*it2 < pattern.size() + 1);
      resultVec[*it2] += resultVec[(*it2) - 1];
      resultVec[*it2] %= 10000;
    }

/*   for(int i = 0; i < resultVec.size(); ++i) {
      printf("resultvec[%d]=%d\n", i, resultVec[i]);
      }*/
  }
  

  return resultVec[pattern.size()];
}

void readlinex(string& line) {
  char c;
  while ((c = getc(stdin)) != '\n') {
    line += c;
  }
}

int main() {
  cin >> n;
  cin.ignore();
  for (int i = 0; i < n; ++i) {
    string line;
    readlinex(line);
    printf("Case #%d: ", i+1);
    printf("%04d\n", solve(line, "welcome to code jam"));
  }

  
}
