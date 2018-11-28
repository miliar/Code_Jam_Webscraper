#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
int used[100], n, c, d, k, f;
char x;
string t;
vector <char> tmp;
vector <string> a, b;
int find(char c1, char c2)
{
  for(int i = 0; i < a.size(); i++)
    if ((a[i][0] == c1 && a[i][1] == c2) || (a[i][0] == c2 && a[i][1] == c1))
      return i;
  return -1;
}
bool check()
{
  for(int i = 0; i < b.size(); i++)
    if (used[b[i][0]] && used[b[i][1]])
      return 1;
  return 0;
}
int main()
{
  freopen("B-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  cin >> n;
  for(int i = 0; i < n; i++)
  {
    tmp.clear(); a.clear(); b.clear();
    for(int j = 65; j <= 90; j++) used[j] = 0;
    cin >> c;
    for(int j = 0; j < c; j++) cin >> t, a.push_back(t);
    cin >> d;
    for(int j = 0; j < d; j++) cin >> t, b.push_back(t);
    cin >> k;
    for(int j = 0; j < k; j++)
    {
      cin >> x;
      if (tmp.size())
      {
        f = find(tmp.back(), x);
        if (f != -1)
        {
          used[tmp.back()]--;
          tmp.back() = a[f][2];
        }
        else
        {
          tmp.push_back(x);
          used[x]++;
          if (check())
          {
            for(int q = 65; q <= 90; q++) used[q] = 0;
            tmp.clear();
          }
        }
      }
      else
        tmp.push_back(x), used[x]++;
    }
    cout << "Case #" << i + 1 << ": [";
    for(int j = 0; tmp.size() > 1 && j < tmp.size() - 1; j++)
      cout << tmp[j] << ", ";
    if (tmp.size()) 
      cout << tmp[tmp.size() - 1];
    cout << "]" << endl;
  }
  return 0;
}