#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

int solveDance(int n, int s, int p, std::vector<int>& scoreList) { 
  int numSurprising = 0; //only has best score P if it is surprising
  int numNormal = 0;     //has best score P without being surprising
  
  for(int i = 0; i < n; i++) { 
    int score = scoreList[i]; 
    int triple = 3 * p; 
    
    if(score == 0) { 
      if(p == 0) { 
	numNormal++;
      }
    }
    else if(triple <= score) { 
      numNormal++;
    }
    else { 
      int remainder = triple - score; 
      if(remainder <= 2) { 
	numNormal++;
      }
      else if(remainder <= 4) { 
	numSurprising++;
      }
    }
  }
  
  return numNormal + ((numSurprising > s) ? s : numSurprising); 
}

void dance(const char* filename) {   
  std::ifstream input(filename); 
  std::string line; 
  getline(input, line); 
  std::stringstream strstr(line); 
  int numCases; 
  strstr >> numCases; 

  int caseNum = 1 ; 

  while(getline(input, line)) { 
    std::stringstream lineStr(line); 
    int n, s, p, t; 
    std::vector<int> scoreList;

    lineStr >> n >> s >> p; 
    
    for(int i = 0; i < n; i++) { 
      lineStr >> t; 
      scoreList.push_back(t); 
    }
    
    std::cout << "Case #" << caseNum << ": " << solveDance(n, s, p, scoreList) << std::endl;
    caseNum++; 
  }  
}


int main (int argc, char* argv[])
{
  if(argc == 2) {
    dance(argv[1]); 
  }
  
  else { 
    std::cout << "Usage: " << argv[0] << " <input filename>" << std::endl;
  }

  return 0;
}
