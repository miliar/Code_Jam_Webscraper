//
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

#include <set>
#include <list>
#include <algorithm>
using namespace std;

// The first line of the input file contains integer number T - the number of test cases.
// For each test case, the first line contains integer number n.
// The next two lines contain n integers each, giving the coordinates of v1 and v2 respectively.

typedef std::multiset< int > t_setValues;
typedef t_setValues::iterator t_setIt;

int main( int argc, char** argv )
{
  string fnIn;
  string line;
  int    subIndex;
  string subString;

	// Set Input File Name
	fnIn = argv[1];
  ifstream myfile ( fnIn.c_str() );
  if ( ! myfile.is_open())
  {
    cout << "Unable to open file";
    return( 1);
  }

  int intNumCases;
  int intNumValues;
  t_setValues    setV1;
  t_setValues    setV2;

  // Get NumCases
  getline (myfile,line);
  intNumCases = atoi( line.c_str());
//  cout << "NumCases: " << intNumCases << endl;

  for ( int intCaseId=1; intCaseId<=intNumCases; ++intCaseId)
  {
    // Get Num Values
    getline (myfile,line);
    intNumValues = atoi( line.c_str());
//  cout << "NumValues: " << intNumValues << endl;

    getline (myfile,line);
    for ( int i=0; i<intNumValues; ++i)
    {
      subIndex = line.find(" ");
      if ( subIndex != string::npos)
        subString = line.substr(0,subIndex+1);
      else
        subString = line;
//      cout << "V1: " << atoi(subString.c_str()) << endl;
      setV1.insert( atoi(subString.c_str()));
      line.erase(0,subIndex+1);
    }
    getline (myfile,line);
    for ( int i=0; i<intNumValues; ++i)
    {
      subIndex = line.find(" ");
      if ( subIndex != string::npos)
        subString = line.substr(0,subIndex+1);
      else
        subString = line;
//      cout << "V2: " << atoi(subString.c_str()) << endl;
      setV2.insert( atoi(subString.c_str()));
      line.erase(0,subIndex+1);
    }

    t_setIt itV1;
    t_setIt itV2;
    int ScalarProduct = 0;
    for ( int i=0; i<intNumValues; ++i)
    {
      itV1 = min_element( setV1.begin(), setV1.end());
      itV2 = min_element( setV2.begin(), setV2.end());
      if ( *itV1 <= *itV2 )
      {
        itV2 = max_element( setV2.begin(), setV2.end());
      }
      else
      {
        itV1 = max_element( setV1.begin(), setV1.end());
      }
      ScalarProduct += *itV1 * *itV2;
      setV1.erase( itV1);
      setV2.erase( itV2);
    }
    cout << "Case #" << intCaseId << ": " << ScalarProduct << endl;
    setV1.clear();
    setV2.clear();
  }
  myfile.close();
}
