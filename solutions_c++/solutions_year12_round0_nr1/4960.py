#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
//#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

char replace(char c, const char* g, const char* n) {
  for (int i = 0; i<27; ++i)
    if (g[i] == c)
      return n[i];

  cout<<"BUGGER: " << c <<endl;

  return '#';
}

int main() {

  const char* google = "abcdefghijklmnopqrstuvwxyz ";
  const char* normal = "yhesocvxduiglbkrztnwjpfmaq ";

  

  int num_inputs;
  scanf( "%d\n", &num_inputs );
  for (int i = 0; i<num_inputs; ++i) {
    char* inp = new char[100];
    int len = 0;
    while (1) {
      char c;
      scanf( "%c", &c);
      if (c == '\n') break;
      inp[len++] = c;
    }

    char* out = new char[len+1];
    for (int j = 0; j < len; ++j) {
      out[j] = replace(inp[j], google, normal);
    }
    out[len] = '\0';
    int casenum = i+1;
    cout << "Case #" << casenum << ": " << out << endl;
  }

}

