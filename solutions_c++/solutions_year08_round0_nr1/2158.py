#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>

using namespace std;

int main()
{
  //Read in the file
  ifstream inTest;
  inTest.open("A-small.in");
  string line;
  getline(inTest, line);
  int numTests = atoi(line.c_str());

  //Open file for output
  ofstream outTest;
  outTest.open("result.txt");

  cout << "Number of tests: " << numTests << endl;

  for(int currTest=1; currTest <= numTests; currTest++)
  {
    int numSwitches = 0;

    //Get number of search engines
    getline(inTest, line);
    cout << "-------Test " << currTest << "-------" << endl;
    cout << "Number of search engines: " << line << endl;
    int numEngines = atoi(line.c_str());

    //Capture all search engines
    vector<pair<string, bool> > engines;
    for(int currEngine=1; currEngine <= numEngines; currEngine++)
    {
      getline(inTest, line);
      engines.push_back(pair<string, bool> (line, false));
    }
    
    //Read in queries
    getline(inTest, line);
    int numQueries = atoi(line.c_str());
    for(int currQuery = 1; currQuery <= numQueries; currQuery++)
    {
      getline(inTest, line);

      //Check if all are true
      bool allTrue = true;
      for(int i=0; i < engines.size(); i++)
      {
	if(engines[i].first == line)
	{
	  engines[i].second = true;
	}
	if(engines[i].second == false)
	{
	  allTrue = false;
	}
      }
      if(allTrue)
      {
	for(int i=0; i< engines.size(); i++)
	{
	  engines[i].second = false;
	}
	numSwitches++;
      }
    }

    outTest << "Case #" << currTest << ": " << numSwitches << endl;
  }
  return 0;
}
