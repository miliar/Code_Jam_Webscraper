// 13.04.2013
//

/*
Problem A. Tic-Tac-Toe-Tomek
Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares.
There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares.
Player X's symbol is 'X', and player O's symbol is 'O'.
After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol,
she wins and the game ends. Otherwise the game continues with the other player's move.
If all of the fields are filled with symbols and nobody won, the game ends in a draw.
See the sample input for examples of various winning positions.
Given a 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square),
describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:
    "X won" (the game is over, and X won)
    "O won" (the game is over, and O won)
    "Draw" (the game is over, and it ended in a draw)
    "Game has not completed" (the game is not over yet)
If there are empty cells, and the game is not over, you should output "Game has not completed", even if the outcome of the game is inevitable.
Input
The first line of the input gives the number of test cases, T. T test cases follow.
Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only).
Each test case is followed by an empty line.
Output
For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above.
Make sure to get the statuses exactly right.
When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ",
the capital letter "O" rather than the number "0", and so on.
Limits
The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above.
Small dataset
1 <= T <= 10.
Large dataset
1 <= T <= 1000.
*/

# include <stdio.h>
# include <math.h>
# include <string.h>

# define isDigit(x) ((x) >= 'A' && (x) <= 'Z')
# define isdigit(x) ((x) >= 'a' && (x) <= 'z')
# define convert(x) ( isdigit (x) ? (x)-'a'+'A' : (x)-'A'+'a' )



# define TRR_JUDGE



const int N = 4;

int n, m, k, i, j, t, r;
char s [N][N+1];

void Print ();
bool Check (char c);
bool CountBlank ();

int main ()
{
# ifdef TRR_JUDGE
   freopen ("A.txt", "rt", stdin);
   freopen ("A.out", "wt", stdout);
# endif

   scanf ("%d\n", &t);

   for ( int i=1; i <= t; i++ )
   {
      scanf ("%s\n%s\n%s\n%s\n\n", s [0], s [1], s [2], s [3]);
/*
# ifdef TRR_JUDGE
      printf ("%s\n%s\n%s\n%s\n\n", s [0], s [1], s [2], s [3]);
# endif
*/
      if ( Check ('X') )
         r = 1;
      else if ( Check ('O') )
         r = 2;
      else if ( CountBlank () )
         r = 4;
      else
         r = 3;

//printf ("r=%d   ", r);

      printf ("Case #%d: ", i);
      if ( r == 1 )
         printf ("X won\n");
      else if ( r == 2 )
         printf ("O won\n");
      else if ( r == 3 )
         printf ("Draw\n");
      else
         printf ("Game has not completed\n");
   }

   return 0;
}

bool CountBlank ()
{
   for ( int i=0, j; i < 4; i++ )
      for ( j=0; j < 4; j++ )
         if ( s [i][j] == '.' )
            return true;
   return false;
}

bool Check (char c)
{
   bool fo;
   for ( int i=0, j; i < 4; i++ )
   {
      for ( j=0, fo=true; j < 4; j++ )
         if ( s [i][j] != c && s [i][j] != 'T' )
            { fo=false; break; }
      if ( fo ) return true;

      for ( j=0, fo=true; j < 4; j++ )
         if ( s [j][i] != c && s [j][i] != 'T' )
            { fo=false; break; }
      if ( fo ) return true;
   }

   fo = true;
   for ( int j=0; j < 4; j++ )
      if ( s [j][j] != c && s [j][j] != 'T' )
         { fo=false; break; }

   if ( fo ) return true;

   fo = true;
   for ( int j=0; j < 4; j++ )
      if ( s [j][3-j] != c && s [j][3-j] != 'T' )
         { fo=false; break; }

   return fo;
}
