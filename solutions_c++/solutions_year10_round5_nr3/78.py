#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int move(int loc, int n, vector<pair<int,int> >& v)
{
  if (n == 0) return 0;
  if (n%2) v.push_back(make_pair(loc, n%2));
  return n/2 +
    move(loc-1, n/2, v) +
    move(loc+1, n/2, v);
}

int main()
{
  freopen("C.in", "r", stdin);
  freopen("C.out", "w", stdout);
  
	int n_cases; cin >> n_cases;
	for (int tcase = 1; tcase <= n_cases; tcase++)
	{
    int C; cin >> C;
    vector<pair<int,int> > x;
    for (int i = 0; i < C; i++)
    {
      int P, V; cin >> P >> V;
      x.push_back(make_pair(P, V));
    }
    
    sort(x.begin(), x.end());
    
    long long a = 0;
    while (true)
    {
      bool f = false;
      vector<pair<int,int> > y;
      for (int i = 0; i < x.size(); i++)
      {
        if (x[i].second > 1 && !f)
        {
          f = true;
          a += move(x[i].first, x[i].second, y);
        }
        else
          y.push_back(x[i]);
      }
      
      if (!f) break;
      
      sort(y.begin(), y.end());
      int j = 0;
      for (int i = 1; i < y.size(); i++)
        if (y[i].first == y[j].first)
        {
          y[j].second += y[i].second;
        }
        else
          y[++j] = y[i];
      y.resize(j+1);
      
      x = y;
    }
    
		printf("Case #%d: %d\n", tcase, a);
	}

	return 0;
}