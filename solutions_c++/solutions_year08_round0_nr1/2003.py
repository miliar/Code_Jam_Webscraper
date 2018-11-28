#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

/* Save the Universe */

class Router {
  private:
    vector<string> engines;
    vector<string> querries;
  public:
    Router() {}
    ~Router () {}
    void ReadInputs(ifstream&);
    int getMinSwitches(void) const;
    void printEngines (void) const;
    void printQuerries (void) const;
    int getMaxDistance(string, int) const;

};

void Router::printEngines(void) const 
{
  cout << "Engines: " << endl;
  vector<string>::const_iterator itx = engines.begin();
  vector<string>::const_iterator itx_end = engines.end();
  for(; itx != itx_end; ++itx) {
    cout << *itx << endl;
  }
}

void Router::printQuerries(void) const 
{
  cout << "Querries: " << endl;
  vector<string>::const_iterator itx = querries.begin();
  vector<string>::const_iterator itx_end = querries.end();
  for(; itx != itx_end; ++itx) {
    cout << *itx << endl;
  }
}

int Router::getMaxDistance(string currentQ, int currentIdx) const
{
  map<string, int> dist;

  for(unsigned int j = 0; j < engines.size(); ++j) {
    if(engines[j] == currentQ) {
      continue;
    }
    for(unsigned int k = currentIdx+1; k < querries.size(); ++k) {
      if(engines[j] == querries[k]) {
        string temp = engines[j];
        dist[temp] = (k - currentIdx);
        break;
      }
    }
  }

  if(dist.size() < (engines.size()-1)) {
    return (querries.size() + 1);
  }
 
  int max = 0; 
  map<string, int>::iterator itx = dist.begin();
  map<string, int>::iterator itx_end = dist.end();
  
  for(; itx != itx_end; ++itx) {
    int current = itx->second; 
    if(current > max) {
      max = current;
    }
  }
  return max;
}

int Router::getMinSwitches(void) const 
{
  /* Better approach */
  int switches = 0;
  int i = 0;
  int qMax = querries.size();
  while (i < qMax) {
    if((i != (qMax-1)) && querries[i] == querries[i+1]) {
      ++i;
      continue;
    }
    unsigned int max = getMaxDistance (querries[i], i);
    if(max > querries.size()) { // max distance i.e. one of the search engines in missing in the querries
      return switches;
    }
    i += max;
    ++switches;
  }

  return switches; 
}

void Router::ReadInputs(ifstream& fstr) 
{
  char numOfEngines[5];
  fstr.getline(numOfEngines, 4);
  int Eg = atoi(numOfEngines);
  /* Read the engines' names */
  for(int se = 0; se < Eg; ++se) {
    char engineName[101];
    fstr.getline(engineName, 100);
    engines.push_back(engineName);
  }

  char numOfQs[5];
  fstr.getline(numOfQs, 4);
  int Qs = atoi(numOfQs);
    /* Read the querries */
  for(int q = 0; q < Qs; ++q) {
    char querry[101];
    fstr.getline(querry, 100);
    querries.push_back(querry);
  }
}

int main(int argc, char** argv)
{
  if(argc != 2) {
    cout << "Error! Usage: <binary_name> <input_file>" << endl;
    exit(-1);
  }
  
  /* Read the Input file */
  ifstream fstr(argv[1], fstream::in);
  
  char numOfTCs[5];
  fstr.getline(numOfTCs, 4);
  int NC = atoi(numOfTCs);
  /* Read all the test cases */
  for(int x = 1; x <= NC; ++x) {
    Router rx;
    rx.ReadInputs(fstr);
    cout << "Case #" << x << ": " << rx.getMinSwitches() << endl;
  }

  return 0;
}
