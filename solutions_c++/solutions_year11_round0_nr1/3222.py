#include <iostream>
using namespace std;
int x, n, k, to, p1, p2, t, t1, t2;
char r;
int ab(int x)
{
  return (x < 0) ? -x : x;
}
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  cin >> n;
  for(int i = 0; i < n; i++)
  {
    cin >> k;
    p1 = p2 = 1;
    t = t1 = t2 = 0;
    for(int j = 0; j < k; j++)
    {
      cin >> r >> to;
      if (r == 'O')
      {
        x = ab(p1 - to) + 1, p1 = to;
        t1 = max(t + 1, t1 + x), t = max(t1, t);
      }
      else
      {
        x = ab(p2 - to) + 1, p2 = to;
        t2 = max(t + 1, t2 + x), t = max(t2, t);
      }
    }
    cout << "Case #" << i + 1 << ": " << t << endl;
  }
  return 0;
}