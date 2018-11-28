#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

int n;
char dict[256];
char inp[500];
using namespace std;
int main(int argc, char** argv){
  freopen("A-small-0.in", "r", stdin);
  freopen("A-small-0.out", "w", stdout);
  n = 0;
  memset(dict, 0, sizeof(dict));
  dict['a']='y';
  dict['o'] = 'e';
  dict['z'] = 'q';
  dict['q'] = 'z';
  dict['\0'] = '\0';
  const char *stri[5], *stro[5];
  stri[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  stro[0] = "our language is impossible to understand";
  stri[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  stro[1] = "there are twenty six factorial possibilities";
  stri[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  stro[2] = "so it is okay if you want to just give up";
  for(int i = 0; i < 3; i++) for(int j = 0; j < strlen(stri[i]); j++)
			       dict[stri[i][j]] = stro[i][j];
  scanf("%d", &n);
  dict[' '] = ' ';
  char out[500];
  gets(inp);
  for(int case_id=1;case_id<=n;case_id++){
    printf("Case #%d: ", case_id);
    //scanf("%s", inp);
    gets(inp);
    int i;
    for(i = 0; i < strlen(inp); i++){
      out[i] = dict[inp[i]];
      //      printf("%c->%c\n", inp[i], out[i]);
    }
    out[i] = '\0';
    printf("%s\n", out);
  }
  
  return 0;
}

