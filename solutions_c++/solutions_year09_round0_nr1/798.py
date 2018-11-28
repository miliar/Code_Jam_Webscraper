#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <set>

using namespace std;
typedef vector<string> ss_t;

int main()
{
  int L, D, N;
  cin >> L >> D >> N; cin.ignore();
  string s;
  ss_t dic(D);
  for (int i = 0; i < D; ++i)
  {
    cin >> dic[i]; cin.ignore();
    assert(dic[i].size() == L);
  }
  for (int n = 1; n <= N; ++n)
  {
    ss_t patt(L);
    for (int pos = 0; pos < L; ++pos)
    {
      char c;
      cin >> c;
      if (c == '(')
      {
        cin >> c;
        while (c != ')')
        {
          patt[pos].push_back(c);
          cin >> c;
        }
      }
      else
      {
        patt[pos].push_back(c);
      }
    }
    int K = 0;
    for (int w = 0; w < D; ++w)
    {
      bool matched = true;
      for (int l = 0; l < L; ++l)
      {
        if (patt[l].find(dic[w][l]) == string::npos)
        {
          matched = false;
          break;
        }
      }
      if (matched) ++K;
    }
    cout << "Case #" << n << ": " << K << endl;
  }
  return 0;
}