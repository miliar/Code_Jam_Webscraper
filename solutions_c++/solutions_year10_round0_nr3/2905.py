#include <iostream>
#include <deque>

using namespace std;

int main()
{
  int T = 0;
  cin >> T;
  
  for(int i = 0; i < T; ++i)
  {
    unsigned R = 0;
    cin >> R;
    unsigned k = 0;
    cin >> k;
    unsigned N = 0;
    cin >> N;

    deque<unsigned> q;

    for(unsigned j = 0; j < N; ++j)
    {
      unsigned g = 0;
      cin >> g;
      q.push_back(g);
    }

    __int64 res = 0;
    for(unsigned j = 0; j < R; ++j)
    {
      unsigned loaded = 0;
      unsigned groups_loaded = 0;
      while(groups_loaded < N && loaded + q.front() <= k)
      {
        loaded += q.front();
        ++groups_loaded;
        q.push_back(q.front());
        q.pop_front();
      }

      res += loaded;
    }

    cout << "Case #" << (i + 1) << ": " << res << endl;
  }
  
  return 0;
}

