#include <iostream>
#include <string>
#include <algorithm>
#include <climits>
#include <cstdlib>
using namespace std;

int solve(const string &strnum) {
  const char ass[] = "1023456789abcdefghijklmnopqrstuvwxyz";
  int dest[256];
  string res(strnum);
  for (int i = 0; i <256; i++) {
    dest[i]=0;
  }
  int base = 0;
  for (int i = 0; i < strnum.length(); i++) {
    if (dest[strnum[i]] == 0) {
      dest[strnum[i]]=ass[base];
      base++;
    }
    res[i]=dest[strnum[i]];
  }
  return strtol(res.c_str(),NULL,max(2,base));
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