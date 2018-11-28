#include<iostream>
#include<string>
#include<cassert>
#include<cstdlib>

using namespace std;

int checkRow(char* deck[4], int cases){
  for(int i = 0; i < 4; ++i){
    int countT = 0, countX = 0, countO = 0;
    for(int j = 0; j < 4; ++j){  
      if(deck[i][j] == 'X'){
	countX++;
      }
      if(deck[i][j] == 'T'){
	countT++;
      }
      if(deck[i][j] == 'O'){
	countO++;
      }
    }
    int resultX = countT+countX;
    int resultO = countT+countO;

    if(resultX == 4){
      cout << "Case #" << cases << ": " << "X won" << endl;
      return 1;
    }
    else if(resultO == 4){
      cout << "Case #" << cases << ": " << "O won" << endl;
      return 1;
    }
  }
  return 0;
}

int checkCol(char* deck[4], int cases){
  for(int i = 0; i < 4; ++i){
    int countT = 0, countX = 0, countO = 0;
    for(int j = 0; j < 4; ++j){
      if(deck[j][i] == 'X'){
        countX++;
      }
      if(deck[j][i] == 'T'){
        countT++;
      }
      if(deck[j][i] == 'O'){
        countO++;
      }
    }
    int resultX = countT+countX;
    int resultO = countT+countO;
  
    if(resultX == 4){
      cout << "Case #" << cases << ": " << "X won" << endl;
      return 1;
    }
    else if(resultO == 4){
      cout << "Case #" << cases << ": " << "O won" << endl;
      return 1;
    }   
  }
  return 0;
}

int checkDig1(char* deck[4], int cases){
  int countT = 0, countX = 0, countO = 0;
  for(int i = 0; i < 4; ++i){
    if(deck[i][i] == 'T'){
      countT++;
    }
    if(deck[i][i] == 'O'){
      countO++;
    }
    if(deck[i][i] == 'X'){
      countX++;
    }
  }
  int resultX = countT+countX;
  int resultO = countT+countO;

  if(resultX == 4){
    cout << "Case #" << cases << ": " << "X won" << endl;
    return 1;
  }
  else if(resultO == 4){
    cout << "Case #" << cases << ": " << "O won" << endl;
    return 1;
  }
    return 0;
}

int checkDig2(char* deck[4], int cases){
  int countT = 0, countX = 0, countO = 0;
  for(int i = 0; i < 4; ++i){
    if(deck[3-i][i] == 'T'){
      countT++;
    }
    if(deck[3-i][i] == 'O'){
      countO++;
    }
    if(deck[3-i][i] == 'X'){
      countX++;
    }
  }
  int resultX = countT+countX;
  int resultO = countT+countO;

  if(resultX == 4){
    cout << "Case #" << cases << ": " << "X won" << endl;
    return 1;
  }
  else if(resultO == 4){
    cout << "Case #" << cases << ": " << "O won" << endl;
    return 1;
  }
  
  return 0;
 
}

int main(){
  int cases = 0, count = 0, i = 0, j = 0;
  cin >> cases;
  count = cases;
  char** deck;
  deck = new char*[4];
  while(count > 0){
    for(i = 0; i < 4; ++i){
      deck[i] = new char[4];
    }
    for(i = 0; i < 4; ++i){
      for(j = 0; j < 4; ++j){
	cin >> deck[i][j];
      }
    }
    if(!checkRow(deck, cases-count+1) && !checkCol(deck, cases-count+1)  && !checkDig1(deck, cases-count+1) && !checkDig2(deck, cases-count+1)){
      
      int dotc = 0;
      for(i = 0; i < 4; ++i){
	for(j = 0; j < 4; ++j){
	  if(deck[i][j] == '.'){
	    dotc++;
	  }
	}
      }
      if(dotc != 0){
	cout << "Case #" << cases-count+1 << ": ";
	cout << "Game has not completed" << endl;	
      }
      else{
	cout << "Case #" << cases-count+1 << ": ";
	cout << "Draw" << endl;
      }
    }
    --count;
  }

  for(i = 0; i < 4; ++i){
    delete deck[i];
  }
  delete deck;
  return 0;
}
