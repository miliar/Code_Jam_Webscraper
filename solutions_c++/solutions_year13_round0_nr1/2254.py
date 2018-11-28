#include<stdio.h>
#include<stdlib.h>

const int width = 4;
const int height = 4;
char board[height][width];
int number;
int test_case;
char* result;
bool winX;
bool winO;
bool is_full;
int checkX;
int checkO;
int checkT;

int load() {
  for(int i=0; i<height; ++i){
    for(int j=0; j<width; ++j){
      scanf("%c", &board[i][j]);
    }
    scanf("\n");
  }
  scanf("\n");
  return 0;
}

int check(char c){
  if(c == 'T'){
    checkT++;
  }
  else {
    if(c == 'O'){
      checkO++;
    }
    else {
      if(c == 'X'){
	checkX++;
      }
    }
  }
  return 0;
}

int setWins(){
  if(!winX){
    if((checkX == 4) || (checkX == 3 && checkT == 1)){
      winX = true;
    }
  }
  if(!winO){
    if((checkO == 4) || (checkO == 3 && checkT == 1)){
      winO = true;
    }    
  }
  return 0;
}

int check_board(){
  is_full = true;
  for(int i=0; i<height; ++i){
    for(int j=0; j<width; ++j){
      if(board[i][j] == '.'){
	is_full = false;
      }
    }
  }
  return 0;
}

int check_rows(){
  for(int i=0; i<height; ++i){
    checkX = 0;
    checkO = 0;
    checkT = 0;
    for(int j=0; j<width; ++j){
      check(board[i][j]);
    }
    setWins();
  }
  return 0;
}

int check_columns(){
  for(int i=0; i<width; ++i){
    checkX = 0;
    checkO = 0;
    checkT = 0;
    for(int j=0; j<height; ++j){
      check(board[j][i]);
    }
    setWins();
  }
  return 0;
}

int check_diagonals(){
  checkX = 0;
  checkO = 0;
  checkT = 0;
  for(int i=0; i<width; ++i){
    check(board[i][i]);
  }
  setWins();
  checkX = 0;
  checkO = 0;
  checkT = 0;
  for(int i=0; i<width; ++i){
    check(board[i][3-i]);
  }
  setWins();
  return 0;
}

int main() {
  scanf("%d\n", &number);
  for(int i=0; i<number; ++i){
    test_case = i+1;
    load();
    check_board();
    winX = false;
    winO = false;
    check_rows();
    //printf("%s\n", (winX)?"true":"false");
    check_columns();
    //printf("%s\n", (winX)?"true":"false");
    check_diagonals();
    //printf("%s\n", (winX)?"true":"false");
    if(winX){
      result = "X won";
    }
    else {
      if(winO){
	result = "O won";
      }
      else {
	if(is_full){
	  result = "Draw";
	}
	else {
	  result = "Game has not completed";
	}
      }
    }
    printf("Case #%d: ", test_case);
    printf("%s\n", result);
  }
  return 0;
}
