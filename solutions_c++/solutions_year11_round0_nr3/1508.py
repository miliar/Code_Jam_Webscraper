
#include <cstdio>
#include <fstream>
#include <sstream>
#include <vector>


void HandleCase(std::ifstream &myfile, int caseIndex)
{
  const int MAXBITS = 20;
  int numBits[20];
  for (int i=0; i<MAXBITS; i++)
    numBits[i] = 0;

  int smallestCandy = 0;
  int totalCandy = 0;

  std::string line;
  getline(myfile, line);
  std::stringstream ss(line);

  int numCandies;
  ss >> numCandies;

  getline(myfile, line);
  std::stringstream ss2(line);
  std::vector<int> candies(numCandies);
  for (int i=0; i<numCandies; i++) {
    int candy;
    ss2 >> candy;

    totalCandy += candy;
    if (i == 0 || candy < smallestCandy)
      smallestCandy = candy;

    for (int j=0; j<MAXBITS; j++) {
      if ((1 << j) & candy)
        numBits[j]++;
    }
  }

  printf("Case #%d: ", caseIndex);
  for (int i=0; i<MAXBITS; i++) {
    if (numBits[i]%2 != 0) {
      printf("NO\n");
      return;
    }
  }
  printf("%d\n", totalCandy-smallestCandy);
}


int main(int argc, char** argv)
{
  std::string line;
  std::ifstream myfile(argv[1]);
  
  getline(myfile, line);
  std::stringstream ss(line);

  int numCases;
  ss >> numCases;

  for (int i=0; i<numCases; i++) {
    HandleCase(myfile, i+1);
  }
}
