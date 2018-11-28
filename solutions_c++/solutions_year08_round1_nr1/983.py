#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

 bool cmp( int a, int b ) {
   return a > b;
 }   

int main(int argc, char* argv[])
{
		// No input file given
		if (argc != 2)
		   exit(0);
	    
		// file name is in argv[1]
		string file = "";
		file += argv[1];
	    
	    
		// open input file
		ifstream inFile(file.c_str());
	    
		// change .in to .out
		file = file.substr(0,file.length() - 2);
		file += "out";
	    
		// open a file for output
		ofstream outFile(file.c_str());
	    
	    
		// file must be opened
		if (!inFile)
		   exit(0);

         // get the number of cases
         int cases;
         inFile >> cases;

         int index;
         for (index = 0; index < cases; index++)
         {
             int elements = 0;
             int result = 0;
             
             inFile >> elements;
             
             vector<int> vec1(elements);
             vector<int> vec2(elements);
             
             int iter;
             for (int iter = 0; iter < elements; iter++)
             {
                 inFile >> vec1[iter];
             }
             for (int iter = 0; iter < elements; iter++)
             {
                 inFile >> vec2[iter];
             }
             
             
             sort( vec1.begin(), vec1.end() ); 
             sort( vec2.begin(), vec2.end(), cmp ); 
             
             for (int iter = 0; iter < elements; iter++)
             {
                 result += (vec1[iter] * vec2[iter]);
             }
             
             outFile << "Case #" << (index + 1) << ": " << result << endl;
             
             
         }
	    


		// cleanup
		inFile.close();
		outFile.close();
    
    return 0;
}
