#include <iostream>
#include <vector>
#include <limits>
#include <cstring>

using namespace std;

int cache[101][1001];

int process(int i_engine, int i_query, vector<string>& engines, vector<string>& queries)
{
  int j;
  for (j = i_query; j < queries.size(); ++j)
  {
    if (queries[j] == engines[i_engine])
      break;
  }

  if (j == queries.size())
    return 0;
  
  int min = numeric_limits<int>::max();
    
  for (int k = 0; k < engines.size(); ++k)
  {
    if (k != i_engine)
    {
      if (cache[k][j] == -1)
	cache[k][j] = process(k, j, engines, queries);

      if (min > cache[k][j])
	min = cache[k][j];
    }
  }

  return 1 + min;
}

int main()
{
  int ncase;

  cin >> ncase;

  for (int i = 0; i < ncase; ++i)
  {
    memset(cache, -1, 101 * 1001 * sizeof(int));
    int nengine;
    cin >> nengine;

    string engine;
    getline(cin, engine);

    vector<string> engines;

    for (int j = 0; j < nengine; ++j)
    {
      getline(cin, engine);
      engines.push_back(engine);
    }

    int nqueries;

    string query;
    cin >> nqueries;
    getline(cin, query);

    vector<string> queries;

    for (int j = 0; j < nqueries; ++j)
    {
      getline(cin, query);
      queries.push_back(query);
    }

    int min = process(0, 0, engines, queries);

    for (int j = 1; j < nengine; ++j)
    {
      int result = process(j, 0, engines, queries);
      if (min > result)
	min = result;
    }

    cout << "Case #" << i + 1 << ": " << min << endl;
  }

  return 0;
}
