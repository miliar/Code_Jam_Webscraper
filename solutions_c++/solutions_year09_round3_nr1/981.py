#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>

// C libraries
#include <cstring>
#include <cstdlib>
#include <cmath>

#define uint unsigned long long int
#define REP_LU(i, s, e) for(uint (i) = (s); (i) <  (e); ++(i))
#define REP_EU(i, s, e) for(uint (i) = (s); (i) <= (e); ++(i))
#define REP_GD(i, s, e) for(uint (i) = (s); (i) >  (e); --(i))
#define REP_ED(i, s, e) for(uint (i) = (s); (i) >= (e); --(i))

using namespace std;

#define MAX_NUM  65

map<char, uint> alphabet;
char num[MAX_NUM];
uint value[MAX_NUM];

uint next_value(uint prev_value) {
  if(prev_value == 1)  return 0;
  if(prev_value == 0)  return 2;
  return prev_value+1;
}

uint read_num() {
  uint d = 1;
  
  char c = cin.get();
  uint prev_value = 1;
  alphabet[c] = value[0] = prev_value;
  num[0] = c;

  do {
    c = cin.get();
    if( isspace(c) ) break;

    num[d] = c;
    map<char, uint>::iterator it = alphabet.find(c);
    if( it == alphabet.end() ){
      prev_value = next_value(prev_value);
      alphabet[c] = value[d] = prev_value;
    } else {
      value[d] = it->second;
    }

    ++d;
  } while ( 1 );

  return d;
}

void calc(uint digits, uint base) {
  uint res = 0;
  if(base == 1) ++base;
  REP_LU(d, 0, digits) {
    uint prev = res;
    res += value[d] * pow(base, digits - d - 1);
    if(res < prev) {
      cerr << "OVERFLOW!" << endl; exit(-1);
    }
  }
  cout << res;
}

int main() {
  uint Cases;
  cin >> Cases; cin.get();

  REP_EU(c, 1, Cases) {
    memset(num, '0', sizeof(char) * MAX_NUM);
    memset(value, 0, sizeof(uint) * MAX_NUM);

    // Read data
    uint digits = read_num();
    num[digits] = '\0';
    cout << "Case #" << c << ": ";
    // Solve problem
    calc(digits, alphabet.size());
    cout << endl;
    alphabet.clear();
  }
}
