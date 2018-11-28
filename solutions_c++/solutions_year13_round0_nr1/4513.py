#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int check(string& currentLine) {
  int ctX = 0, ctO = 0, ctT = 0;

  for (int i = 0; i < 4; i++) {
    if (currentLine[i] == 'X') {
      ctX++;
    }
    else if (currentLine[i] == 'O') {
      ctO++;
    }
    else if (currentLine[i] == 'T') {
      ctT++;
    }
  }
  
  if (ctX == 4 || (ctX == 3 && ctT == 1)) {
    return 1;
  }
  else if (ctO == 4 || (ctO == 3 && ctT == 1)) {
    return 2;
  }
  
  return 0;
}

int main(int argc, char* argv[])
{ 
  char table[4][4];

  int t;
  
  cin >> t;
  
  string currentLine;
  
  bool completed;

  bool Xwon;
  bool Owon;
   
  for (int i = 0; i < t; i++) {
    completed = true;
    Xwon = Owon = false;
  
    for (int j = 0; j < 4; j++) {
      cin >> currentLine;
      
      for (int k = 0; k < 4; k++) {
        table[j][k] = currentLine[k];
        
        if (currentLine[k] == '.') {
          completed = false;
        }
      }
      
      //winner already found (horizontal)
      if (Xwon || Owon) {
        continue;
      }
      
      //check horizontal
      int result = check(currentLine);

      if (result == 1) {
        Xwon = true;
      }
      else if (result == 2) {
        Owon = true;
      }
    }
    
    
    if (!Xwon && !Owon) {
      //check vertical
      for (int j = 0; j < 4; j++) {
        stringstream ss;  
    
        for (int k = 0; k < 4; k++) {
          ss << table[k][j];
        }
        
        currentLine = ss.str();
        
        //winner already found (vertical)
        if (Xwon || Owon) {
          continue;
        }
        
        int result = check(currentLine);

        if (result == 1) {
          Xwon = true;
        }
        else if (result == 2) {
          Owon = true;
        }
      }
    }
    
    if (!Xwon && !Owon) {
      //check 1st diagonal
      stringstream ss;
      
      for (int i = 0; i < 4; i++) {
        ss << table[i][i];
      }
      
      currentLine = ss.str();
      
      int result = check(currentLine);

      if (result == 1) {
        Xwon = true;
      }
      else if (result == 2) {
        Owon = true;
      }
    }
    
    if (!Xwon && !Owon) {
      //check 2nd diagonal
      stringstream ss;
      
      for (int i = 0; i < 4; i++) {
        ss << table[i][3 - i];
      }
      
      currentLine = ss.str();
      
      int result = check(currentLine);

      if (result == 1) {
        Xwon = true;
      }
      else if (result == 2) {
        Owon = true;
      }
    }
    
    
    cout << "Case #" << i + 1 << ": ";
      
    if (Xwon) {
      cout << "X won" << endl;
    }
    else if (Owon) {
      cout << "O won" << endl;
    }
    else if (completed) {
      cout << "Draw" << endl;
    }
    else {
      cout << "Game has not completed" << endl;
    }
  }

  return 0;
}
