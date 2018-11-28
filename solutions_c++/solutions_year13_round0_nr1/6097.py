// AUTHOR: Ray Powers
// DATE: April 12, 2013
// PLATFORM: C++98

// Description: The purpose of this program is to evaluate the progress of a tic-tac-toe-tomek game.


#include<iostream>
#include<fstream>
#include<string>
#include<queue>
#include<algorithm>

using namespace std;

// Data Structure
struct testCase {
  string values[4];
};

string processGame(const testCase game);
// Function evaluates a game based on several conditions.
// pre: none
// post: none


int main (int argNum, char * argValues[]) {

  // Locals
  testCase tmpCase;
  string tmp;
  int numOfLines = 0;
  queue<testCase> testCases;

  // Need to obtain test data.
  // Read in File Contents
  string filename = argValues[1];
  ifstream srcFile;
  srcFile.open(filename.c_str());
  if (srcFile.fail()) {
    return -1;
  }  

  // File was opened. Proceed to read in contents.
  if (srcFile.is_open()) {
    srcFile >> numOfLines;
    numOfLines += 1;
    // Store the rest of the data.
    for (int i = 1; i < numOfLines; i++) {
      srcFile >> tmpCase.values[0];
      srcFile >> tmpCase.values[1];
      srcFile >> tmpCase.values[2];
      srcFile >> tmpCase.values[3];

      testCases.push(tmpCase);
      /*cout << tmpCase.values[0] << endl;
      cout << tmpCase.values[1] << endl;
      cout << tmpCase.values[2] << endl;
      cout << tmpCase.values[3] << endl;
      cout << endl;//*/
    }
    
  }
  srcFile.close();
  srcFile.clear();

  // Process 
  for (int i = 1; i < numOfLines; i++) {
    tmpCase = testCases.front();
    testCases.pop();
    cout << "Case #" << i << ": " << processGame(tmpCase) << endl;
  }

  return 0;
}

string processGame( testCase game) {

  // Locals
  const string XWIN = "X won";
  const string OWIN = "O won";
  const string DRAW = "Draw";
  const string INCP = "Game has not completed";
  const int numGrid = 4;
  string answer = "No Solution.";
  int count[numGrid]; // 0=X, 1=O, 2=., 3=T
  for (int i = 0; i < 4; i++) {
    count[i] = 0;
  }
  bool hasAnswer = false;
  bool isComplete = true;

  // Evaluate rows
  for (int i = 0; i < numGrid; i++) {
    for (int k = 0; k < 4; k++) {
      count[k] = 0;
    }
    string tmpStr = game.values[i];
    for (int j = 0; j < numGrid; j++) {
      if (tmpStr[j] == 'X') {
	count[0] += 1;
      } else if (tmpStr[j] == 'O') {
	count[1] += 1;
      } else if (tmpStr[j] == 'T') {
	count[3] += 1;
      } else if (tmpStr[j] == '.') {
	count[2] += 1;
	isComplete = false;
      }
    }
    // Check For win condition
    if (count[0] == 4 || (count[0] == 3 && count[3] == 1)) {
      hasAnswer = true;
      answer = XWIN;
      break;
    } else if (count[1] == 4 ||  (count[1] == 3 && count[3] == 1)) {
      hasAnswer = true;
      answer = OWIN;
      break;
    }
  }

  // Evaluate Columns
  if (!hasAnswer) {
    for (int i = 0; i < numGrid; i++) {
      for (int k = 0; k < 4; k++) {
	count[k] = 0;
      }
      for (int j = 0; j < numGrid; j++) {
	if ((game.values[j])[i] == 'X') {
	  count[0] += 1;
	} else if ((game.values[j])[i] == 'O') {
	  count[1] += 1;
	} else if ((game.values[j])[i] == 'T') {
	  count[3] += 1;
	} else if ((game.values[j])[i] == '.') {
	  count[2] += 1;
	  isComplete = false;
	}
      }

    
      // Check For win condition
      if (count[0] == 4 || (count[0] == 3 && count[3] == 1)) {
	hasAnswer = true;
	answer = XWIN;
	break;
      } else if (count[1] == 4 ||  (count[1] == 3 && count[3] == 1)) {
	hasAnswer = true;
	answer = OWIN;
	break;
      } 
    }
  }

  // Evaluate the Diagnals
  if (!hasAnswer) {
    for (int k = 0; k < 4; k++) {
      count[k] = 0;
    }
    // Top left to bottom right
    for (int i = 0; i < numGrid; i++) {
      if ((game.values[i])[i] == 'X') {
	count[0] += 1;
      } else if ((game.values[i])[i] == 'O') {
	count[1] += 1;
      } else if ((game.values[i])[i] == 'T') {
	count[3] += 1;
      } else if ((game.values[i])[i] == '.') {
	count[2] += 1;
	isComplete = false;
      }
    }
    
    // Check For win condition
    if (count[0] == 4 || (count[0] == 3 && count[3] == 1)) {
      hasAnswer = true;
      answer = XWIN;
    } else if (count[1] == 4 ||  (count[1] == 3 && count[3] == 1)) {
      hasAnswer = true;
      answer = OWIN;
    } 

    if (!hasAnswer) {
      for (int k = 0; k < 4; k++) {
	count[k] = 0;
      }
      // Top left to bottom right
      for (int i = 3; i >= 0; i--) {
	if ((game.values[3-i])[i] == 'X') {
	  count[0] += 1;
	} else if ((game.values[3-i])[i] == 'O') {
	  count[1] += 1;
	} else if ((game.values[3-i])[i] == 'T') {
	  count[3] += 1;
	} else if ((game.values[3-i])[i] == '.') {
	  count[2] += 1;
	  isComplete = false;
	}
      }
      //cout << "Number of O's:" << count[1] << " and num of Ts" << count[3] << endl;
      // Check For win condition
      if (count[0] == 4 || (count[0] == 3 && count[3] == 1)) {
	hasAnswer = true;
	answer = XWIN;
      } else if (count[1] == 4 ||  (count[1] == 3 && count[3] == 1)) {
	hasAnswer = true;
	answer = OWIN;
      } 
    }
  }

  if (!hasAnswer) {
    // Test Draw or incomplete
    if (!isComplete) {
      // incomplete
      answer = INCP;
    } else {
      answer = DRAW;
    }
  }
  return answer;
}
