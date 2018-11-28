#include <cassert>
#include <cmath>
#include <cctype>
#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <vector>
#include <set>
#include <iomanip>
#include <functional>

using namespace std;
typedef vector<int> vi_t;
typedef vector<string> vs_t;
typedef unsigned long long i64_t;

int main()
{
  int N; cin >> N; cin.ignore();

  for (int n = 1; n <= N; ++n)
  {
    string num;
    cin >> num;
    set<int> sc;
    copy(num.begin(), num.end(), inserter(sc, sc.begin()));
    size_t base = sc.size();
    if (base == 1) base = 2;
    string out(num.size(), '\t');
     char nd = '1';
     char fr = num[0];
    for (size_t j = 0; j < num.size(); ++j)
    {
      if (num[j] == fr) 
      {
        out[j] = '1';
        num[j] = '\t';
      }
    }
    nd = '0';
    for (size_t s = 1; s < num.size(); ++s)
    {
      if (num[s] == '\t') continue;
      char fr = num[s];
      for (size_t i = s; i < num.size(); ++i)
      {
        if (num[i] == fr) 
        {
          out[i] = nd;
          num[i] = '\t';
        }
      }
      if (nd == '0') nd = '2';
      else ++nd;
    }
    string res;
    i64_t r = 0;
    for (size_t i = 0; i < out.size(); ++i)
    {
      r *= base;
      r += out[i] - '0';
    }
    cout << "Case #" << n << ": " << r << endl;
  }
  return 0;
}
