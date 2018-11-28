#include <iostream>
#include <fstream>
#include <sstream>

void googlereseTranslate(std::string& str) { 
  for(int i = 0; i < str.length(); i++) { 
    switch(str[i]) { 
    case 'a': 
      str[i] = 'y'; 
      break;
    case 'b': 
      str[i] = 'h'; 
      break;
    case 'c': 
      str[i] = 'e'; 
      break;
    case 'd': 
      str[i] = 's'; 
      break;
    case 'e': 
      str[i] = 'o'; 
      break;
    case 'f': 
      str[i] = 'c'; 
      break;
    case 'g': 
      str[i] = 'v'; 
      break;
    case 'h': 
      str[i] = 'x'; 
      break;
    case 'i': 
      str[i] = 'd'; 
      break;
    case 'j': 
      str[i] = 'u'; 
      break;
    case 'k': 
      str[i] = 'i'; 
      break;
    case 'l': 
      str[i] = 'g'; 
      break;
    case 'm': 
      str[i] = 'l'; 
      break;
    case 'n': 
      str[i] = 'b'; 
      break;
    case 'o': 
      str[i] = 'k'; 
      break;
    case 'p': 
      str[i] = 'r'; 
      break;
    case 'q': 
      str[i] = 'z'; 
      break;
    case 'r': 
      str[i] = 't'; 
      break;
    case 's': 
      str[i] = 'n'; 
      break;
    case 't': 
      str[i] = 'w'; 
      break;
    case 'u': 
      str[i] = 'j'; 
      break;
    case 'v': 
      str[i] = 'p'; 
      break;
    case 'w': 
      str[i] = 'f'; 
      break;
    case 'x': 
      str[i] = 'm'; 
      break;
    case 'y': 
      str[i] = 'a'; 
      break;
    case 'z': 
      str[i] = 'q'; 
      break;
    }
  }
}

void problem1(const char* filename) { 
  std::ifstream input(filename); 
  std::string line; 
  getline(input, line); 
  std::stringstream strstr(line); 
  int numCases; 
  strstr >> numCases; 

  int caseNum = 1 ; 

  while(getline(input, line)) { 
    googlereseTranslate(line); 
    std::cout << "Case #" << caseNum << ": " << line << std::endl;
    caseNum++; 
  }  
}



void problem2(const char* filename) { 
  std::ifstream input(filename); 
  std::string line; 
  while(getline(input, line)) { 
    std::cout << line << std::endl; 
  }  
}

void problem3(const char* filename) {
  std::ifstream input(filename); 
  std::string line; 
  while(getline(input, line)) { 
    std::cout << line << std::endl;  
  }  
}

void problem4(const char* filename) { 
  std::ifstream input(filename); 
  std::string line; 
  while(getline(input, line)) { 
    std::cout << line << std::endl; 
  }  
}


int main (int argc, char* argv[])
{
  if(argc == 3) {
    switch(atoi(argv[2])) { 
    case 1:
      problem1(argv[1]);
      break;
    case 2:
      problem2(argv[1]);
      break;
    case 3:
      problem3(argv[1]); 
      break;
    case 4:
      problem4(argv[1]); 
      break;
    default:
      std::cout << "Invalid problem #! Pick a number from 1 - 4" << std::endl;
    }
  }
  
  else { 
    std::cout << "Usage: " << argv[0] << " <input filename> <problem #>" << std::endl;
  }

  return 0;
}
