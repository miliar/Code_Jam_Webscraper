	#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std ; 

typedef map< char , char > dict ; 


int main (int argc , char **argv)
{
	dict mydictionary ;
	mydictionary ['a'] = 'y' ; 
	mydictionary ['b'] = 'h' ; 
	mydictionary ['c'] = 'e' ; 
	mydictionary ['d'] = 's' ; 
	mydictionary ['e'] = 'o' ; 
	mydictionary ['f'] = 'c' ; 
	mydictionary ['g'] = 'v' ; 
	mydictionary ['h'] = 'x' ; 
	mydictionary ['i'] = 'd' ; 
	mydictionary ['j'] = 'u' ; 
	mydictionary ['k'] = 'i' ; 
	mydictionary ['l'] = 'g' ; 
	mydictionary ['m'] = 'l' ; 
	mydictionary ['n'] = 'b' ; 
	mydictionary ['o'] = 'k' ; 
	mydictionary ['p'] = 'r' ; 
	mydictionary ['q'] = 'z' ; 
	mydictionary ['r'] = 't' ; 
	mydictionary ['s'] = 'n' ; 
	mydictionary ['t'] = 'w' ; 
	mydictionary ['u'] = 'j' ; 
	mydictionary ['v'] = 'p' ; 
	mydictionary ['w'] = 'f' ; 
	mydictionary ['x'] = 'm' ; 
	mydictionary ['y'] = 'a' ; 
	mydictionary ['z'] = 'q' ; 

	 string line = "" ; 
	 string out = ""; 
	 ifstream myfile ("A-small-attempt0.in");
     ofstream fileout ("outputfile.txt");


	if(myfile.is_open())
	{
		getline (myfile,line);
		int counter = 0 ; 
		while (myfile.good())
		{
	      counter ++ ; 
		  out = "" ;
		  line = "" ; 
		  getline (myfile,line);

		  for(int i = 0 ; i < line.length() ; i ++ )
		  {
		    out += mydictionary[line[i]];
		  }
		  
		  char buffer [100] ; 
		  string cnt = itoa(counter ,buffer , 10 ) ; 
		  cout << ("Case #" + cnt + ": " + out + "\n" ); 
		  fileout  << ("Case #" + cnt + ": " + out + "\n" );
		}
	}



	return 0 ;
}