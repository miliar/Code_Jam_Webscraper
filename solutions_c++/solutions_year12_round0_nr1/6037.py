#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(int argc, char** argv){
  ifstream inputFile;
  ofstream outputFile;
  int numCases;
  char buf[200];

  //validate args
  if( argc != 2 ){
    cerr << "Usage: " << argv[0] << " filename" << endl;
    return 1;
  }

  //set up the character mapping
  char map[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

  //get the input file
  inputFile.open(argv[1]);
  if( !inputFile ){
    cerr << "Failed to open file: " << argv[1] << endl;
    return 1;
  }

  //setup the iutput file
  outputFile.open("output.txt");
  if(!outputFile){
    fprintf(stderr, "Failed to open file for output");
    return 1;
  }
  
  //get the number of test cases
  inputFile >> numCases;
  cout << "The Number of Test Cases is: " << numCases << endl;

  //read a line
  int d;
  inputFile.ignore(1, '\n');
  for(int i = 0; i < numCases; ++i){
    inputFile.getline(buf, 200);
    cout << "Line " << i+1 << ": "  << buf << endl;

    //convert the line to Googlese
    for(int j = 0; j < 100; ++j){
      if( isalpha(buf[j]) ){
	  d = buf[j] - 97;
	  buf[j] = map[d];
	}
    }

    //output the transated line
    outputFile << "Case #" << i+1 << ": " <<  buf << endl;
    
  }

  //close file
  inputFile.close();
  outputFile.close();
  return 0;
}
