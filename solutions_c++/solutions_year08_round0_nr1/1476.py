//
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

#include <set>
#include <list>
using namespace std;

typedef std::set< string > t_setNames;
typedef std::list< string > t_listQueries;

int main( int argc, char** argv )
{
  string fnIn;
  string line;

	// Set Input File Name
	fnIn = argv[1];
  ifstream myfile ( fnIn.c_str() );
  if ( ! myfile.is_open())
  {
    cout << "Unable to open file";
    return( 1);
  }

  int intNumCases;
  int intNumEngines;
  int intNumQ;
  int intSwitchCnt;
  t_setNames    setEngineNames;
  t_setNames    setUnusedNames;
  t_listQueries listQueries;
  t_setNames::iterator    itN;
  t_listQueries::iterator itQ;

  // Get NumCases
  getline (myfile,line);
  intNumCases = atoi( line.c_str());
//  cout << "NumCases: " << intNumCases << endl;

  for ( int intCaseId=1; intCaseId<=intNumCases; ++intCaseId)
  {
    // Get Num Search Engines
    getline (myfile,line);
    intNumEngines = atoi( line.c_str());

    for ( int i=0; i<intNumEngines; ++i)
    {
      getline (myfile,line);
      setEngineNames.insert( line);
    }
//    cout << "Using Engine Names:" << endl;
//    for (
//      itN  = setEngineNames.begin();
//      itN != setEngineNames.end();
//      ++itN)
//    {
//      cout << "  " << *itN << endl;
//    }

    getline (myfile,line);
    intNumQ = atoi( line.c_str());
    for ( int intQCnt=0; intQCnt<intNumQ; ++intQCnt)
    {
      getline (myfile,line);
      listQueries.push_back( line);
    }

    intSwitchCnt = 0;
    setUnusedNames = setEngineNames;
    for (
      itQ  = listQueries.begin();
      itQ != listQueries.end();
      ++itQ)
    {
      if ( setUnusedNames.count( *itQ) > 0)
      {
        setUnusedNames.erase( *itQ);
        if ( setUnusedNames.empty())
        {
          intSwitchCnt++;
          setUnusedNames = setEngineNames;
          setUnusedNames.erase( *itQ);
        }
      }
    }
    cout << "Case #" << intCaseId << ": " << intSwitchCnt << endl;
    setEngineNames.clear();
    listQueries.clear();
  }
  myfile.close();
}
