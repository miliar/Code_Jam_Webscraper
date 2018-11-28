
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <map>

using namespace std;

int getint(istream &in)
{
  string line;
  getline(in, line);
  stringstream ss(line);
  int x;
  ss >> x;
  return x;
}

int main()
{
  int N = getint(cin);
  for (int n = 0; n < N; ++n)
  {
    int S = getint(cin);
    vector<string> engines(S);
    map<string, int> engine_index;
    for (int s = 0; s < S; ++s)
    {
      getline(cin, engines[s]);
      engine_index[engines[s]] = s;
    }

    int Q = getint(cin);
    vector< set<int> > x(S);
    for (int q = 0; q < Q; ++q)
    {
      string engine;
      getline(cin, engine);
      int s = engine_index[engine];
      x[s].insert(q);
    }

    int result = 0;
    if (Q > 0)
    {
      int pos = 0;
      while (pos < Q)
      {
        int max_pos = pos;
        for (int s = 0; s < S; ++s)
        {
          set<int>::iterator find = x[s].lower_bound(pos);
          if (find == x[s].end())
            max_pos = Q;
          else
            max_pos = max(max_pos, *find);
        }
        pos = max_pos;
        ++result;
      }
      --result;
    }
    cout << "Case #" << (n + 1) << ": " << result << endl;
  }

  return 0;
}
