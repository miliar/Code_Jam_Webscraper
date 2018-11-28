#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <sstream>
using namespace std;
typedef long long ll;

char gog[] = "yhesocvxduiglbkrztnwjpfmaq";


void infer() {
  char mp[26] = {};

  int T;
  scanf(" %d ", &T);
  for (int ii = 0; ii < T; ++ii) {
    char buf1[100], buf2[100];
    fgets(buf1, 100, stdin);
    fgets(buf2, 100, stdin);
    for (int i = 0; buf1[i] != '\0'; ++i) {
      if (isalpha(buf1[i])) {
	mp[buf1[i] - 'a'] = buf2[i];
      }
    }
  }

  for (int i = 0; i < 26; ++i) {
    if (mp[i] == 0) {
      printf("\n");
    } else {
      printf("%c", mp[i]);
    }
  }
    
}


int main() {
  //infer();

  int T;
  cin >> T >> ws;

  for (int ii = 0; ii < T; ii++) {
    string s;
    getline(cin, s);
    printf("Case #%d: ", ii+1);
    for (int i = 0; i < s.size(); ++i) {
      if (s[i] != ' ') cout << gog[s[i] - 'a'];
      else cout << ' ';
    }
    cout << endl;
  }
}
