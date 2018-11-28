#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>

using namespace std;

typedef char searchName_t[101];
searchName_t input;
searchName_t searchEngines[103];
searchName_t queries[1003];
int queryAsInt[1003];
bool queriedEngine[103];

int  numberCases;
int  numberEngines;
int  numberQueries;
int  numSwitch;
ifstream inFile;
ofstream outFile;

bool allSearched(void) {
  int count;
  for (count = 0; count < numberEngines; count++) {
    if (queriedEngine[count] == false) {
      return false;
    }
  }
  return true;
}

void resetSearch(void) {
  int count;
  for (count = 0; count < numberEngines; count++) {
    queriedEngine[count] = false;
  }
}

void translateToInts(void) {
  int count;
  int engCount;

  for (count = 0; count < numberQueries; count++) {
    // Current query is queries[count].  Find in searchEngines.
    for (engCount = 0; engCount < numberEngines; engCount++) {
      if (strcmp(queries[count], searchEngines[engCount]) == 0) {
        queryAsInt[count] = engCount;
        //cout << engCount << endl;
        break;
      }
    }
  }
}

void runCase(void) {
  int count; 
  int currentSearch;
  numSwitch = 0;

  memset (searchEngines, 0, sizeof( searchEngines ));
  memset (queries, 0, sizeof( queries ));
  inFile >> numberEngines;
  inFile.getline(input, sizeof(input));
  //cout << numberEngines << endl;

  for (count = 0; count < numberEngines; count++) {
    inFile.getline(input, sizeof(input));
    strcpy(searchEngines[count], input);
    //cout << input << endl;
  }

  inFile >> numberQueries;
  inFile.getline(input, sizeof(input));
  //cout << numberQueries << endl;
  for (count = 0; count < numberQueries; count++) {
    inFile.getline(input, sizeof(input));
    strcpy(queries[count], input);
    //cout << input << endl;
  }

  translateToInts();
  resetSearch();

  for (currentSearch = 0; currentSearch < numberQueries; currentSearch++) {
    queriedEngine[queryAsInt[currentSearch]] = true;
    if (allSearched()) {
      //cout << "AS at " << currentSearch << endl;
      numSwitch++;
      resetSearch();
      queriedEngine[queryAsInt[currentSearch]] = true;
    }
  }
}

int main(int argc, char **argv) {
  inFile.open(argv[1]);
  outFile.open("output");

  // First line N
  inFile >> numberCases;
  //cout << numberCases << endl;

  for (int i = 0; i < numberCases; i++) {
    runCase();
    cout << "Case #" << i+1 << ": " << numSwitch << endl;
    outFile << "Case #" << i+1 << ": " << numSwitch << endl;
  }

  inFile.close();
  outFile.close();
}
