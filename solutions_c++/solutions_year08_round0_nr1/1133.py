#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using std::ifstream;
using std::ofstream;
using std::string;
using std::cout;
using std::endl;
using std::vector;
using std::count;
using std::cerr;


int farthest(vector<string> engines, vector<string> queries, int start)
{
    vector<string>::iterator farthestDistance = find((queries.begin() + start), queries.end(), engines[0]);
    int farthestIndex = 0;
    
    int index;
    for (index = 1; index < engines.size(); index++)
    {
        vector<string>::iterator  location = find((queries.begin()+ start), queries.end(), engines[index]);
        if (location == engines.end())
        {
           farthestIndex = index;
        }
        if (location > farthestDistance)
        {
                     farthestDistance = location;
                     farthestIndex = index;
        }
    }
    
    return farthestIndex;
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
             // read in the number of search engines
             int engineCount;
             inFile >> engineCount;
             
             // This will hold the search engine strings
             vector<string> engines(engineCount, "");
             
             // since the line feed is still left in there
             // take it out since I am using getline
             inFile.ignore();
             
             // move the next engineCount strings into the string vector
             int engineIndex;
             for (engineIndex = 0; engineIndex < engineCount; engineIndex++)
             {
                 getline(inFile, engines[engineIndex]);
             }

             
             // read in the number of queries
             int queryCount;
             inFile >> queryCount;
             
             // This will hold the query strings
             vector<string> queries(queryCount, "");
             
             // since the line feed is still left in there
             // take it out since I am using getline
             inFile.ignore();
             
             //move the next queryCount strings into the query vector
             int queryIndex;
             for (queryIndex = 0; queryIndex < queryCount; queryIndex++)
             {
                 getline(inFile, queries[queryIndex]);
             }
             

             int switches = 0;
             
             // find the engine used the farthest away 
             int currentSEIndex = farthest(engines, queries, 0);
             string currentSE = engines[currentSEIndex];
             
             
             for (queryIndex = 0; queryIndex < queryCount; queryIndex++)
             {
                 
                 
                 // if we need to switch the engine, increment switches and set currentSE
                 // to the search engine with the next lowest amount of queries to 
                 // besides the one currently in use
                 if (!queries[queryIndex].compare(currentSE))
                 {
                      switches++;
                      currentSEIndex = farthest(engines, queries, queryIndex);
                      currentSE = engines[currentSEIndex];
                 }
             }
             
             outFile << "Case #" << (index + 1) << ": " << switches << endl;
             
             
         }
	    


		// cleanup
		inFile.close();
		outFile.close();
    
    return 0;
}
