#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int main(void)
{
  int C; cin >> C;
  for (int c = 1; c <= C; c++) {
    printf("Case #%d: ", c);
    string str;
    cin >> str;
    vector <char> chars;
    bool found = false;
    str = '0' + str;
    for (int i = str.length()-1; i > 0; i--) {
      chars.push_back(str[i]);
      if (str[i] > str[i-1]) {
	if (i > 1)
	  cout << str.substr(1, i-2);
	chars.push_back(str[i-1]);
	sort(chars.begin(), chars.end());
	for (int j = 0; j < chars.size(); j++)
	  if (chars[j] > str[i-1]) {
	    cout << chars[j];
	    chars.erase(chars.begin() + j);
	    break;
	  }
	for (int j = 0; j < chars.size(); j++)
	  cout << chars[j];
	found = true;
	break;
      }
    }
    printf("\n");
  }
  return 0;
}
