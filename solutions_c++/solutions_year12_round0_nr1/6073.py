
/**
 *
 *  Time-stamp:<2012/04/14 14:13:08>
 **/

#include <functional>
#include <algorithm>
#include <iostream>
#include <complex>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
#include <cctype>
#include <deque>
#include <stack>
#include <queue>
#include <cmath>
#include <set>
#include <map>
using namespace std;

int c;
string g;

string solve() {
  char ans[g.size()];
  for(int i=0; i<(int)g.size(); i++) {
    switch(g[i]) {
    case 'a':
      ans[i] = 'y';
      break;
    case 'b':
      ans[i] = 'h';
      break;
    case 'c':
      ans[i] = 'e';
      break;
    case 'd':
      ans[i] = 's';
      break;
    case 'e':
      ans[i] = 'o';
      break;
    case 'f':
      ans[i] = 'c';
      break;
    case 'g':
      ans[i] = 'v';
      break;
    case 'h':
      ans[i] = 'x';
      break;
    case 'i':
      ans[i] = 'd';
      break;
    case 'j':
      ans[i] = 'u';
      break;
    case 'k':
      ans[i] = 'i';
      break;
    case 'l':
      ans[i] = 'g';
      break;
    case 'm':
      ans[i] = 'l';
      break;
    case 'n':
      ans[i] = 'b';
      break;
    case 'o':
      ans[i] = 'k';
      break;
    case 'p':
      ans[i] = 'r';
      break;
    case 'q':
      ans[i] = 'z';
      break;
    case 'r':
      ans[i] = 't';
      break;
    case 's':
      ans[i] = 'n';
      break;
    case 't':
      ans[i] = 'w';
      break;
    case 'u':
      ans[i] = 'j';
      break;
    case 'v':
      ans[i] = 'p';
      break;
    case 'w':
      ans[i] = 'f';
      break;
    case 'x':
      ans[i] = 'm';
      break;
    case 'y':
      ans[i] = 'a';
      break;
    case 'z':
      ans[i] = 'q';
      break;
    case ' ':
      ans[i] = ' ';
      break;
    default:
      ans[i] = '\0';
      return ans;
    }
  }

  return ans;
}

int main()
{
  cin >> c;
  getline(cin, g);
  for(int i=0; i<c; i++) {
//    cin >> g;
    getline(cin, g);
    string tmp = solve();
    cout << "Case #" << i+1 << ": " << tmp.substr(0, g.size()) << endl;
  }

  return 0;
}
