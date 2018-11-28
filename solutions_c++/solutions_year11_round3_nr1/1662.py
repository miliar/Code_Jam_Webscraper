
#include <cstdio>
#include <fstream>
#include <sstream>
#include <vector>


void HandleCase(std::ifstream &myfile, int caseIndex)
{
  std::string line;
  getline(myfile, line);
  std::stringstream ss(line);
  int rows, cols;
  ss >> rows;
  ss >> cols;

  int numWhite = 0;
  char **grid = new char*[rows];
  for (int i=0; i<rows; i++) {
    grid[i] = new char[cols];
    getline(myfile, line);
    for (int j=0; j<cols; j++) {
      grid[i][j] = line[j];
      if (line[j] == '#')
        numWhite++;
    }
  }

  for (int i=0; i<rows-1; i++) {
    for (int j=0; j<cols-1; j++) {
      if (grid[i][j] == '#' && grid[i][j+1] == '#' &&
          grid[i+1][j] == '#' && grid[i+1][j+1] == '#') {
        grid[i][j] = '/';
        grid[i][j+1] = '\\';
        grid[i+1][j] = '\\';
        grid[i+1][j+1] = '/';
        numWhite -= 4;
      }
    }
  }
  
  printf("Case #%d:\n", caseIndex);
  if (numWhite > 0) {
    printf("Impossible\n");
  }
  else {
    for (int i=0; i<rows; i++) {
      for (int j=0; j<cols; j++) {
        printf("%c", grid[i][j]);
      }
      printf("\n");
    }
  }

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
