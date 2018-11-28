// Daremonai
// OS: Gentoo
// Compiler version: g++ 4.3.4

#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <exception>

using namespace std;

map<string, char> combinations;
map<char, char> oppositions1;
map<char, char> oppositions2;
char list[100];
char output[100];
int outputLength = 0;

char empty = '\0';

void printCombinations() {
  map<string, char>::iterator it = combinations.begin();
  for (; it != combinations.end(); ++it) {
    printf("COMB: %s - %c\n", it->first.c_str(), it->second);
  }
}

void printOppositions() {
  map<char, char>::iterator it = oppositions1.begin();
  for (; it != oppositions1.end(); ++it)
    printf("OPP: %c - %c\n", it->first, it->second);
}


void addToOutput(char c) {
  //printf("ADD TO OUTPUT %c\n", c);
  if (outputLength == 0) {
    output[0] = c;
    //printf("adding in pos 0: %c\n", c);
    ++outputLength;
    return;
  }
  char toCheck[2];
  toCheck[0] = c;
  toCheck[1] = output[outputLength - 1];
  string check1(toCheck);
  char combResult1 = combinations[check1];
  
  if (combResult1 != empty) { //there's a combination
    output[outputLength - 1] = combinations[check1];
    //printf("CHAGING IN POSITION %d to %c\n", outputLength - 1, combinations[check1]);
    return;
  }

  toCheck[0] = output[outputLength - 1];
  toCheck[1] = c;
  string check2(toCheck);
  char combResult2 = combinations[check2];
  if (combResult2 != empty) { //there's a combination
    output[outputLength - 1] = combinations[check2];
    //printf("CHAGING IN POSITION %d to %c\n", outputLength - 1, combinations[check2]);
    return;
  }

  char cOpposition1 = oppositions1[c];

  if (cOpposition1 != empty) {
    for (int i = 0; i < outputLength; ++i) {
      if (output[i] == cOpposition1) {
        outputLength = 0;
        //printf("CLEARING LIST BECAUSE OF OPPOSITION: %c\n", cOpposition1);
        return;
      }
    }
  }

  char cOpposition2 = oppositions2[c]; 
  if (cOpposition2 != empty) {
    for (int i = 0; i < outputLength; ++i) {
      if (output[i] == cOpposition2) {
        outputLength = 0;
        //printf("CLEARING LIST BECAUSE OF OPPOSITION: %c\n", cOpposition2);
        return;
      }
    }
  }

  output[outputLength] = c;
  ++outputLength;
  //printf("APPENDING TO LIST AT POSITION %d value %c\n", outputLength -1, c);
}

void printOutput() {
  if (outputLength == 0) {
    cout << "[]\n";
    return;
  }
  cout << "[";
  for (int i = 0; i < outputLength - 1; ++i) {
    cout << output[i] << ", ";
  }
  cout << output[outputLength - 1];
  cout << "]\n";
}

int main(int argc, char **argv)
try {
  if (argc != 2) {
    cerr << "Usage: " << argv[0] << " filename" << endl;
    return -1;
  }
  ifstream input(argv[1]);
  if(!input) {
    cerr << "Could not open file " << argv[1] << endl;
    return -2;
  }
  int T = 0;
  input >> T;

  for (int i = 0; i < T; ++i) {
    int nbCombinations = 0;
    input >> nbCombinations;

    for (int cc = 0; cc < nbCombinations; ++cc) {
      char comb[3];
      input >> comb;
      char cc[2];
      cc[0] = comb[0];
      cc[1] = comb[1];
      string now(cc);
      combinations[cc] = comb[2];
      char cd[2];
      cd[0] = comb[1];
      cd[1] = comb[0];
      combinations[string(cd)] = comb[2];
    }
    //printCombinations();

    int nbOppositions = 0;
    input >> nbOppositions;
    for (int cc = 0; cc < nbOppositions; ++cc) {
      char opp[2];
      input >> opp;
      oppositions1[opp[0]] = opp[1];
      oppositions2[opp[1]] = opp[0];
    }
    //printOppositions();

    int length = 0;
    input >> length;

    input >> list;
    for (int j = 0; j < length; ++j) {
      addToOutput(list[j]);
    }

    cout << "Case #" << i + 1 << ": ";
    printOutput();

    combinations.clear();
    oppositions1.clear();
    oppositions2.clear();
    outputLength = 0;
    //printf("----------------------------------\n\n");
  }

  return 0;
}
catch (exception & e) {
  cerr << "Error: " << e.what() << endl;
  return -2;
}
catch(...) {
  cerr << "Unknown exception." << endl;
  return -3;
}
