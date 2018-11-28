#include <iostream>
#include <fstream>
#include <list>
#include <sstream>
#include <string>

#include <libgen.h>
#include <stdlib.h>
#include <unistd.h>

using namespace std;

string getExecutablePath() {
  char buffer[BUFSIZ] = {0};
  readlink("/proc/self/exe", buffer, BUFSIZ);
  return dirname(buffer);
}

string getOutputFilename(string inputFilename) {
  size_t pos = inputFilename.find(".");
  return inputFilename.substr(0, pos);
}

int main(int argc, char **argv) {
  int lineCount = 0;
  int caseTotal = 0;
  int caseCount = 0;

  string inputFile = argv[1];
  ifstream inFile (inputFile.c_str());

  string inputFileName = basename((char*)inputFile.c_str());
  string outputFile = getExecutablePath() + "/../output/" + getOutputFilename(inputFileName) + ".out";
  ofstream outFile (outputFile.c_str());

  if (inFile.is_open()) {
    while (inFile.good()) {
      int numGooglers = 0;    // N
      int numSurprising = 0;  // S
      int minResult = 0;      // p
      list<int> totalPoints;  // N
      int numGooglersWithMinResult = 0; // y

      string line;
      getline (inFile, line);
      lineCount++;
      if (lineCount == 1) {
        caseTotal = atoi(line.c_str());
        continue;
      }

      if (caseCount < caseTotal) {
        int count = 0;
        string word;
        istringstream iss(line, istringstream::in);
        while(iss >> word) {
          int tmpNum = atoi(word.c_str());

          switch (count) {
            case 0:
              numGooglers = tmpNum;
              break;
            case 1:
              numSurprising = tmpNum;
              break;
            case 2:
              minResult = tmpNum;
              break;
            default:
              totalPoints.push_back(tmpNum);
              break;
          }

          count++;
        }

        for (list<int>::iterator it = totalPoints.begin(); it != totalPoints.end(); it++) {
          int num = *it;
          int result = num / 3;
          int remainer = num % 3;

          if (result >= minResult) {
            numGooglersWithMinResult++;
          }
          else {
            if (num != 0) {
              if (remainer == 0) {
                if (numSurprising > 0 && (result + 1 >= minResult)) {
                  numGooglersWithMinResult++;
                  numSurprising--;
                }
              }
              else {
                if (result + 1 >= minResult) {
                  numGooglersWithMinResult++;
                }
                else if (remainer == 2) {
                  if (numSurprising > 0 && (result + 2 >= minResult)) {
                    numGooglersWithMinResult++;
                    numSurprising--;
                  }
                }
              }
            }
          }
        }

        outFile  << "Case #" << caseCount+1 << ": " << numGooglersWithMinResult << endl;
        caseCount++;
      }
      else {
        break;
      }
    }

    inFile.close();
    outFile.close();
  }

  return 0;
}

