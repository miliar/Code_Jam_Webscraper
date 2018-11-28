#include <iostream>
#include <string>

using namespace std;

int main()
{
  int nCases;
  cin >> nCases;
  cin.ignore();
  char mapping[256];
  for (int i=0; i<256; i++)
    mapping[i] = '*';
  const char *s1from = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  const char *s2from = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  const char *s3from = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  const char *s1to = "our language is impossible to understand";
  const char *s2to = "there are twenty six factorial possibilities";
  const char *s3to = "so it is okay if you want to just give up";
  for (int i=0; s1from[i] != '\0'; i++)
    mapping[s1from[i]] = s1to[i];
  for (int i=0; s2from[i] != '\0'; i++)
    mapping[s2from[i]] = s2to[i];
  for (int i=0; s3from[i] != '\0'; i++)
    mapping[s3from[i]] = s3to[i];
  mapping['q'] = 'z';
  mapping['z'] = 'q';

  for (int caseNumber=1; caseNumber <= nCases; caseNumber++) {
    string line;
    getline(cin, line);
    cout << "Case #" << caseNumber << ": ";
    for (int i=0; i<line.length(); i++) {
      line[i] = mapping[line[i]];
    }
    cout << line;
    cout << endl;
  }
  return 0;
}
