#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

class LongVal {
  static const int len = 51;
  short vals[len];
public:
  LongVal() {
    for (int i=0;i<len;i++)
      vals[i] = 0;
  }
  LongVal(std::string str) {
    for (int i=0;i<str.size();i++) 
      vals[i] = str[str.size()-1-i] - '0';
    for (int i=str.size();i<len;i++)
      vals[i] = 0;
  }
  LongVal(const LongVal &val) {
    for (int i=0;i<len;i++) 
      vals[i] = val.vals[i];
  }
  LongVal operator-(const LongVal &val) {
    short rest = 0;
    LongVal result;
    for (int i=0;i<len;i++) {
      short diff = vals[i] - val.vals[i] - rest;
      if (diff<0) {
	diff += 10;
	rest = 1;
      } else
	rest = 0;
      result.vals[i] = diff;
    }
    return result;
  }
  LongVal rest(const LongVal &val) {
    int cnt = 0;
    LongVal rest = *this;
    while (!(rest<val)) {
      rest = rest - val;
      cnt++;
    }
    return rest;
  }
  bool isZero() {
    bool zero = true;
    for (int i=0;i<len;i++)
      zero &= (vals[i] == 0);
    return zero;
  }
  friend bool operator<(const LongVal &val1, const LongVal &val2) {
    short rest = 0;
    for (int i=0;i<len;i++) {
      short diff = val1.vals[i] - val2.vals[i] - rest;
      if (diff<0) 
	rest = 1;
      else
	rest = 0;
    }
    return (bool)rest;
  }
  friend std::ostream &operator<<(std::ostream &os, LongVal &val) {
    int i = len-1;
    if (val.isZero()) {
      os << "0";
      return os;
    }
    while (!val.vals[i] && i>=0)
      i--;
    for (;i>=0;i--) 
      os << val.vals[i];
    return os;
  }
};

main(int argc, char *argv[])
{
  std::ifstream infile(argv[1]);
  int C, N;
  infile >> C;
  for (int i=0;i<C;i++) {
    infile >> N;
    std::vector<LongVal> t(N);
    std::string tj;
    for (int j=0;j<N;j++) {
      infile >> tj;
      t[j] = tj;
    }
    std::sort(t.begin(), t.end());
    std::vector<LongVal> d(N-1);
    for (int j=0;j<N-1;j++) 
      d[j] = t[j+1] - t[j];
    std::sort(d.begin(), d.end());
    for (int j=0;j<d.size();j++) {
      if (d[j].isZero()) {
	for (int k=j;k<d.size()-1;k++)
	  d[k] = d[k+1]; 
	j--;
	d.pop_back();
      }
    }
    //for (int j=0;j<d.size();j++) 
    //  std::cout << "d: " << d[j] << std::endl;
    LongVal b = d[0];
    for (int j=1;j<d.size();j++) {
      LongVal a = d[j];
      LongVal r = a.rest(b);
      while (!r.isZero()) {
	a = b;
	b = r;
	r = a.rest(b);
      }
    }
    LongVal r = t[N-1].rest(b);
    LongVal y = b - r;	 
    if (r.isZero())
      y = r;
    std::cout << "Case #" << (i+1) << ": " << y << std::endl;
  }
}
