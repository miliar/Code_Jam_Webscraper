#include <string>
#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
  if (argc != 2)
  {
    cerr << "Usage: " << argv[0] << " filename" << endl;
    return 1;
  }

  ifstream fin(argv[1]);

  int nCases, nEngines, nQueries, nSwitches, curQuery, maxChunk;
  string* engines, *queries;
  int i, j, k;

  fin >> nCases;

  for (i = 0; i < nCases; ++i)
  {
    fin >> nEngines;
    engines = new string[nEngines];
    fin.ignore(10, '\n');
    for (j = 0; j < nEngines; ++j)
    {
      getline(fin, engines[j]);
    }

    fin >> nQueries;
    curQuery = 0;
    nSwitches = -1;
    queries = new string[nQueries];
    fin.ignore(10, '\n');

    for (j = 0; j < nQueries; ++j)
    {
      getline(fin, queries[j]);
    }

    while (curQuery < nQueries)
    {
      maxChunk = 0;
      ++nSwitches;
      for (j = 0; j < nEngines; ++j)
      {
	for (k = curQuery; k < nQueries && queries[k] != engines[j]; ++k);
	if (k > maxChunk)
	{
	  maxChunk = k;
	  if (k == nQueries) j = nEngines;
	}
      }

      curQuery = maxChunk;
    }

    if (nSwitches == -1) nSwitches = 0;
    cout << "Case #" << i + 1 << ": " << nSwitches << endl;

    delete[] queries;
    delete[] engines;
  }
  
  fin.close();

  return 0;
}
