#include <iostream>
#include <string>
#include <vector>

using namespace std;

int Pr[20][50];
bool A[1<<17];
int con[20][20];
int B[1<<17];
int ans[1<<17];

int main ()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    cout << "Case #" << t << ": ";
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < k; j++)
      {
        cin >> Pr[i][j];
      }
    }
    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < n; j++)
      {
        con[i][j] = 1;
        for (int x = 1; x < k; x++)
        {
          int z = (Pr[i][x-1] < Pr[j][x-1]) && (Pr[i][x] < Pr[j][x]);
          z |= (Pr[i][x-1] > Pr[j][x-1]) && (Pr[i][x] > Pr[j][x]);
          con[i][j] &= z;
        }
      }
    }
    int b = 0;
    for (int x = 0; x < (1<<n); x++)
    {
      A[x] = 1;
      int z = 0;
      for (int i = 0; i < n; i++)
      {
        if (!(x & (1<<i))) continue;
        z++;
        for (int j = i+1; j < n; j++)
        {
          if (!(x & (1<<j))) continue;
          if (!con[i][j]) A[x] = 0;
        }
      }
      ans[x] = z;
      for (int i = 0; i < b; i++)
      {
        if (x | B[i] == x)
        {
          if (ans[x & (~B[i])] + 1 < ans[x])
          {
            ans[x] = ans[x & (~B[i])] + 1;
          }
        }
      }
      if (A[x] == 1)
      {
        B[b++] = x;
        ans[x] = 1;
      }
    }
    cout << ans[(1<<n)-1] << endl;
  }
  return 0;
}