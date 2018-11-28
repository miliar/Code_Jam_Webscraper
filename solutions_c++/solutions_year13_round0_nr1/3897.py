//
//  main.cpp
//  qu
//
//  Created by Julian Wu on 4/13/13.
//  Copyright (c) 2013 Julian Wu. All rights reserved.
//

#include <stdio.h>

int countEmpty(char* t) {
  int ept = 0;
  for (int i = 0; i < 16; ++i) {
    if (t[i] == '.') {
      ept++;
    }
  }
  return ept;
}

void printTb(char* t){
  for (int i = 0; i < 16; ++i) {
    if (i % 4 == 0) {
      printf("\n");
    }
    printf("%c", t[i]);
    
  }
}

inline bool isP(int i, int j, char* t, char player){
  return t[i * 4 + j] == player || t[i * 4 + j] == 'T';
}

bool hasConnected(char player, char *t) {
  for (int i = 0; i < 4; ++i) {
    // row
    if (isP(i, 0, t, player) &&
        isP(i, 1, t, player) &&
        isP(i, 2, t, player) &&
        isP(i, 3, t, player) )
    {
      return true;
    }
    // col
    if (isP(0, i, t, player) &&
        isP(1, i, t, player) &&
        isP(2, i, t, player) &&
        isP(3, i, t, player) )
    {
      return true;
    }
    
    //diag
    if (isP(0, 0, t, player) &&
        isP(1, 1, t, player) &&
        isP(2, 2, t, player) &&
        isP(3, 3, t, player) )
    {
      return true;
    }
    if (isP(0, 3, t, player) &&
        isP(1, 2, t, player) &&
        isP(2, 1, t, player) &&
        isP(3, 0, t, player) )
    {
      return true;
    }
  }
  return false;
}

void analysis(char *t){
  if (hasConnected('O', t)) {
    printf("O won\n");
    return;
  }
  if (hasConnected('X', t)) {
    printf("X won\n");
    return;
  }
  if (countEmpty(t)) {
    printf("Game has not completed\n");
    return;
  } else {
    printf("Draw\n");
    return;
  }
}
int main(){
  int cases = 0;
  scanf("%d", &cases);
  getchar();
  for (int i = 0; i < cases; ++i) {
    char table[17];
    for (int j = 0; j < 16; j+=4) {
      gets(table + j);
    }
    if (i < cases - 1) getchar();
    printf("Case #%d: ", i+1);
    analysis(table);
//    printf("\nPrinting table======\n");
//    printTb(table);
//    printf("\nend----\n");
  }
  
}