#include <iostream>
#include <fstream>
#include <map>
#include <set>
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

int countRecycledPairs(int num, int endNum) {
  map<int, set<int> > numMap;
  stringstream ss;
  string numStr;
  string tmpNumStr;
  int count = 0;

  ss << num;
  numStr = ss.str();
  tmpNumStr = numStr;

  for (unsigned int i = 0; i < numStr.length(); i++) {
    int tmpNum;
    
    tmpNumStr.append(1, tmpNumStr[0]);
    tmpNumStr.erase(0, 1);

    // ignore numbers with leading 0
    if (tmpNumStr[0] != '0') {
      tmpNum = atoi(tmpNumStr.c_str());
      
      // ignore same number
      if ((num != tmpNum) && (tmpNum <= endNum)) {
        numMap[num].insert(tmpNum);
      }
    }
  }

  for (map<int, set<int> >::iterator itm = numMap.begin(); itm != numMap.end(); itm++) {
    set<int> numSet = (*itm).second;

    for (set<int>::iterator its = numSet.begin(); its != numSet.end(); its++) {
      if ((*itm).first < (*its)) {
        count++;
      }
    }
  }

  return count;
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
      string line;
      getline (inFile, line);
      lineCount++;
      if (lineCount == 1) {
        caseTotal = atoi(line.c_str());
        continue;
      }

      if (caseCount < caseTotal) {
        string startNumStr;
        int startNum = 0;
        string endNumStr;
        int endNum = 0;
        int numRecycledPairs = 0;

        int count = 0;
        string word;
        istringstream iss(line, istringstream::in);
        while(iss >> word) {
          int tmpNum = atoi(word.c_str());

          switch (count) {
            case 0:
              startNumStr = word;
              startNum = tmpNum;
              break;
            case 1:
              endNumStr = word;
              endNum = tmpNum;
              break;
          }

          count++;
        }

        if (startNumStr.length() > 1) {
          for (int i = startNum; i <= endNum; i++) {
            numRecycledPairs += countRecycledPairs(i, endNum);
          }
        }
        outFile  << "Case #" << caseCount+1 << ": " << numRecycledPairs << endl;
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

