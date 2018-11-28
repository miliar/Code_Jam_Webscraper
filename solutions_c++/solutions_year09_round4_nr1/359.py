
#include <cstring>
#include <iostream>
#include <queue>
#include <map>

using namespace std;

char m[40][40];
int s[40];

int n;

void solve(int CASE)
{
  cin >> n;  

  memset(s, 0, sizeof s);

  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
    {
      cin >> m[i][j];
      if (m[i][j] == '1')
        s[i] = j;
    }

  int steps = 0;
  for (int i = 0; i < n; i++)
    if (s[i] > i)
    {
      for (int j = i+1; j < n; j++)
        if (s[j] <= i)
        { /* swap i with j */
          while (j != i)
            std::swap(s[j-1], s[j]), j--, steps++;
          break;
        }
    }

  printf("Case #%d: %d\n", CASE, steps);
}



int main()
{
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++)
    solve(i);
  return 0;
}
