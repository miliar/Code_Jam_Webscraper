#include <iostream>
#include <map>
#include <string>
#include <sstream>
using namespace std;

static map<long, map<char,long> > table;

map<char,long> calc(long ir) {
  cout << table[ir];
  std::ostringstream stm;

  stm << ir;
  string input;
  input = stm.str();
  string new_string;
  long i = 0;
  map<char,long> h;

  while (i < input.length()) {
    if (input[i] != '0') {
      new_string += input[i];
    }
    i++;
  }

  for(i=0; i < new_string.length(); i++) {
    h[new_string[i]] += 1;
  }
  table[ir] = h;

  return h;
}

int main() {
  long num_tests, in, out,i, tmp;
  cin >> num_tests;
  i = 0;
  while (i < num_tests) {
    cin >> in;
    map<char,long> orig = calc(in);
    in++;
     while (calc(in) != orig) {
       in++;
     }

  cout <<  "Case #" << i + 1 << ": " << in << endl;
    i++;
  }



}
