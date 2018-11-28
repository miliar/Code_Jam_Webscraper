#include <iostream>
#include <iomanip>
#include <cstring>

#define uint unsigned long long
#define MAX_LINE 512

using namespace std;

class HugeNumber {
  uint lo;
  uint hi;
public:
  HugeNumber() : lo(0), hi(0) {}
  HugeNumber(uint x) : lo(x), hi(0) {}

  HugeNumber operator + (const HugeNumber & rgt) const {
    HugeNumber result;
    result.lo = rgt.lo + lo;
    result.hi = rgt.hi + hi;

    if(result.lo < rgt.lo || result.lo < lo)
      ++result.hi;
    return result;
  }

  HugeNumber operator = (const HugeNumber &rgt) {
    lo = rgt.lo;
    hi = rgt.hi;
    return *this;
  }

  HugeNumber operator = (const uint rgt) {
    lo = rgt;
    hi = 0;
    return *this;
  }

  HugeNumber operator += (const HugeNumber & rgt) {
    lo += rgt.lo;
    hi += rgt.hi;
    if(lo < rgt.lo) ++hi;
    return *this;
  }

  HugeNumber operator += (const uint rgt) {
    lo += rgt;
    if( lo < rgt ) ++hi;
    return *this;
  }

  friend ostream& operator << (ostream & s, const HugeNumber & hn) {
    //s << setfill('0') << setw(20) << hn.hi << setw(20) << hn.lo;
    s << setfill('0') << setw(4) << hn.lo;
    return s;
  }
};

uint N; // Numer of cases.
char text[] = "welcome to code jam";

HugeNumber count_welcomes(char * pos, uint chr){
  if(text[chr] == '\0') return HugeNumber(1);
  else if(*pos == '\0') return HugeNumber(0);

  HugeNumber cases(0);
  while( (pos = strchr(pos, text[chr])) != NULL ) {
    cases += count_welcomes(++pos, chr+1);
  }
  return cases;
}

int main() {
  cin >> N;
  cin.get();
  for(uint c = 1; c <= N; ++c) {
    char line[MAX_LINE];
    cin.getline(line, MAX_LINE);
    
    cout << "Case #" << c << ": " << count_welcomes(line, 0) << endl;
  }

  return 0;
}
