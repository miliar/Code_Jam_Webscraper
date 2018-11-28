#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <set>

using namespace std;

map<string, char> compound;
set<string> opposed;

int main () {
  int T;
  scanf ("%d", &T);
  for (int t = 1; t <= T; t++) {
    compound = map<string,char> ();
    opposed = set<string> ();
    
    int C, D, N;
    char c1, c2, r;
    scanf ("%d", &C);
    //printf ("C %d\n", C);
    while (C > 0) {
      getc(stdin);
      scanf("%c%c%c", &c1, &c2, &r);
      string s, s1;
      s.push_back(c1);
      s.push_back(c2);
      s1.push_back(c2);
      s1.push_back(c1);
      compound[s] = r;
      compound[s1] = r;
      //printf ("%s %s %c\n", s.c_str(), s1.c_str(), compound[s]);
      C--;
    }
    scanf ("%d", &D);
    //printf ("D %d\n", D);
    while (D > 0) {
      getc(stdin);
      scanf("%c%c", &c1, &c2);
      string s, s1;
      s.push_back(c1);
      s.push_back(c2);
      s1.push_back(c2);
      s1.push_back(c1);
      opposed.insert(s);
      opposed.insert(s1);
      //printf ("%s %s\n", s.c_str(), s1.c_str());
      D--;
    }
    scanf ("%d", &N);
    //printf ("N %d\n", N);
    getc(stdin);
    vector<char> list = vector<char> ();
    while (N > 0) {
      char c;
      scanf ("%c", &c);
      //printf ("%c\n", c);
      if (list.size() > 0) {
        char ant = list[list.size()-1];
        string s;
        s.push_back(c);
        s.push_back(ant);
        if (compound.find(s) != compound.end()) {
          list.pop_back();
          list.push_back(compound[s]);
        }
        else
          list.push_back(c);
      }
      else
        list.push_back(c);
      
      char last = list[list.size()-1];
      for (int i = 0; i < list.size()-1; i++) {
        string s;
        s.push_back(last);
        s.push_back(list[i]);
        //printf ("procurei %s\n", s.c_str());
        if (opposed.find(s) != opposed.end()) {
          //printf ("achei!");
          list.clear();
          break;
        }
      }
      N--;
      
    }
    int s = list.size()-1;
    printf ("Case #%d: [", t);
    for (int i = 0; i < s; i++)
      printf ("%c, ", list[i]);
    if (list.size() > 0)
      printf ("%c", list[list.size()-1]);
    printf ("]\n");
  }
  return 0;
}

