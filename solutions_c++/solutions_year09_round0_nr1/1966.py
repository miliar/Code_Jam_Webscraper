#include <boost/regex.hpp>
#include <iostream>
#include <string>

using namespace std;

int main(void) {
  int L, D, N;
  cin >> L >> D >> N;
  string w[D], reg;
  size_t pos;
  for(int i = 0; i < D; ++i)
    cin >> w[i];
  for(int i = 1; i <= N; ++i) {
    int count = 0;
    cin >> reg;

    while((pos = reg.find("(")) != reg.npos)
      reg.replace(pos, 1, "[");
    while((pos = reg.find(")")) != reg.npos)
      reg.replace(pos, 1, "]{1}");

    boost::regex pat(reg);

    for(int d = 0; d < D; ++d)
      if(boost::regex_match(w[d], pat))
	++count;

    printf("Case #%i: %i\n", i, count);
  }
}
