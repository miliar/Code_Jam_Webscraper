// Solution made by Peter Zeman.
// {{{
// vim:filetype=cpp foldmethod=marker foldmarker={{{,}}}
#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vpii;
#define debug(x) cout << ">>> " << x << endl;
// }}}

int main()
{
  int t;
  string m("yhesocvxduiglbkrztnwjpfmaq");
  scanf("%d", &t);
  getchar();
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    char c;
    while ((c = getchar()) != '\n')
      if (c == ' ') putchar(' ');
      else putchar(m[c - 'a']);
    putchar(c);
  }
  return 0;
}
