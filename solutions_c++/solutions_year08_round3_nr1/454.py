#include <iostream>
#include <sstream>
#include <inttypes.h>
#include <vector>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <math.h>
#include <iterator>
#include <map>
#include <cstring>

template<typename T>
std::string to_s(T v)
{
  std::stringstream s;
  s << v;
  return s.str();
}

int k[1000];
int words[1000];

int main(int argc, char** argv) {
  std::ifstream in(argv[1]);
  int numCase;
  in >> numCase;
  for(int cases = 0; cases < numCase; ++cases) {

    std::string line;
    int numP;
    in >> numP;
    int numK;
    in >> numK;
    int numW;
    in >> numW;
    
    for(int i = 0; i < numW; ++i) {
      int f;
      in >> f;
      words[i] = f; 
    }

    std::sort(&words[0], &words[numW], std::greater<int>());

    std::fill(&k[0], &k[numK], 0);

    int64_t score = 0;
    bool impossible = false;
    for(int i = 0; i < numW; ++i) {
      if(k[0] >= numP) {
	impossible = true;
	break;
      }
      ++k[0];
      score += words[i]*k[0];
      std::sort(&k[0], &k[numK]);
    }

    std::cout << "Case #" << cases+1 << ":";
    if(impossible) {
      std::cout << " IMPOSSIBLE";
    } else {
      std::cout << " " << score;
    }
    std::cout << std::endl;
  }
}
