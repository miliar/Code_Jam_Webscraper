#include <iostream>
#include <cassert>

char sz[256];
bool v[2000002];

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  long long C[10][10];
  ::memset(C, 0, sizeof(C));
  for(int i = 0; i < 10; ++i)
    C[i][0] = 1;
  for(int i = 1; i < 10; ++i)
    for(int j = 1; j < 10; ++j)
      C[i][j] = C[i - 1][j - 1] + C[i - 1][j];

  int tests = 0;
  std::cin >> tests;
  for(int test = 1; test <= tests; ++test)
  {
    int A = 0;
    int B = 0;
    std::cin >> A >> B;

    ::memset(v, 0, sizeof(v));

    long long r = 0;

    for(int i = A; i <= B; ++i)
      if(!v[i])
      {
        v[i] = true;
        sprintf(sz, "%d", i);
        int n = ::strlen(sz);
        int c = 1;
        for(int j = 1; j < n; ++j)
        {
          sz[n + j - 1] = sz[j - 1];
          sz[n + j] = '\0';

          if(sz[j] != '0')
          {
            int k = ::atoi(sz + j);
            if(A <= k && k <= B && !v[k])
            {
              v[k] = true;
              ++c;
            }
          }
        }

        r += C[c][2];
      }

    std::cout << "Case #" << test << ": " << r << std::endl;
  }

  return 0;
}