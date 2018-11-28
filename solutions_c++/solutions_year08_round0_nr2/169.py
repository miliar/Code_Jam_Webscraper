#include <algorithm>
#include <cstdio>
#include <map>
#include <string>
#include <vector>

using namespace std;

#define pb push_back

int t, na, nb;
vector <int> tai, tao, tbi, tbo;

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int test = 1; test <= tn; test++)
  {
    tai.clear(), tao.clear();
    tbi.clear(), tbo.clear();
    scanf("%d", &t);
    scanf("%d%d", &na, &nb);
    for (int i = 0; i < na; i++)
    {
      int a, b, c, d;
      scanf("%d:%d %d:%d", &a, &b, &c, &d);
      tao.pb(a * 60 + b);
      tbi.pb(c * 60 + d + t);
    }
    for (int i = 0; i < nb; i++)
    {
      int a, b, c, d;
      scanf("%d:%d %d:%d", &a, &b, &c, &d);
      tbo.pb(a * 60 + b);
      tai.pb(c * 60 + d + t);
    }
    sort(tai.begin(), tai.end());
    sort(tao.begin(), tao.end());
    sort(tbi.begin(), tbi.end());
    sort(tbo.begin(), tbo.end());
    int ansa = 0, ansb = 0, i, j;
    for (i = j = 0; i < (int)tao.size(); i++)
      if (j < (int)tai.size() && tai[j] <= tao[i])
        j++;
      else
        ansa++;
    for (i = j = 0; i < (int)tbo.size(); i++)
      if (j < (int)tbi.size() && tbi[j] <= tbo[i])
        j++;
      else
        ansb++;
    printf("Case #%d: %d %d\n", test, ansa, ansb);
  }
  return 0;
}
