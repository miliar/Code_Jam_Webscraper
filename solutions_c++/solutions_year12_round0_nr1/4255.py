#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <set>

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;

int T;

char g[3][200] = {
"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv" };

char s[3][200] = {
"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"
};

char p[300];
char ss[300];

int main()
{
  for (int i = 0; i < 3; ++i)
    for (int j = 0; j < strlen(g[i]); ++j)
      p[g[i][j]] = s[i][j];
  p['q'] = 'z';
  p['z'] = 'q';

  /*for (char ch = 'a'; ch <= 'z'; ++ch)
    printf("%c = %c\n", ch, p[ch]); */
  scanf("%d", &T);
  gets(ss);
  for (int t = 0; t < T; ++t)
  {
    gets(ss);
    for (int i = 0; i < strlen(ss); ++i)
      ss[i] = p[ss[i]];
    printf("Case #%d: %s\n", t+1, ss);
  } 
  return 0;
}