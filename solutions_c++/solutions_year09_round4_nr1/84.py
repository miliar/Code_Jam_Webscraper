#include <iostream>
#include <string>
#include <vector>

using namespace std;

char M[50][50];
int last[50];

int main ()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
    int n;
    int ans = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
      last[i] = -1;
      cin >> M[i];
      for (int j = 0; j < n; j++)
      {
        if (M[i][j] == '1')
        {
          last[i] = j;
        }
      }
    }
    for (int i = 0; i < n; i++)
    {
      int j;
      for (j = i; last[j] > i; j++);
      int x = last[j];
      ans += j-i;
      for (; j > i; j--)
      {
        last[j] = last[j-1];
      }
      last[i] = x;
    }
    cout << ans << endl;
  }
  return 0;
}