#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>

using namespace std;

const int maxS = 100 + 10;
const int maxQ = 1000 + 10;
const int INF = 200000000;

int n, s, q;

int f[maxQ][maxS];
vector<string> query;
vector<int> idx;
map<string, int> qindex;

void
update(int value, int &p1, int &p2)
{
  if (p1 >= value)
  {
    p2 = p1;
    p1 = value;
  }
  else if (p2 > value)
  {
    p2 = value;
  }
}

int main()
{
  int p1, p2;
  string buff;
  scanf("%d\n", &n);
  for (int e = 1; e <= n; ++e)
  {
    query.clear();
    idx.clear();
    qindex.clear();
    cout << "Case #" << e << ": ";
    scanf("%d\n", &s);
    for (int i = 0; i < s; ++i)
    {
      getline(cin, buff);
      qindex[buff] = i;
    }
    scanf("%d\n", &q);
    for (int i = 0; i < q; ++i)
    {
      getline(cin, buff);
      idx.push_back(qindex[buff]);
    }
    if (q <= 0)
    {
      cout << 0 << endl;
      continue;
    }
    p1 = p2 = INF + 1;
    for (int j = 0; j < s; ++j)
    {
      f[0][j] = INF;
      if (j == idx[0])
      {
	continue;
      }
      f[0][j] = 0;
      update(f[0][j], p1, p2);
    }
    for (int i = 1; i < q; ++i)
    {
      for (int j = 0; j < s; ++j)
      {
	f[i][j] = INF;
	if (j == idx[i])
	{
	  continue;
	}
	if (f[i - 1][j] > p1)
	{
	  f[i][j] = min(p1 + 1, f[i - 1][j]);
	}
	else if (f[i - 1][j] == p1)
	{
	  f[i][j] = min(p2 + 1, f[i - 1][j]);
	}
      }
      p1 = p2 = INF + 1;
      for (int j = 0; j < s; ++j)
      {
	update(f[i][j], p1, p2);
      }
    }
    /*
    for (int i = 0; i < q; ++i)
    {
      for (int j = 0; j < s; ++j)
      {
	cout << f[i][j] << ' ';
      }
      cout << endl;
    }
    */
    cout << p1 << endl;
  }
  return 0;
}

