#include <cstdio>
#include <cassert>

#include <iostream>
#include <string>

using namespace std;

int main()
{
  string encrypted =
    "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string decrypted =
    "our language is impossible to understand"
    "there are twenty six factorial possibilities"
    "so it is okay if you want to just give up";
  assert(encrypted.size() == decrypted.size());

  int to[256] = {0};
  for (int i = 0; i < 256; ++i)
    to[i] = i;

  int n = (int)encrypted.size();

  for (int i = 0; i < n; ++i)
  {
    to[(int)encrypted[i]] = decrypted[i];
  }
/*
  for (int i = 'a'; i <= 'z'; ++i)
    if (to[i])
      printf("%c --> %c\n", (char)i, (char)to[i]);
 */

  to['q'] = 'z';
  to['z'] = 'q';

  string T;
  getline(cin, T);

  cin >> noskipws;
  int no = 0;
  for (string s; getline(cin, s); ) {
    for (int i = 0; i < (int)s.size(); ++i)
      s[i] = to[(int)s[i]];
    cout << "Case #" << ++no << ": " << s << endl;
  }

  return 0;
}
