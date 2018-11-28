#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("file.out");

//#define fin cin
//#define fout cout

int main() {
  int L, D, N;
  fin >> L >> D >> N;
  vector<string> words;
  for(int i = 0; i < D; i++) {
    string temp;
    fin >> temp;
    words.push_back(temp);
  }
  vector<vector<string> > patterns;
  for(int i = 0; i < N; i++) {
    string temp;
    fin >> temp;
    string tmp;
    bool b = false;
    patterns.push_back(vector<string>());
    for(int j = 0; j < temp.length(); j++) {
      if(temp[j] == '(') {
        b = true;
        continue;
      }
      if(temp[j] == ')') {
        b = false;
        patterns[i].push_back(tmp);
        tmp.clear();
        continue;
      }
      if(b)
        tmp.push_back(temp[j]);
      else
        patterns[i].push_back(string(1,temp[j]));
    }
  }
  vector<int> results;
  for(int k = 0; k < N; k++) {
    int res = 0;
    for(int i = 0; i < D; i++) {
      bool b = false;
      for(int j = 0; j < L; j++) {
        char cur = words[i][j]; //Текущий элемент для проверки соответствия шаблону
        for(int l = 0; l < patterns[k][j].length(); l++) {
          if(cur == patterns[k][j][l]) {
            b = true;
            break;
          }
        }
        if(!b)
          break;
        if(j+1 != L)
          b = false;
      }
      res += b;
    }
    results.push_back(res);
    fout << "Case #" << k+1 << ": " << res << endl;
  }
}
