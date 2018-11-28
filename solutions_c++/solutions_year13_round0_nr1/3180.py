#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void SolveTask(std::ifstream& input,std::ofstream& output) {
  std::vector<std::string> board;
  
  for (int index=0;index<4;++index) {
    std::string line;
    input>>line;
    board.push_back(line);
  }
  
  int xCount,oCount,tCount;
    
  for (int index=0;index<4;++index) {
    xCount=0;oCount=0;tCount=0;
    
    for (int index2=0;index2<4;++index2)
      switch (board[index][index2]) {
        case 'X': {
          ++xCount;
          break;
        }
        case 'O': {
          ++oCount;
          break;
        }
        case 'T': {
          ++tCount;
          break;
        }
      }
    
    if (xCount+tCount==4) {
      output<<"X won";
      return;
    }

    if (oCount+tCount==4) {
      output<<"O won";
      return;
    }
    
    xCount=0;oCount=0;tCount=0;
    
    for (int index2=0;index2<4;++index2)
      switch (board[index2][index]) {
        case 'X': {
          ++xCount;
          break;
        }
        case 'O': {
          ++oCount;
          break;
        }
        case 'T': {
          ++tCount;
          break;
        }
      }
      
    if (xCount+tCount==4) {
      output<<"X won";
      return;
    }

    if (oCount+tCount==4) {
      output<<"O won";
      return;
    }
  }
  
  xCount=0;oCount=0;tCount=0;
  
  for (int index=0;index<4;++index)
    switch (board[index][index]) {
      case 'X': {
        ++xCount;
        break;
      }
      case 'O': {
        ++oCount;
        break;
      }
      case 'T': {
        ++tCount;
        break;
      }
    }  
    
  if (xCount+tCount==4) {
    output<<"X won";
    return;
  }

  if (oCount+tCount==4) {
    output<<"O won";
    return;
  }
  
  xCount=0;oCount=0;tCount=0;
  
  for (int index=0;index<4;++index)
    switch (board[index][3-index]) {
      case 'X': {
        ++xCount;
        break;
      }
      case 'O': {
        ++oCount;
        break;
      }
      case 'T': {
        ++tCount;
        break;
      }
    }  
    
  if (xCount+tCount==4) {
    output<<"X won";
    return;
  }

  if (oCount+tCount==4) {
    output<<"O won";
    return;
  }
  
  bool containsEmptyCell=false;
  
  for (int index=0;index<4;++index)
    for (int index2=0;index2<4;++index2)
      containsEmptyCell=containsEmptyCell||(board[index][index2]=='.');
  
  if (containsEmptyCell) {
    output<<"Game has not completed";
  } else {
    output<<"Draw";
  }
}

void main() {
  std::ifstream input("Input.Txt");
  std::ofstream output("Output.Txt");
  
  int numberOfCases;  
  input>>numberOfCases;
  
  for (int caseNumber=1;caseNumber<=numberOfCases;++caseNumber) {
    output<<"Case #"<<caseNumber<<": ";
    SolveTask(input,output);
    output<<std::endl;
  }
}