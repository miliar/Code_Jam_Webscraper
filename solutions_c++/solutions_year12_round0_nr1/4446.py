#include <algorithm>
#include <bitset>
#include <cmath>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

bool ok[26];
char mmm[26];

string examples_in[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
  "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

string examples_out[3] = {"our language is impossible to understand",
  "there are twenty six factorial possibilities",
  "so it is okay if you want to just give up"};

int main() {
  int TS;
  
  freopen("input.txt", "r", stdin);
  freopen("output.txt" ,"w", stdout);

  memset(mmm, 26, sizeof(mmm));
   
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < examples_in[i].size(); j++) {
      if (isalpha(examples_in[i][j])) {
        ok[examples_out[i][j] - 'a'] = true;
        mmm[examples_in[i][j] - 'a'] = examples_out[i][j];
      }
    }
  }

 mmm[16] = 'z';
 mmm[25] = 'q';

  scanf("%d\n", &TS);
  for (int ts = 1; ts <= TS; ts++) {
    char str[256];
    scanf("%[^\n]\n", str);
  
    printf("Case #%d: ", ts);
    for (int i = 0, sz = strlen(str); i < sz; i++) {  
      if (isalpha(str[i])) {
        printf("%c", mmm[str[i]-'a']);
      } else {
        printf("%c", str[i]);
      }
    }
    puts("");
  }

  return 0;
}