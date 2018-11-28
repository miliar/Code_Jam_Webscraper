//
//  main.cpp
//  a
//
//  Created by Andrew Bloch on 4/13/12.
//  Copyright 2012 __MyCompanyName__. All rights reserved.
//
int verbose = 0 ;

#include <iostream>
using namespace std ;

// This is a simple string translation

char translateMap[27] = "                          ";
//char reverseMap[27] = "                          ";
char reverseMap[27] = "yhesocvxduiglbkrztnwjpfmaq";


int generateMap() {
  int testCases ;
  cin >> testCases ;
  char inputLines[testCases][101];
  char outputLines[testCases][101];
  cin.getline(inputLines[0], 101);
  int i;
  for (i=0 ; i < testCases ; i++) {
    cin.getline(inputLines[i], 101);
    cout << inputLines[i] << endl;
  }
  for (i=0 ; i < testCases ; i++) {
    cin.getline(outputLines[i], 101);
    cout << outputLines[i] << endl;
    int j ;
    for (j = 0 ; j < strlen(inputLines[i]) ; j++) {
      char ci, co;
      ci = inputLines[i][j] ;
      co = outputLines[i][j];
      if (ci != ' ') {
        translateMap[co-'a'] = ci ;
        reverseMap[ci-'a'] = co ;
      }
    }
  }
  cout << "Translate map: " << translateMap << endl ;
  cout << "Reverse map:   " << reverseMap << endl ;
  return 0 ;  
}

int main (int argc, const char * argv[])
{
  if (argc>1) {
    cout << "argc " << argc << endl ;
    generateMap();
  }
  int testCases ;
  cin >> testCases ;
  char line[101];
  if (verbose)
    cout << "Test cases: " << testCases << endl ;
  cin.getline(line,101);
  int i;
  for (i=0 ; i < testCases ; i++) {
    cout << "Case #" << i + 1 << ": " ;
    cin.getline(line,101);
    int j ;
    for (j = 0 ; j < strlen(line); j++) {
      if (line[j]==' ')
        cout << line[j] ;
      else
        cout << reverseMap[line[j]-'a'] ;
    }
    cout << endl;
  }

  
  return 0;
}

