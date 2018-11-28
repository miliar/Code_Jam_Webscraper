#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
char a[100][100];
string s;
int k, n, m;
bool yes(int i, int j)
{
  return 0 <= i && i < n && 0 <= j && j < m;
}
bool check(int i, int j)
{
  return yes(i + 1, j + 1) && a[i][j] == '#' && a[i + 1][j] == '#' && a[i][j + 1] == '#' && a[i + 1][j + 1] == '#';
}
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  cin >> k;
  for(int c = 0; c < k; c++)
  {
    cin >> n >> m;
    for(int i = 0; i < n; i++)
    {
      cin >> s;
      for(int j = 0; j < m; j++)
        a[i][j] = s[j];
    }
    for(int i = 0; i < n; i++)
      for(int j = 0; j < m; j++)
        if (check(i, j))
        {
          a[i][j] = '/';
          a[i][j + 1] = '\\';
          a[i + 1][j] = '\\';
          a[i + 1][j + 1] = '/';
        }
    bool flag = false;
    for(int i = 0; i < n; i++)
      for(int j = 0; j < m; j++)
        if (a[i][j] == '#')
          flag = true;
    printf("Case #%d:\n", c + 1);
    if (flag)
      cout << "Impossible" << endl;
    else
    {
      for(int i = 0; i < n; printf("\n"), i++)
        for(int j = 0; j < m; j++)
          cout << a[i][j];
    }
  }
  return 0;
}