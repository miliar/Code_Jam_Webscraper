#include<iostream>
#include<cstdio>

void work (int ca) 
{
  char a[5][5];
  for(int i = 0; i <4; i++) {
    scanf("%s", a[i]);
  }
  bool win;
  for (int i = 0; i < 4; i++) {	
     win = true;
    for (int j = 0; j < 4; j++) {
      if (!(a[i][j] == 'X' || a[i][j] == 'T'))
	win = false;
    }
    if (win) {
      printf("Case #%d: X won", ca);
      return;
    }
    win = true;
    for (int j = 0; j < 4; j++) {
      if (!(a[j][i] == 'X' || a[j][i] == 'T'))
	win = false;
    }
    if (win) {
      printf("Case #%d: X won", ca);
      return;
    }
  }	
   win = true;
  for (int j = 0; j < 4; j++) {
    if (!(a[j][j] == 'X' || a[j][j] == 'T'))
      win = false;
  }
  if (win) {
    printf("Case #%d: X won", ca);
    return;
  }
   win = true;
  for (int j = 0; j < 4; j++) {
    if (!(a[3-j][j] == 'X' || a[3-j][j] == 'T'))
      win = false;
  }
  if (win) {
    printf("Case #%d: X won", ca);
    return;
  }

  //=========================
  for (int i = 0; i < 4; i++) {	
     win = true;
    for (int j = 0; j < 4; j++) {
      if (!(a[i][j] == 'O' || a[i][j] == 'T'))
	win = false;
    }
    if (win) {
      printf("Case #%d: O won", ca);
      return;
    }
    win = true;
    for (int j = 0; j < 4; j++) {
      if (!(a[j][i] == 'O' || a[j][i] == 'T'))
	win = false;
    }
    if (win) {
      printf("Case #%d: O won", ca);
      return;
    }
  }	
  win = true;
  for (int j = 0; j < 4; j++) {
    if (!(a[j][j] == 'O' || a[j][j] == 'T'))
      win = false;
  }
  if (win) {
    printf("Case #%d: O won", ca);
    return;
  }
  win = true;
  for (int j = 0; j < 4; j++) {
    if (!(a[3-j][j] == 'O' || a[3-j][j] == 'T'))
      win = false;
  }
  if (win) {
    printf("Case #%d: O won", ca);
    return;
  }
  
  for (int i = 0; i < 4; i++) 
    for (int j = 0; j < 4; j++) 
      if (a[i][j] == '.') {
	printf("Case #%d: Game has not completed", ca);
	return;
      }
  
  printf("Case #%d: Draw", ca);
}

int main()
{
  int T;
  scanf("%d",&T);
  int b = T;
  while(T-- > 0) {
    work(b-T);
    printf("\n");
  }
}

