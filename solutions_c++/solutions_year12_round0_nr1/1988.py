#include <iostream>
#include <string>

const char I[] = \
  "our language is impossible to understand"     \
  "there are twenty six factorial possibilities" \
  "so it is okay if you want to just give up";

const char O[] = \
  "ejp mysljylc kd kxveddknmc re jsicpdrysi"     \
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" \
  "de kr kd eoya kw aej tysr re ujdr lkgc jv";


char a2g[260];
char g2a[260];

static std::string translate(std::string s)
{
  for (unsigned i = 0; i < s.length(); ++i) {
    s[i] = g2a[s[i]];
  }
  return s;
}

int main()
{
  memset(a2g, '*', sizeof(a2g));
  memset(g2a, '*', sizeof(g2a));

  a2g[' '] = ' '; g2a[' '] = ' ';
  a2g['z'] = 'q'; g2a['q'] = 'z';
  a2g['q'] = 'z'; g2a['z'] = 'q';

  for (unsigned i = 0; i < sizeof(I); ++i) {
    char x = I[i];
    char y = O[i];
    a2g[x] = y;
    g2a[y] = x;
  }

  // std::cout << "abcdefghijklmnopqrstuvwxyz" << std::endl;
  // for (char c = 'a'; c <= 'z'; ++c) {
  //   std::cout << a2g[c];
  // }
  // std::cout << std::endl;
  // std::cout << std::endl;
  // std::cout << std::endl;

  // for (char c = 'a'; c <= 'z'; ++c) {
  //   std::cout << g2a[c];
  // }
  // std::cout << std::endl;
  // std::cout << "abcdefghijklmnopqrstuvwxyz" << std::endl;

  int nCase;
  std::cin >> nCase;

  std::string str;
  std::getline(std::cin, str);
  for (int iCase = 1; iCase <= nCase; iCase++) {
    std::getline(std::cin, str);
    std::cout << "Case #" << iCase << ": " << translate(str) << std::endl;
  }

  return 0;
}
