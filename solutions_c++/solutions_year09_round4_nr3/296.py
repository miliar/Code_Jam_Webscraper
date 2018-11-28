#include <iostream>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

const int NO_EDGE = -(1<<30);

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen)
{
  if (seen[i])
    return false;
  seen[i] = true;
  for (int j = 0; j < w[i].size(); j++)
    if (w[i][j] != NO_EDGE && mc[j] < 0)
      {
	mr[i] = j;
	mc[j] = i;
	return true;
      }
  for (int j = 0; j < w[i].size(); j++)
    if (w[i][j] != NO_EDGE && mr[i] != j)
      if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen))
	{
	  mr[i] = j;
	  mc[j] = i;
	  return true;
	}
  return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc)
{
  mr = VI(w.size(), -1);
  mc = VI(w[0].size(), -1);
  VI seen(w.size());

  int ct = 0;
  for (int i = 0; i < w.size(); i++)
    {
      fill(seen.begin(), seen.end(), 0);
      if (FindMatch(i, w, mr, mc, seen)) ct++;
    }
  return ct;
}

int T, n, k;
VVI price;

int solve()
{
  cin >> n >> k;
  price.resize(n);
  for (int i = 0; i < n; i++)
    {
      price[i].resize(k);
      for (int j = 0; j < k; j++) cin >> price[i][j];
    }
  VVI w(n);
  for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
      {
	int value = 1;
	for (int d = 0; d < k; d++)
	  if (price[i][d] >= price[j][d])
	    {
	      value = NO_EDGE;
	      break;
	    }
	w[i].push_back(value);
      }
  VI mr, mc;
  return n - BipartiteMatching(w, mr, mc);
}

int main()
{
  cin >> T;
  for (int i = 0; i < T; i++)
    cout << "Case #" << i+1 << ": " << solve() << endl;
  return 0;
}
