#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int main (int argc, char* argv[]) {

  
  
	ifstream myfile;
	cout<< "Filename "<< argv[1] << std::endl;
	myfile.open (argv[1]);
	int numTests = -1;
	string line;
	if (!myfile.is_open()) {
	  return -1;
	}
	getline (myfile,line);
	ofstream resultFile;
	resultFile.open ("result.out");
	
	
	istringstream ( line ) >> numTests;
	std::cout << "Tests " << numTests;
	int size = 0;
	
	for (int test = 0; test<numTests; ++test) {
    std::vector < std::string > tictac;
    size = 0;
    
	  getline (myfile,line);
	  
	  while (line.size()>1) {
	    std::transform(line.begin(), line.end(),line.begin(), ::toupper);
	    tictac.push_back (line);
	    getline (myfile,line);
	  }
	  
	  bool ganaX = false;
	  bool ganaO = false;
	  bool not_finished = true;
	  int countO = 0, countX = 0;
	  for (int i=0; !ganaX && !ganaO && i<tictac.size(); ++i) {
	    countO = 0, countX = 0;
	    for (int j=0; j<tictac[i].size(); ++j) {
	      if (tictac[i][j]=='X')
	        countX++;
	      if (tictac[i][j]=='O')
	        countO++;
	      if (tictac[i][j]=='T') {
	        countX++;
	        countO++;
	      }
	      if (tictac[i][j]=='.') {
	        not_finished = false;
	      }
	    }
	    if (countX==tictac.size()) {
	      ganaX = true;
	    }
	    if (countO==tictac.size()) {
	      ganaO = true;
	    }
	  }
	  for (int i=0; !ganaX && !ganaO && i<tictac.size(); ++i) {
	    countO = 0, countX = 0;
	    for (int j=0; j<tictac[i].size(); ++j) {
	      if (tictac[j][i]=='X')
	        countX++;
	      if (tictac[j][i]=='O')
	        countO++;
	      if (tictac[j][i]=='T') {
	        countX++;
	        countO++;
	      }
	    }
	    if (countX==tictac.size()) {
	      ganaX = true;
	    }
	    if (countO==tictac.size()) {
	      ganaO = true;
	    }
	  }
	  
	  countO = 0, countX = 0;
	  for (int i=0; !ganaX && !ganaO && i<tictac.size(); ++i) {
	    if (tictac[i][i]=='X')
	        countX++;
	      if (tictac[i][i]=='O')
	        countO++;
	      if (tictac[i][i]=='T') {
	        countX++;
	        countO++;
	      }
	  }
	  if (countX==tictac.size()) {
      ganaX = true;
    }
    if (countO==tictac.size()) {
      ganaO = true;
    }
    
    countO = 0, countX = 0;
	  for (int i=0; !ganaX && !ganaO && i<tictac.size(); ++i)  {
	    if (tictac[i][tictac.size()-1-i]=='X')
	        countX++;
	      if (tictac[i][tictac.size()-1-i]=='O')
	        countO++;
	      if (tictac[i][tictac.size()-1-i]=='T') {
	        countX++;
	        countO++;
	      }
	  }
	  if (countX==tictac.size()) {
      ganaX = true;
    }
    if (countO==tictac.size()) {
      ganaO = true;
    }
    
	  
	  
    resultFile << "Case #" << test+1 << ": ";
    if (ganaX)
      resultFile << "X won" << std::endl;
    else
      if (ganaO)
        resultFile<< "O won" << std::endl;
      else 
        if (!not_finished)
          resultFile << "Game has not completed" << std::endl;
        else
          resultFile << "Draw" << std::endl;
       
	}
	resultFile.close();
  myfile.close();
	return 0;
}
