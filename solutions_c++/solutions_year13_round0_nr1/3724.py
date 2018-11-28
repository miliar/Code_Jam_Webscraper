#include <cstdio>
#include <cstdlib>

char board[4][4];
int gameCompleted;
FILE *fout = fopen ("output.txt", "w");

int checkRow (int row);
int checkCol (int col);
int checkDiag1 (void);
int checkDiag2 (void);
void printBoard (void);
void checkBoard (int caseNum);

int main (int argc, char **argv) {
   remove ("output.txt");
   FILE *fin = fopen ("input.txt", "r");
   
   int n;
   fscanf (fin, "%d\n", &n);
   
   for (int i = 0; i < n; i++) {
      for (int j = 0; j < 4; j++) {
         for (int k = 0; k < 4; k++) {
            fscanf (fin, "%c", &board[j][k]);
         }
         fscanf (fin, "\n");
      }
      fscanf (fin, "\n");
      //printBoard ();
      checkBoard (i + 1);
   }
   
   //system ("pause");
   
   return 0;
}

int checkRow (int row) {
   int numX = 0, numO = 0;
   for (int i = 0; i < 4; i++) {
      if (board[row][i] == 'X') {
         numX++;
      } else if (board[row][i] == 'O') {
         numO++;
      } else if (board[row][i] == 'T') {
         numX++;
         numO++;
      }
   }
   
   if (numX == 4) {
      //X won
      return 1;
   } else if (numO == 4) {
      //O won
      return -1;
   } else {
      //neither won
      return 0;
   }
}

int checkCol (int col) {
   int numX = 0, numO = 0;
   for (int i = 0; i < 4; i++) {
      if (board[i][col] == 'X') {
         numX++;
      } else if (board[i][col] == 'O') {
         numO++;
      } else if (board[i][col] == 'T') {
         numX++;
         numO++;
      }
   }
   
   if (numX == 4) {
      //X won
      return 1;
   } else if (numO == 4) {
      //O won
      return -1;
   } else {
      //neither won
      return 0;
   }
}

int checkDiag1 (void) {
   int numX = 0, numO = 0;
   for (int i = 0; i < 4; i++) {
      if (board[i][i] == 'X') {
         numX++;
      } else if (board[i][i] == 'O') {
         numO++;
      } else if (board[i][i] == 'T') {
         numX++;
         numO++;
      }
   }
   
   if (numX == 4) {
      //X won
      return 1;
   } else if (numO == 4) {
      //O won
      return -1;
   } else {
      //neither won
      return 0;
   }
}

int checkDiag2 (void) {
   int numX = 0, numO = 0;
   for (int i = 0; i < 4; i++) {
      if (board[i][3-i] == 'X') {
         numX++;
      } else if (board[i][3-i] == 'O') {
         numO++;
      } else if (board[i][3-i] == 'T') {
         numX++;
         numO++;
      }
   }
   
   if (numX == 4) {
      //X won
      return 1;
   } else if (numO == 4) {
      //O won
      return -1;
   } else {
      //neither won
      return 0;
   }
}

void printBoard (void) {
   for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
         printf("%c", board[i][j]);
      }
      printf("\n");
   }
}

void checkBoard (int caseNum) {
   gameCompleted = 1;
   
   for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
         if (board[i][j] == '.') {
            gameCompleted = 0;
         }
      }
   }
   
   for (int i = 0; i < 4; i++) {
      if (checkRow (i) == 1) {
         fprintf (fout, "Case #%d: X won\n", caseNum);
         //printf ("Case #%d: X won\n", caseNum);
         return;
      } else if (checkRow (i) == -1) {
         fprintf (fout, "Case #%d: O won\n", caseNum);
         //printf ("Case #%d: O won\n", caseNum);
         return;
      }
   }
   
   for (int i = 0; i < 4; i++) {
      if (checkCol (i) == 1) {
         fprintf (fout, "Case #%d: X won\n", caseNum);
         //printf ("Case #%d: X won\n", caseNum);
         return;
      } else if (checkCol (i) == -1) {
         fprintf (fout, "Case #%d: O won\n", caseNum);
         //printf ("Case #%d: O won\n", caseNum);
         return;
      }
   }
   
   if (checkDiag1 () == 1) {
      fprintf (fout, "Case #%d: X won\n", caseNum);
      //printf ("Case #%d: X won\n", caseNum);
      return;
   } else if (checkDiag1 () == -1) {
      fprintf (fout, "Case #%d: O won\n", caseNum);
      //printf ("Case #%d: O won\n", caseNum);
      return;
   }
   
   if (checkDiag2 () == 1) {
      fprintf (fout, "Case #%d: X won\n", caseNum);
      //printf ("Case #%d: X won\n", caseNum);
      return;
   } else if (checkDiag2 () == -1) {
      fprintf (fout, "Case #%d: O won\n", caseNum);
      //printf ("Case #%d: O won\n", caseNum);
      return;
   }
   
   if (gameCompleted == 0) {
      fprintf (fout, "Case #%d: Game has not completed\n", caseNum);
      //printf ("Case #%d: Game has not completed\n", caseNum);
      return;
   } else {
      fprintf (fout, "Case #%d: Draw\n", caseNum);
      //printf ("Case #%d: Draw\n", caseNum);
      return;
   }
}

