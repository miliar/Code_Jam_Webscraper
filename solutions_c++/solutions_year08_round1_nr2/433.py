
#include <iostream>
#include <vector>

using namespace std;

int Ones(int x)
{
  int count = 0;
  while (x != 0)
  {
    x &= (x - 1);
    ++count;
  }
  return count;
}

int main()
{
  int C;
  cin >> C;
  for (int c = 1; c <= C; ++c)
  {
    int N, M;
    cin >> N;
    cin >> M;
    vector<int> fav0(M), fav1(M);
    for (int m = 0; m < M; ++m)
    {
      int T;
      cin >> T;
      for (int t = 1; t <= T; ++t)
      {
        int x, y;
        cin >> x >> y;
        if (y == 0)
          fav0[m] |= 1 << (x - 1);
        else
          fav1[m] |= 1 << (x - 1);
      }
    }

    int best_q = -1;
    int best_ones = 0;
    int limit = 1 << N;
    for (int q = 0; q < limit; ++q)
    {
      bool all_fav = true;
      for (int m = 0; m < M; ++m)
      {
        if (!((fav1[m] & q) || (fav0[m] & (~q))))
        {
          all_fav = false;
          break;
        }
      }
      if (all_fav)
      {
        int ones = Ones(q);
        if ((best_q < 0) || (ones < best_ones))
          best_q = q, best_ones = ones;
      }
    }

    cout << "Case #" << c << ":";
    if (best_q < 0)
      cout << " IMPOSSIBLE";
    else
    {
      for (int i = 0; i < N; ++i)
        cout << " " << ((best_q >> i) & 1);
    }
    cout << endl;
  }
  return 0;
}
