#include <iostream>
#include <fstream>
#include <string>
#include <cctype>


using namespace std;

/*******************************************************/
/* Input file is given as a command line argument e.g  */
/*                                                     */
/* program.exe input.txt                               */
/*******************************************************/

int main(int argc, char *argv[]) {
    
    string fileName = ""; 
    
    const int MAXL = 15;
    const int MAXD = 5000;
    const int MAXN = 500;
    
    int L, //maximum L for current test case between 1 and 15
        D, //maximum D for current test case between 1 and 5000
        N; //maximum N for current test case between 1 and 500
        
    string words[MAXD];//Allocate space to holds the maximum possible number of words in the language
    string patterns[MAXN];//Allocate space to hold the maximum possible number of patterns
    
    //Holds start and end indices of the search blocks
    int startSearchIndices[MAXL];
    int endSearchIndices[MAXL];
    
    /*Get file name containing input from file */
    if(argv[1] != NULL) {
        fileName = string(argv[1]);        
    }
    else {
        cout << "Usage: <program executable> <inputFileName>\n";
        return 0;
    }
    
    /*Open the file and read the input*/
    fstream inputFile;    
    inputFile.open(fileName.c_str(), fstream::in);
    if(inputFile.fail() == true) {
       std::cout << "Failed to open the input file: \"" << fileName << "\"\n";
	   return 0;
    }
    
    //Read input
    inputFile >> L >> D >> N;
    for(int i = 0; i < D; i++) {
       inputFile >> words[i];
    }
    for(int i = 0; i < N; i++) {
       inputFile >> patterns[i];
    }
   
    inputFile.close();//close file
        
    //Loop through patterns in each test case and check how many words the pattern matches
    for(int n = 0; n < N; n++) {
    
            int numOfMatches = 0;
            
            //Generate search blocks for current pattern
            int patternLength = patterns[n].length();
            for(int j = 0, i = 0; j < L; j++) {                    
                  
                  if( patterns[n].at(i) == '(' ) {
                      
                      startSearchIndices[j] = i + 1;                      
                      i = i + 2;

                      while(patterns[n].at(i) != ')') {
                          i++;
                      }
                      
                      endSearchIndices[j] = i - 1;
                      
                      i++;
                  }
                  else {
                       
                       startSearchIndices[j] = endSearchIndices[j] = i;
                       
                       i++;
                  }
            }
            
            //Search the number of words current pattern can generate
            for(int d = 0; d < D; d++) {
                    
                    bool searchFailed = false;

                    for(int i = 0; i < L; i++) {
                            
                            //get search block for this index
                            int searchLength = endSearchIndices[i] - startSearchIndices[i] + 1; 
                            string stringToSearch = patterns[n].substr(startSearchIndices[i], searchLength);
                            
                            //perform search
                            if(stringToSearch.find(words[d].at(i)) == string::npos) {   
                               searchFailed = true;
                               break;
                            }
                            
                    }
                    
                    if(!searchFailed)
                       numOfMatches++;                    
            }
            
            //Print number of matches for this pattern
            std::cout << "Case #" << n + 1 << ": " << numOfMatches << '\n'; 
    }
    return 0;
}



