#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <fstream>

using namespace std;

#define STRBUF 1000

map<char, char> m;

void print_map() {
  for (map<char, char>::iterator it = m.begin();
       it != m.end();
       it++) {
    printf ("%c %c\n", it->first, it->second);
  }
}

int main() {
  m[' '] = ' ';
  m['z'] = 'q';
  m['q'] = 'z';

  fstream fin ("A.sample", fstream::in);
  for (int i = 0; i < 3; i++) {
    char sin[STRBUF], sout[STRBUF];
    fin.getline (sin, STRBUF);
    fin.getline (sout, STRBUF);
    //printf ("%s %s\n", sin, sout);

    for (int j = 0; j < strlen(sin); j++) {
      //printf ("%c %c\n", sin[j], sout[j]);
      if (!m.count(sin[j])) m[sin[j]] = sout[j];
      else {
        if (m[sin[j]] != sout[j]) {
          printf ("Failure in making array!\n");
          //print_map();
          return 0;
        }
      }
    }
  }
  //print_map();

  int n_cases;
  scanf ("%d\n", &n_cases);
  for (int i_case = 0; i_case < n_cases; i_case++) {
    char sin[STRBUF], sout[STRBUF];
    cin.getline (sin, STRBUF);
    //printf ("%s %d\n", sin, strlen(sin));

    for (int i = 0; i < strlen(sin); i++) sout[i] = m[sin[i]];
    sout[strlen(sin)] = '\0';

    printf ("Case #%d: %s\n", i_case+1, sout);
  }
}
