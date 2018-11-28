#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

enum ROBOT_TYPE
  {
    BLUE,
    ORANGE
  };

struct SequenceNode
{
public:
  ROBOT_TYPE color;
  int buttonNumber;
};

int main()
{
  ifstream Input("input.txt");
  ofstream Output("out.txt");
  int nCases = 0;
  int curSequenceLength = 0;
  vector<SequenceNode> sequence(0);
  string currentLine;
  int caseNum = 0;

  if(!(Input.good())) {
    cout << "Problem opening input stream" << endl;
    return 0;
  }

  while(!(Input.eof())) {
    if(nCases == 0) {
      Input >> nCases; Input.ignore();
      continue;
    } else {
      caseNum++;
      getline(Input, currentLine);
      if(currentLine.length() == 0) {
      	continue;
      }

      char flag = 'N';
      // N: curSequenceLength
      // C: Robot color
      // B: Button number
      for(int i = 0; i < currentLine.length(); i++) {
	// Swap flags:
	if((currentLine[i] == ' ') || (currentLine[i] == '\t')) {
	  if(flag == 'N') {
	    flag = 'C';
	    sequence.resize(1);
	    sequence[0].buttonNumber = 0;
	  } else if(flag == 'C') {
	    flag = 'B';
	  } else if(flag == 'B') {
	    flag = 'C';
	    sequence.resize(sequence.size() + 1);
	    sequence[sequence.size() - 1].buttonNumber = 0;
	  }
	  
	  continue;
	} else if(currentLine[i] == '\n' || currentLine[i] == '\r') {
	  if(flag == 'B') {
	    flag = 'N';
	  }
	  continue;
	}
      
	// Swap cases:
	switch(flag) {
	case 'N':
	  curSequenceLength *= 0;
	  curSequenceLength += static_cast<int>(currentLine[i] - '0');
	  break;
	case 'C':
	  if(currentLine[i] == 'B') {
	    sequence[sequence.size() - 1].color = BLUE;
	  } else if(currentLine[i] == 'O') {
	    sequence[sequence.size() - 1].color = ORANGE;
	  } else {
	    throw ("Invalid sequence " + currentLine[i]);
	  }
	  break;
	case 'B':
	  sequence[sequence.size() - 1].buttonNumber *= 10;
	  sequence[sequence.size() - 1].buttonNumber +=
	    static_cast<int>(currentLine[i] - '0');
	  break;
	}
      }
      // Parsing complete.
      int bluePos = 1;
      int orangePos = 1;
      int nextBluePos = 0;
      int nextOrangePos = 0;
      int timeElapsed = 0;
      for(int i = 0; i < sequence.size(); i++) {
	if(nextBluePos == 0 && sequence[i].color == BLUE) {
	  nextBluePos = sequence[i].buttonNumber;
	}
	if(nextOrangePos == 0 && sequence[i].color == ORANGE) {
	  nextOrangePos = sequence[i].buttonNumber;
	}
	if(nextBluePos != 0 && nextOrangePos != 0) {
	  break;
	}
      }
      // Start our sequence!
      while(sequence.size() > 0) { 
	bool toRemove = false;
	// Move our colors in the directions they should be...
	if(nextBluePos != 0 && nextBluePos > bluePos) {
	  bluePos++;
	} else if(nextBluePos != 0 && nextBluePos < bluePos) {
	  bluePos--;
	} else if((nextBluePos == bluePos) && (sequence[0].color == BLUE)) {
	  // Push the button!
	  toRemove = true;

	  nextBluePos = 0;
	  for(int i = 1; (i < sequence.size()) && (nextBluePos == 0); i++) {
	    if(sequence[i].color == BLUE)
	      nextBluePos = sequence[i].buttonNumber;
	  }
	}

	if(nextOrangePos != 0 && nextOrangePos > orangePos) {
	  orangePos++;
	} else if(nextOrangePos != 0 && nextOrangePos < orangePos) {
	  orangePos--;
	} else if((nextOrangePos == orangePos) && (sequence[0].color == ORANGE)) {
	  toRemove = true;

	  nextOrangePos = 0;
	  for(int i = 1; (i  < sequence.size()) && (nextOrangePos == 0); i++) {
	    if(sequence[i].color == ORANGE)
	      nextOrangePos = sequence[i].buttonNumber;
	  }
	}

	if(toRemove) {
	  for(int i = 1; i < sequence.size(); i++) {
	    sequence[i - 1] = sequence[i];
	  }
	  sequence.resize(sequence.size() - 1);
	}
	
	timeElapsed++;
      }

      // Output the information we have found:
      Output << "Case #" << caseNum << ": " << timeElapsed << endl;

      curSequenceLength = 0;
      sequence.resize(0);
      currentLine = "";
    }
  }

  Input.close();
  Output.close();
  return 0;
}
