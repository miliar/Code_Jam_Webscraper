#include <iostream>
#include <algorithm>

using namespace std;

int C[1000];

int main()
{
  int T,N;
  cin >> T;
  for (int t=0; t<T; t++)
    {
      cin >> N;
      int total=0;
      for (int i=0; i<N; i++)
        {
          cin >> C[i];
          total ^= C[i];
        }

      if (total!=0)
        cout << "Case #" << t+1 << ": NO" << endl;
      else
        {
          sort(C, C+N);
          int p1=C[0];
          int p2=0;
          int p2sum=0;
          for (int i=1; i<N; i++)
            {
              p2 ^= C[i];
              p2sum += C[i];
            }
          for (int i=1; i<N; i++)
            {
              if (p1 == p2)
                break;
              p1 ^= C[i];
              p2 ^= C[i];
              p2sum -= C[i];
            }

          cout << "Case #" << t+1 << ": " << p2sum << endl;
        }

    }

  return 0;
}
