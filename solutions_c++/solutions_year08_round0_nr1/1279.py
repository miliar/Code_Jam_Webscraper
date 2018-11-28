#include <stdio.h>
#include <set>
#include <fstream>

using namespace std;

int main()
{
  ifstream input("A-large.in");
  if (input.fail())
  {
    fprintf(stderr, "Cannot open input file");
    exit(1);
  }

  uint32_t num_engines, num_cases, num_queries, switches;
  input >> num_cases;
  string line;

  for (uint32_t i = 1; i <= num_cases; i++)
  {
    switches = 0;
    input >> num_engines;
    getline(input, line);
    for (uint32_t j = 0; j < num_engines; j++)
    {
      getline(input, line);
    }

    input >> num_queries;
    getline(input, line);
    set<string> engines;
    engines.clear();

    for (uint32_t j = 0; j < num_queries; j++)
    {
      getline(input, line);
      engines.insert(line);
      if (engines.size() == num_engines)
      {
	switches++;
	engines.clear();
	engines.insert(line);
      }
    }
    fprintf(stdout, "Case #%u: %u\n", i, switches);
  }

  input.close();

  return 0;
}
