#include<cstdio>
#include<map>
#include<set>
#include<vector>
#include<algorithm>

using namespace std;

typedef pair<int, int> pii;
typedef multiset<pii> mspii;
typedef vector<pii> vpii;
typedef long long ll;
typedef unsigned int uint;

ll sumk2[100001];

ll next_step(mspii &v)
{
  mspii::iterator it, itn = v.begin(); itn++;
  for (it = v.begin() ; itn != v.end(); it++, itn++)
    {
      if (it->first + it->second > itn->first)
	{
	  int a1 = it->first;
	  int l1 = it->second;
	  int a2 = itn->first;
	  int l2 = itn->second;
	  v.erase(it);
	  v.erase(itn);
	  ll d = (a2 - a1 + 1)*(a1 + l1 - a2);
	  if (l2 > 1)
	    v.insert(pii(a2+1, l2-1));
	  v.insert(pii(a1-1, a1+l1-a2));
	  v.insert(pii(a1+a1+l1-a2, a2-a1+1));
	  return d;
	}
    }
  return 0;
}

bool finished(vpii &v)
{
  for (uint i = 1 ; i < v.size() ; i++)
    if (v[i - 1].first + v[i - 1].second > v[i].first)
      return false;
  return true;
}

int main()
{
  for (ll i = 1 ; i <= 100000 ; i++)
    sumk2[i] = sumk2[i-1] + i*i;

  int T;
  scanf("%d", &T);
  for (int t = 1 ; t <= T ; t++)
    {
      mspii w;
      ll res = 0;
      int C;
      scanf("%d", &C);
      for (int i = 0 ; i < C ; i++)
	{
	  int p, v;
	  scanf("%d%d", &p, &v);
	  res += sumk2[v/2];
	  if (v & 1)
	    w.insert(pii(p - v/2, v));
	  else
	    {
	      w.insert(pii(p - v/2, v/2));
	      w.insert(pii(p+1, v/2));
	    }
	}
      ll d;
      while(1)
	{
	  d = next_step(w);
	  if (!d)
	    break;
	  res += d;
	}
      printf("Case #%d: %lld\n", t, res);
    }
}
