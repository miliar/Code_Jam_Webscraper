#include <map>
#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

map<char, char> mapping;

void solve (int a_case) {
  string s;

  getline(cin, s);

  for (int i = 0; i < s.size(); ++i)
    s[i] = mapping[s[i]];

  printf("Case #%d: %s\n", a_case, s.c_str());
}

int main ()
{
  int n;
  string dummy;

  string bootstrap[] = {
    "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv y qee z",
    "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up a zoo q"
  };


  for (int i = 0; i < bootstrap[0].size(); ++i) {
    char& c = mapping[bootstrap[0][i]];
    if (c == 0) c = bootstrap[1][i];
    else if (c != bootstrap[1][i]) { fprintf(stderr, "Invalid bootstrap at position %d\n", i); return 1; }
  }

  if (mapping.size() != 27) {
    fprintf(stderr, "Mapping incomplete! Only %d entries\n", (int)mapping.size());

    for (map<char,char>::iterator it = mapping.begin(); it != mapping.end(); ++it) {
      fprintf(stderr, "[%c] -> [%c]\n", it->first, it->second);
    }

    return 2;
  }

  cin >> n;
  getline(cin, dummy);
  for (int i = 0; i < n; ++i) solve(i+1);

  return 0;
}



