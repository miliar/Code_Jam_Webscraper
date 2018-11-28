#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

string s;
long x;

bool backtrack(int i) {
  for(;(i<s.size())&&(s[i]!='?');i++);
  //std::cerr << "backtrack(" << i << ")\n";
  if(i>=s.size()){
    long y = sqrt(x);
    //std::cerr << y*y << "?=" << x << '\n';
    return y*y == x;
  }

  s[i]='0';
  if(backtrack(i+1)) return true;
  s[i]='1';
  x+= (1L << i);
  if(backtrack(i+1)) return true;
  x-= (1L << i);
  s[i]='?';
  return false;
}


int main() {
  int t;
  cin >> t;

  //cout.precision(std::numeric_limits< double >::digits10);
  //cout << sizeof(long) << ' ' << sizeof(int) << ' ' << sizeof(long long) << '\n';

  for(int tcase=1;tcase<=t;tcase++){
    cin >> s;
    reverse(s.begin(), s.end());
    x=0;
    for(long i=0,j=1;i<s.size();i++,(j<<=1))
      if(s[i]=='1') x+=j;
    cerr << backtrack(0) << '\n';
    reverse(s.begin(), s.end());
    cout << "Case #" << tcase << ": " << s << '\n';
  }
}
