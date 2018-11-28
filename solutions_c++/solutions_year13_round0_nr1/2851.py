#include <stdio.h>

#define X_WON_TEXT     "X won"
#define O_WON_TEXT     "O won"
#define DRAW_TEXT      "Draw"
#define NOT_ENDED_TEXT "Game has not completed"

typedef enum
{
  X_WON_GAME,
  O_WON_GAME,
  NO_WINNER
} LineState;

typedef enum
{
  X_WON,
  O_WON,
  DRAW,
  NOT_ENDED
} GameState;

bool isComplete( const char table[ ][ 4 ] )
{
  for ( int ii = 0; ii < 4; ++ii )
  {
    for ( int jj = 0; jj < 4; ++jj )
    {
      if ( table[ ii ][ jj ] == '.' )
      {
        return false;
      }
    }
  }

  return true;
}

LineState verifyLine( const char table[ ][ 4 ], unsigned int line )
{
  int ii;
  for ( ii = 0; ii < 4 && ( table[ line ][ ii ] == 'X' || table[ line ][ ii ] == 'T' ); ++ii );
  if ( ii == 4 )
  {
    return X_WON_GAME;
  } 

  for ( ii = 0; ii < 4 && ( table[ line ][ ii ] == 'O' || table[ line ][ ii ] == 'T' ); ++ii );
  if ( ii == 4 )
  {
    return O_WON_GAME;
  } 

  return NO_WINNER;
}

LineState verifyColumn( const char table[ ][ 4 ], unsigned int column )
{
  int ii;
  for ( ii = 0; ii < 4 && ( table[ ii ][ column ] == 'X' || table[ ii ][ column ] == 'T' ); ++ii );
  if ( ii == 4 )
  {
    return X_WON_GAME;
  } 

  for ( ii = 0; ii < 4 && ( table[ ii ][ column ] == 'O' || table[ ii ][ column ] == 'T' ); ++ii );
  if ( ii == 4 )
  {
    return O_WON_GAME;
  } 

  return NO_WINNER;
}

LineState verifyDiagonals( const char table[ ][ 4 ] )
{
  int ii;
  for ( ii = 0; ii < 4 && ( table[ ii ][ ii ] == 'X' || table[ ii ][ ii ] == 'T' ); ++ii );
  if ( ii == 4 )
  {
    return X_WON_GAME;
  } 

  for ( ii = 0; ii < 4 && ( table[ ii ][ ii ] == 'O' || table[ ii ][ ii ] == 'T' ); ++ii );
  if ( ii == 4 )
  {
    return O_WON_GAME;
  } 

  for ( ii = 0; ii < 4 && ( table[ ii ][ 3 - ii ] == 'X' || table[ ii ][ 3 - ii ] == 'T' ); ++ii );
  if ( ii == 4 )
  {
    return X_WON_GAME;
  } 

  for ( ii = 0; ii < 4 && ( table[ ii ][ 3 - ii ] == 'O' || table[ ii ][ 3 - ii ] == 'T' ); ++ii );
  if ( ii == 4 )
  {
    return O_WON_GAME;
  } 

  return NO_WINNER;
}

GameState getGameState( const char table[ ][ 4 ] )
{
  switch ( verifyLine( table, 0 ) )
  {
    case X_WON_GAME:
      return X_WON;
    case O_WON_GAME:
      return O_WON;
  }
  switch ( verifyLine( table, 1 ) )
  {
    case X_WON_GAME:
      return X_WON;
    case O_WON_GAME:
      return O_WON;
  }
  switch ( verifyLine( table, 2 ) )
  {
    case X_WON_GAME:
      return X_WON;
    case O_WON_GAME:
      return O_WON;
  }
  switch ( verifyLine( table, 3 ) )
  {
    case X_WON_GAME:
      return X_WON;
    case O_WON_GAME:
      return O_WON;
  }
  switch ( verifyColumn( table, 0 ) )
  {
    case X_WON_GAME:
      return X_WON;
    case O_WON_GAME:
      return O_WON;
  }
  switch ( verifyColumn( table, 1 ) )
  {
    case X_WON_GAME:
      return X_WON;
    case O_WON_GAME:
      return O_WON;
  }
  switch ( verifyColumn( table, 2 ) )
  {
    case X_WON_GAME:
      return X_WON;
    case O_WON_GAME:
      return O_WON;
  }
  switch ( verifyColumn( table, 3 ) )
  {
    case X_WON_GAME:
      return X_WON;
    case O_WON_GAME:
      return O_WON;
  }
  switch ( verifyDiagonals( table ) )
  {
    case X_WON_GAME:
      return X_WON;
    case O_WON_GAME:
      return O_WON;
  }

  if ( isComplete( table ) )
  {
    return DRAW;
  } else
  {
    return NOT_ENDED;
  }
}


int main( void )
{
  char table[ 4 ][ 4 ] = { 'X','X','X','T', '.', '.', '.', '.', 'O', 'O', '.', '.', '.', '.', '.', '.' };
  char * msg      = NULL;
  int    ii       = 1;
  int    numCases = 0;
  FILE * input  = fopen( "C:\\Users\\Tiago\\Dropbox\\GoogleCodeJam2013\\QualificationRound\\input.txt", "rt" );
  FILE * output = fopen( "C:\\Users\\Tiago\\Dropbox\\GoogleCodeJam2013\\QualificationRound\\output.txt", "wt" );

  fscanf( input, " %d", &numCases );

  for ( ii = 1; ii <= numCases; ++ii )
  {
    fscanf( input, " %c %c %c %c\n %c %c %c %c\n %c %c %c %c\n %c %c %c %c\n", &table[ 0 ][ 0 ], &table[ 0 ][ 1 ], &table[ 0 ][ 2 ], &table[ 0 ][ 3 ], 
                                                                               &table[ 1 ][ 0 ], &table[ 1 ][ 1 ], &table[ 1 ][ 2 ], &table[ 1 ][ 3 ], 
                                                                               &table[ 2 ][ 0 ], &table[ 2 ][ 1 ], &table[ 2 ][ 2 ], &table[ 2 ][ 3 ], 
                                                                               &table[ 3 ][ 0 ], &table[ 3 ][ 1 ], &table[ 3 ][ 2 ], &table[ 3 ][ 3 ] );

    switch ( getGameState( table ) )
    {
      case X_WON:
        msg = X_WON_TEXT;
        break;
      case O_WON:
        msg = O_WON_TEXT;
        break;
      case DRAW:
        msg = DRAW_TEXT;
        break;
      case NOT_ENDED:
        msg = NOT_ENDED_TEXT;
        break;

    }
    fprintf( output, "Case #%d: %s\n", ii, msg );
  }
}