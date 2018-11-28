#include <iostream>
#include <string>
#include <iterator>
#include <algorithm>
#include <vector>
#include <iomanip>
#include <functional>

using namespace std;
typedef vector<int> vi_t;
typedef vector<vi_t> mat_t;

int main()
{
  int N; cin >> N; cin.ignore();
  string patt = "welcome to code jam";
  const size_t pl = patt.size();
  for (int n = 1; n <= N; ++n)
  {
    string t;
    getline(cin, t);
    mat_t mat(t.size(), vi_t(pl, 0));
    if (t[0] == 'w') mat[0][0] = 1;
    for (size_t i = 1; i < t.size(); ++i)
    {
      copy(mat[i-1].begin(), mat[i-1].end(), mat[i].begin());
        for (size_t j = 0; j < pl; ++j)
        {
          if (patt[j] == t[i])
          {
            if (j >= 1)
             mat[i][j] += mat[i-1][j-1];
            else
              ++mat[i][j];
            mat[i][j] %= 10000;
          }
        }
    }
    cout << "Case #" << n << ": ";
    cout.width(4);
    cout.fill('0');
    cout <<  mat[t.size() - 1][pl-1] << endl;
  }
  return 0;
}