
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include <map>

using namespace std ;

int main(const int argc, char * argv[])
{



  cerr << argv[1] << endl ;
  
  ifstream inputFile(argv[1]) ;
  if( inputFile.is_open())
    {

      int numTests ;
      inputFile >> numTests ;
      cerr << "Number of tests: " << numTests << endl ;

      for ( int i = 0 ; i < numTests ; ++i)
	{
	  int A, B ;

	  inputFile >> A ;
	  inputFile >> B ;

	  //cout << i << "A: " << A << " B: " << B << endl ;
	  
	  stringstream aSS, bSS ;
	  aSS << A ;
	  bSS << B ;

	  string aString, bString ;
	  aString = aSS.str() ;
	  bString = bSS.str() ;

	  int intLen= aString.length() ;
	  map<string,int> myMap ;

	  cerr << i << "A: " << aString << " B: " << bString << endl ;
	  for(int a = A ; a < B; ++a)
	    {
	      stringstream nSS ;
	      nSS << a ;
	      string n = nSS.str() ;

	      for(int b = a+1; b <= B; ++b)
		{
		  stringstream mSS ;
		  mSS << b ;
		  string m = mSS.str() ;

		  string lastString = n ;
		  for(int z = 0; z < intLen-1 ; ++z)
		    {
		      lastString = lastString.substr(intLen-1,1).append(lastString.substr(0,intLen-1)) ;
		      //cerr << "lastString " << lastString << endl ;
		      if(lastString == m)
			{
			  myMap[n+m] = 1 ;
			}

		    }
		  
		}
	    }
	  cout << "Case #" << i+1 << ": " << myMap.size() << endl ;
	}

      inputFile.close() ;
      
    }


}
