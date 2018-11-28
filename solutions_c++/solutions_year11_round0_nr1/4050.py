#include <iostream>
#include <string>
#include <sstream>
#include <vector> 


using std::cin;
using std::cout;
using std::endl;

using std::string;
using std::vector;


const int MAX_SEQLEN = 100;
const int ORANGE = 3;
const int BLUE = 4;


void Parse(string &parameters, vector<int> &orangeNumbers, vector<int> &blueNumbers, vector<int> &robotSequence) {
  
  int sequenceLen;
  std::istringstream stream(parameters);
  stream >> sequenceLen;
  
  robotSequence.resize(sequenceLen);

  for (int i = 0; i < sequenceLen; ++i) {
    
    char c;
    stream >> c;

    switch (c) {
     case 'O':
      robotSequence[i] = ORANGE;
      break;
     case 'B':
      robotSequence[i] = BLUE;
    }

    int buttonNumber;
    stream >> buttonNumber;
    if (robotSequence[i] == ORANGE) {
      orangeNumbers.push_back(buttonNumber);
    }
    else {
      blueNumbers.push_back(buttonNumber);
    }
  }
}



int CalculateRobotTime(const vector<int> &blueNumbers, int blueIndex) {
  int currentButton = 1;

  if (blueIndex > 0) {
    currentButton = blueNumbers[blueIndex - 1];
  }

  int distance = blueNumbers[blueIndex] - currentButton;
  if (distance < 0) {
    distance = -distance;
  }
  int time = distance + 1;
  return time;
}


int Max(int a, int b) {
  if (a > b) return a;
  return b;
}



int GetTime(const vector<int> &orangeNumbers, const vector<int> &blueNumbers, const vector<int> &robotSequence) {
  int commonTime;

  int indexInSeq = 0;
  int blueIndex = 0;
  int orangeIndex = 0;
  int blueTime = 0;
  int orangeTime = 0;



  while (indexInSeq < robotSequence.size()) {
    int currentColor = robotSequence[indexInSeq];
    int robotTime;
    int stepsNumber = 0;

    while (indexInSeq < robotSequence.size() && robotSequence[indexInSeq] == currentColor) {
      ++indexInSeq;
      ++stepsNumber;
    }

    for (int i = 0; i < stepsNumber; ++i) {
      switch (currentColor) {
      case BLUE:
        robotTime = CalculateRobotTime(blueNumbers, blueIndex);
        ++blueIndex;
        blueTime += robotTime;
        if (orangeTime >= blueTime) {
          blueTime = orangeTime + 1;
        }
        break;
      case ORANGE:
        robotTime = CalculateRobotTime(orangeNumbers, orangeIndex);
        ++orangeIndex;
        orangeTime += robotTime;
        if (blueTime >= orangeTime) {
          orangeTime = blueTime + 1;
        }
        break;
      }
    }
  }

  commonTime = Max(blueTime, orangeTime);
  return commonTime;
}


int main() {
  string parameters;
  std::getline(cin, parameters);
  
  int numberOfCases;
  std::istringstream stream(parameters);
  stream >> numberOfCases;
  vector<int> result(numberOfCases);

  for (int caseNum = 0; caseNum < numberOfCases; ++caseNum) { 
    std::getline(cin, parameters);

    vector<int> orangeNumbers;
    vector<int> blueNumbers;
    vector<int> robotSequence;

    Parse(parameters, orangeNumbers, blueNumbers, robotSequence);
    result[caseNum] = GetTime(orangeNumbers, blueNumbers, robotSequence);
  }

  for (int i = 0; i < numberOfCases; ++i) {
    cout << "Case #" << i + 1 << ": " << result[i] << endl;
  }
  return 0;
}