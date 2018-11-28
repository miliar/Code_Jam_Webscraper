#include <vector>
#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string>
#include <assert.h>
#include <map>

using namespace std;


map<char, char> alph;

string Translate( const string& input ) {
  string res = input;
  for (int i = 0; i < res.length(); i++) {
    if(res[i] == ' ') continue;
    res[i] = alph[res[i]];
  }

  return res;
}

void Input(vector<string>& strs) {
  int count;
  cin >> count;
  if(count == 0) return;
  strs.resize(count);
  getline(cin, strs[0]);
  for( int i = 0; i < count; i++ ) {
    getline(cin, strs[i]);
  }
}


bool setHas(char symbol) {
  for(char c = 'a'; c <= 'z'; c++) {
    if(alph[c] == symbol) return true;
  }
  return false;
}


int main() {
  for(char c = 'a'; c <= 'z'; c++) {
    alph[c] = '-';
  }

  alph['y'] = 'a';
  alph['e'] = 'o';
  alph['q'] = 'z';

  string strings[3];
  strings[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  strings[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  strings[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

  string res[3];
  res[0] = "our language is impossible to understand";
  res[1] = "there are twenty six factorial possibilities";
  res[2] = "so it is okay if you want to just give up";

  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < strings[i].size(); j++) {
      char c = strings[i][j];
      if( c == ' ' ) continue;
      if (alph[c] != '-') {
        char symbol = alph[c];
        char symbolInRes = res[i][j];
        assert (symbol == symbolInRes);
      } else {
        alph[c] = res[i][j];
      }
    }
  }

  for(char c = 'a'; c <= 'z'; c++) {
    if (!setHas(c)) {
      alph['z'] = c;
    }
  }

  vector<string> input;
  Input( input );

  for( int i = 0; i < input.size(); i++ ) {
    cout << "Case #" << i + 1 << ": " << Translate( input[i] ) << endl;
  }

  return 0;
}