#include <string>
#include <fstream>
#include <iostream>

using namespace std;
const int MAX_SERVERS = 100;
const int MAX_QUERIES = 1000;
const int MAX_NAME_LENGTH = 100;

static   ifstream input ("exo1_input");

char peek()
{
  return  input.peek();
}

int pos()
{
  return input.tellg();
}


int solve_case(string* servers, int nb_servers, string* queries, int nb_queries);


int main(int, char*)
{
  int nb_cases;
  int nb_servers;
  int nb_queries;
  string  servers[MAX_SERVERS];
  string  queries[MAX_QUERIES];

  input >> nb_cases;

=>for (int c = 0; c < nb_cases; ++c)
  {
    input >> nb_servers;
    input.get(); // termine la lecture de la ligne, sinon la prochaine ligne lu est vide
    for (int s = 0; s < nb_servers; ++s)
      getline(input, servers[s]);
    input >> nb_queries;
    input.get(); // idem
    for (int q = 0; q < nb_queries; ++q)
      getline(input, queries[q]);

    cout << "Case #" << (c+1) << ": " << solve_case(servers, nb_servers, queries, nb_queries) << endl;
  }

  input.close();

  return 0;
}

////////// RESOLUTION


int solve_case(string* servers, int nb_servers, string* queries, int nb_queries)
{
  // OPTIMIZATIONS : transforms all names in integers
  int* qs = new int[nb_queries];

  for (int q = 0; q < nb_queries; ++q)
  {
    int s = -1;
    while (++s < nb_servers)
      if (queries[q] == servers[s])
      {
        qs[q] = s;
        break;
      }

    if (s == nb_servers)
      qs[q] = nb_servers; // won't implode any server :) So qe associate this query to an arbitrary value
  }

  int res = 0;
  int count = 0;
  int* counts = new int[nb_servers + 1];

  for (int s = 0; s < nb_servers; ++s)
    counts[s] = 0;

  for (int q = 0; q < nb_queries; ++q)
  {
    if (counts[qs[q]] == 0 && qs[q] < nb_servers)
      ++count;
    ++counts[qs[q]];

    if (count == nb_servers)
    {
      res++;
      for (int s = 0; s < nb_servers; ++s)
        counts[s] = 0;
      count = 0;
      --q;
    }
  }

  delete[] qs;
  delete[] counts;

  return res;
}
