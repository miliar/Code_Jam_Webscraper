#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <istream>

using namespace std;

bool myFunc (int i, int j) { return (i<j); }

int main()
{
  //Read in the file
  ifstream inTest;
  inTest.open("a-small.in");
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
      inTest >> line;
      cout << "-------Test " << currTest << "-------" << endl;
      cout << "Number of vertices engines: " << line << endl;
      int numVertices = atoi(line.c_str());

      //Capture all search engines
      vector<int> xvertices;
      vector<int> yvertices;

      for(int currVertex=1; currVertex <= numVertices; currVertex++)
	{
	  inTest >> line;
	  cout << line;
	  xvertices.push_back(atoi(line.c_str()));
	}
      cout << endl;

      for(int currVertex=1; currVertex <= numVertices; currVertex++)
        {
          inTest >> line;
          yvertices.push_back(atoi(line.c_str()));
        }

      sort(xvertices.begin(), xvertices.begin() + xvertices.size(), myFunc);
      sort(yvertices.begin(), yvertices.begin() + yvertices.size(), myFunc);

      for(int i =0; i < xvertices.size(); i++)
	{
	  cout << xvertices[i] << " ";
	}
      cout << endl;

      for(int i =0; i < yvertices.size(); i++)
        {
          cout << yvertices[i] << " ";
        }
      cout << endl;

      int sum = 0;

      for(int currVertex=0; currVertex < numVertices; currVertex++)
        {
          sum += (xvertices[currVertex] * yvertices[numVertices - 1 - currVertex]);
	  cout << xvertices[currVertex] << "*" << yvertices[numVertices - currVertex] << "=" << (xvertices[currVertex] * yvertices[numVertices + 1 - currVertex]) << endl;
        }

      cout << endl << sum << endl;

      outTest << "Case #" << currTest << ": " << sum << endl;
    }
  return 0;
}
