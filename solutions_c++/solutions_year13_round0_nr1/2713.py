#include <cstdio>
#include <cstdlib>

int  T;
char board[5][5];

enum {
  X_WON,
  O_WON,
  DRAW,
  NOT_COMPLETED
};

const char *status_description[4] = {
  "X won",
  "O won",
  "Draw",
  "Game has not completed"
};

void readBoard()
{
  for ( int i=0; i<5; ++i )
    gets(board[i]);
}

void report()
{
  fprintf(stderr, "The board given is not valid!\n");
  exit(1);
}

int getStatus()
{
  int X_complete_count =  0;
  int O_complete_count =  0;
  int empty_count      =  0;
  int row_count[4][2]  = {0};
  int col_count[4][2]  = {0};
  int dia_count[7][2]  = {0};
  int dib_count[7][2]  = {0};
  int Ti=-1, Tj=-1, Tk=-1, Tl=-1;

  for ( int i=0; i<4; ++i ) {
    for ( int j=0; j<4; ++j ) {
      if      ( board[i][j]=='.' ) ++empty_count;
      else if ( board[i][j]=='T' ) Ti=i, Tj=j, Tk=i+j, Tl=i-j+3;
      else if ( board[i][j]=='X' ) ++row_count[i][0], ++col_count[j][0], ++dia_count[i+j][0], ++dib_count[i-j+3][0];
      else if ( board[i][j]=='O' ) ++row_count[i][1], ++col_count[j][1], ++dia_count[i+j][1], ++dib_count[i-j+3][1];
      else                         report();
    }
  }

  for ( int i=0; i<4; ++i ) {
    if ( row_count[i][0]==4 || (i==Ti && row_count[i][0]==3) ) ++X_complete_count;
    if ( row_count[i][1]==4 || (i==Ti && row_count[i][1]==3) ) ++O_complete_count;
  }

  for ( int j=0; j<4; ++j ) {
    if ( col_count[j][0]==4 || (j==Tj && col_count[j][0]==3) ) ++X_complete_count;
    if ( col_count[j][1]==4 || (j==Tj && col_count[j][1]==3) ) ++O_complete_count;
  }

  for ( int k=0; k<7; ++k ) {
    /*
    printf("dia_count[k=%d][X]=%d, dia_count[k=%d][O]=%d\n",
	   k, dia_count[k][0],
	   k, dia_count[k][1]);
    */
    if ( dia_count[k][0]==4 || (k==Tk && dia_count[k][0]==3) ) ++X_complete_count;
    if ( dia_count[k][1]==4 || (k==Tk && dia_count[k][1]==3) ) ++O_complete_count;
  }

  for ( int l=0; l<7; ++l ) {
    if ( dib_count[l][0]==4 || (l==Tl && dib_count[l][0]==3) ) ++X_complete_count;
    if ( dib_count[l][1]==4 || (l==Tl && dib_count[l][1]==3) ) ++O_complete_count;
  }

  //printf("X_complete_count = %d\n", X_complete_count);
  //printf("O_complete_count = %d\n", O_complete_count);

  if ( empty_count==0 ) {
    if      ( X_complete_count==0 && X_complete_count==O_complete_count ) return DRAW;
    else if ( X_complete_count> 0 && O_complete_count==0 )                return X_WON;
    else if ( X_complete_count==0 && O_complete_count> 0 )                return O_WON;
    else                                                                  report();
  }
  else {
    if      ( X_complete_count> 0 && O_complete_count==0 )                return X_WON;
    else if ( X_complete_count==0 && O_complete_count> 0 )                return O_WON;
    else if ( X_complete_count==0 && O_complete_count==0 )                return NOT_COMPLETED;
    else                                                                  report();
  }
}

int main()
{
  scanf("%d\n", &T);
  for ( int i=1; i<=T; ++i ) {
    readBoard();
    int status = getStatus();
    printf("Case #%d: %s\n", i,
	   status_description[status]);
  }
}
