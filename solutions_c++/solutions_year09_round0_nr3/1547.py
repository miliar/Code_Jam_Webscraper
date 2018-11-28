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
  int N,s,t;
  int i,j;
  string pattern;
  cin >> N;
  getline(cin, pattern);
  const char* test = "welcome to code jam";
  //cout << strlen(test) << endl;
  int table[500][18];
  for (int c = 1; c <= N; c++) {
    getline(cin, pattern);
    char* cstr = (char*)pattern.c_str();
    int m = strlen(cstr);
    //cout << pattern << endl;

    for(j = 18; j >= 0; j--) {
      for(i = m-1; i >= 0; i--) {
	table[i][j] = 0;
	if(cstr[i] != test[j]) {
	  table[i][j] = 0;
	} else if(j == 18) {
          table[i][j] = 1; 
	} else {
	  s = 0;
	  for(int k = i+1; k < m; k++) {
	    s += table[k][j+1];
	    s %= 10000;
	  }
	  table[i][j] = s;
	}
      }
    }
    
    t = 0;
    for(i = 0; i < m; i++) {
      t += table[i][0];
      t %= 10000;
    }
    printf("Case #%d: %04d\n", c, t);
  }
}
