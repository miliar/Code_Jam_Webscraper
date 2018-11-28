#include <iostream>
#include <string>
#include <algorithm>
#include <climits>
#include <cstdlib>
using namespace std;

string solve(const string &strnum) {
  string ret(strnum);
  char used[10] = {0,0,0,0,0,0,0,0,0,0};
  int i,j;
  for (i =0; i < strnum.length(); i++)
    used[strnum[i]-'0']++;
  if (next_permutation( ret.begin(), ret.end())) {
    return ret;
  }
/*  string next = "99999999999999999999999";
  while(next_permutation(ret.begin(), ret.end())) {
    if(atoi(ret.c_str()) < atoi(next.c_str()) && atoi(ret.c_str()) > atoi(strnum.c_str())) {
      retnow = true;
      next = ret;
    }
  if (retnow)
    return next;
  }*/
  ret.clear();
  used[0]++; //We add a 0
  for (i = 1; i <= 9;i++)
    if(used[i] > 0) {
      ret.push_back(i+'0');
      used[i]--;
      break;
    }

  for (i = 0, j = '0'; i <= 9; i++, j++) {
    while (used[i] > 0) {
      ret.push_back(j);
      used[i]--;
    }
  }
  return ret;
}


int main () {
  int cases;
  cin >> cases;
  for (int c = 1; c <= cases; c++) {
    string strnum;
    cin >> strnum;
    cout << "Case #" << c << ": " << solve(strnum) << endl;
  }
  return 0;
}