#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

#include <intrin.h>

struct get_maximum
{
  std::vector<std::string> queries;
  int& maximum;

  get_maximum(std::vector<std::string>::const_iterator queryBegin,
              std::vector<std::string>::const_iterator queryEnd,  
              int& maximum)
    :maximum(maximum),queries(queryBegin,queryEnd){}

  void operator()(const std::string& searchEngine)
  {
    int max=0;
    for(; max < queries.size(); ++max)
    {
      if( queries[max] == searchEngine )
      {
        break;
      }
    }
    if(max > maximum)
    {
      maximum = max;
    }
  }
};
void saving_the_universe(int caseNumber)
{
  std::vector<std::string> searchEngines;
  std::vector<std::string> queries;

  int searchEngineCount; std::cin >> searchEngineCount;
  for(int i=0; i < searchEngineCount; ++i)
  {
    searchEngines.push_back("");
    while(searchEngines.back() == "" )
    {
      std::getline(std::cin,searchEngines.back());
    }    
  }

  int queryCount; std::cin >> queryCount;
  for(int i=0; i < queryCount; ++i)
  {
    queries.push_back("");
    while(queries.back() == "" )
    {
      std::getline(std::cin,queries.back());
    }
  }

  std::vector<std::string>::const_iterator current_query = queries.begin();
  int changes = 0;
  while( current_query != queries.end() )
  {
    int maximum = 0;
    std::for_each(searchEngines.begin(),searchEngines.end(),get_maximum(current_query,queries.end(),maximum));
    current_query += maximum;
    if( current_query != queries.end())
    {
      ++changes;
    }
  }

  std::cout << "Case #" << caseNumber << ": " << changes << std::endl;


}

int main()
{
  int numberOfTestCases; std::cin >> numberOfTestCases;
  for(int testCase = 1; testCase <= numberOfTestCases; ++testCase)
  {
    saving_the_universe(testCase);
  }
}
