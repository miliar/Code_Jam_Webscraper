#include <cstdio>
#include <set>
#include <vector>
using namespace std;

int licz(bool *siedzi, int p, vector<int> &tor)
{
  bool ok = true;

  for(int i=0;i<tor.size();++i)
    if(tor[i] != -1)
      ok = false;

  if(ok)
    return 0;

  int res = 2000000000;

  for(int k=0;k<tor.size();++k)
    if(tor[k] != -1)
    {
      int t = tor[k];
      tor[k] = -1;

      int s = t - 1;
      int points = 0;
      while(s >= 0 && siedzi[s] != false)
      {
        ++points;
        --s;
      }
      s = t + 1;
      while(s < p && siedzi[s] != false)
      {
        ++points;
        ++s;
      }

      siedzi[t] = false;

      int tmp = points + licz(siedzi, p, tor);
      if(tmp < res)
        res = tmp;

      tor[k] = t;

      siedzi[t] = true;

    }

  return res;
}

void fun(int casenr)
{
  int p, q;
  scanf("%d%d", &p, &q);
  vector<int> torelease;
  for(int i=0;i<q;++i)
  {
    int tmp;
    scanf("%d", &tmp);
    torelease.push_back(tmp-1);
  }

  bool * tmp = new bool[p];
  for(int i=0;i<p;++i)
    tmp[i] = true;

  printf("Case #%d: %d\n", casenr, licz(tmp, p, torelease));

  delete [] tmp;
}

int main()
{
  int t;
  scanf("%d", &t);
  for(int i=1;i<=t;++i)
    fun(i);

  return 0;
}

