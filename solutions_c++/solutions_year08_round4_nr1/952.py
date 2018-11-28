#include <iostream>
#include <vector>
#include <numeric>
#include <list>
#include <map>
#include <cassert>
#include <sstream>
#include <queue>
#include <set>

using namespace std;

const int MAX_M = 10000;

int changble[MAX_M];
int operation[MAX_M];
int values[MAX_M];

int min_op[2][MAX_M];

int solve(int node, int value, bool ch = true)
{
  if (values[node] != -1)
    {
      if (values[node] == value)
	{
	  min_op[value][node] = 0;
	  min_op[1 - value][node] = -2;
	}
      else
	{    
	  min_op[value][node] = -2;
	  min_op[1 - value][node] = 0;
	}
    }

  if (min_op[value][node] != -1)
    return min_op[value][node];
  
//   int l0 = solve((node+1)*2 - 1, 0);
//   int r0 = solve((node+1)*2, 0);
//   int l1 = solve((node+1)*2 - 1, 1);
//   int r1 = solve((node+1)*2, 1);

  bool chang = false;
  if (changble[node] == 1)
    {
      chang = true;
      changble[node] = 0;
    }

  int m = -2;
  
  for (int i = 0; i < 2; ++i)
    for (int j = 0; j < 2; ++j)
      {
	if (solve((node+1)*2 - 1, i) == -2)
	  continue;
	if (solve((node+1)*2, j) == -2)
	  continue;

	bool t = (operation[node] == 1) ? (i && j) : (i || j);
	int v = min_op[i][(node+1)*2 - 1] + min_op[j][(node+1)*2];
	if (t == value)
	  m = (m == -2) ? v : min (m, v);
      }

  int n = -2;
  if (chang)
    {
      operation[node] = 1 - operation[node];
      int n = solve(node, value, false);
      if (m == -2)
	m = (n == -2) ? m : n + 1;
      else if (n != -2)
	m = min(m, n + 1);
      operation[node] = 1 - operation[node];
      changble[node] = 1;
    }

  if (m == -2 && ch)
    values[node] = 1 - value;
  if (ch)
    min_op[value][node] = m;

  return m;

}

int main()
{
  int N;
  cin >> N;
  
  for (int i = 0; i < N; ++i)
    {
      memset(changble, 0, sizeof(changble));
      memset(operation, 0, sizeof(operation));
      memset(values, -1, sizeof(values));
      memset(min_op, -1, sizeof(min_op));

      int M, V;
      cin >> M >> V;

      for (int j = 0; j < (M - 1)/2; ++j)
	{
	  cin >> operation[j];
	  cin >> changble[j];
	}

      for (int j = 0; j < (M + 1)/2; ++j)
	{
	  cin >> values[j + (M - 1)/2];
	}

      int s = solve(0, V);
      if (s >= 0)
	cout << "Case #" << i + 1 << ": " << s << endl;
      else
	cout << "Case #" << i + 1 << ": IMPOSSIBLE" <<endl;
    }

  return 0;
}
