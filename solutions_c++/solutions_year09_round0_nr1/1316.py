#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main () {
  int D, L, N;
  
  vector<string> language = vector<string> ();
  scanf ("%d%d%d", &L, &D, &N);
  
  for (int i = 0; i < D; i++) {
    char s[16];
    scanf ("%s", s);
    string st = string(s);
    language.push_back(st);
  }
  
  for (int i = 1; i <= N; i++) {
    string s;
    vector <string> parlang = language;
      
    for (int j = 0; j < L; j++) {
      vector<string> par;
      char c = getchar();
      vector<char> possib = vector<char> ();
      
      while (c == '\n')
        c = getchar();
      if (c == '(') {
        c = getchar();
        while (c != ')') {
          possib.push_back (c);
          c = getchar();
        }
      }
      else
        possib.push_back(c);
      
      /*for (int k = 0; k < possib.size(); k++)
        printf ("%c ", possib[k]);
      printf ("\n");*/
      
      for (int k = 0; k < parlang.size(); k++) {
        for (int l = 0; l < possib.size(); l++) {
          if (parlang[k][j] == possib[l]) {
            par.push_back(parlang[k]);
            break;
          }
        }
      }
      parlang = par;
      //printf ("%d\n", parlang.size());
    }
    printf ("Case #%d: %d\n", i, parlang.size());
    
  }
  return 0;
}
