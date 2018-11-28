#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <string.h>
#include <vector>
int main (int argc, char** argv) {
  std::string line;
  std::ifstream inputFile("A-small-attempt2.in");
  char* ptrString = 0;
  getline(inputFile, line);
  short unsigned int numCases = atoi(line.c_str());
  unsigned int N = 0, K = 0;

  std::cout << numCases << "\n";
  unsigned int caseNum = 0;
  while (getline(inputFile, line)) {
    ptrString = strtok(const_cast<char*>(line.c_str()), " ");
    N = atoi(ptrString);
    ptrString = strtok(NULL, " ");
    K = atoi(ptrString);
    //std::cout << N << "," << K << "\n";
    std::vector<bool> State(N, 0);
    std::vector<bool> RecvPow(N, 0);
    RecvPow[0] = true;
    unsigned int i = 0;
    while (K) {
      i = 0;
      while (RecvPow[i] && (i < N)) {
        State[i] = State[i] ? false : true;
	++i;
      }
      i = 0;
      while (RecvPow[i] && State[i] && (i < N-1)) {
        ++i;
        RecvPow[i] = true;
      }
      ++i;
      while (i < N) {
        RecvPow[i] = false;
        ++i;
      }
      --K;
    }
      std::cout << "Case #" << ++caseNum << ": ";
    if (State[N-1] && RecvPow[N-1])
      std::cout << "ON\n";
    else
      std::cout << "OFF\n";



  }
}
