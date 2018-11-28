#include <stdio.h>

char matrix[4][4];

bool match(char value, char who) {
  return (value==who) || (value=='T');
}

bool wins(char who) {
  for (int i=0; i<4; i++) {
    //Row
    if (match(matrix[i][0], who) && match(matrix[i][1], who) && match(matrix[i][2], who) && match(matrix[i][3], who))
      return true;
    //Col
    if (match(matrix[0][i], who) && match(matrix[1][i], who) && match(matrix[2][i], who) && match(matrix[3][i], who))
      return true;
  }

  //Diag 1
  if (match(matrix[0][0], who) && match(matrix[1][1], who) && match(matrix[2][2], who) && match(matrix[3][3], who))
      return true;
  //Diag 2
  if (match(matrix[3][0], who) && match(matrix[2][1], who) && match(matrix[1][2], who) && match(matrix[0][3], who))
      return true;

  return false;
}

int main() {
  int nTests;
  scanf("%i", &nTests);
  for (int test=1; test<=nTests; test++) {
    bool completed=true;
    for (int line=0; line<4; line++) {
      for (int col=0; col<4; col++) {
	scanf(" %c", &matrix[line][col]);
	completed = completed && matrix[line][col] != '.';
      }
    }

    printf("Case #%i: ", test);
    if (wins('X')) {
      printf("X won\n");
    } else if (wins('O')) {
      printf("O won\n");
    } else if (completed) {
      printf("Draw\n");
    } else {
      printf("Game has not completed\n");
    }
  }

  return 0;
}