
//----------------------------------------------------------------------------
// Require-header-file(s)
//----------------------------------------------------------------------------

// Standard-library
#include <iostream>
#include <fstream>

//----------------------------------------------------------------------------
// Common using types
//----------------------------------------------------------------------------

typedef size_t                           size_type;
typedef char                             char_type;
typedef std::basic_ifstream< char_type > ifst_type;
typedef std::basic_ofstream< char_type > ofst_type;

enum { BUFF_SIZE = 4 };
typedef char_type buff_type[BUFF_SIZE][BUFF_SIZE];

//----------------------------------------------------------------------------
// Defined constants
//----------------------------------------------------------------------------

#define TILE_D '.'
#define TILE_O 'O'
#define TILE_T 'T'
#define TILE_X 'X'

#define FLAG_NONE 0
#define FLAG_DRAW 1
#define FLAG_XWON 2
#define FLAG_OWON 3

//----------------------------------------------------------------------------
//! \brief Load the input data from the target input file stream.
//! \param ifst Target input file stream.
//! \param buff Buffer that will held the loaded input.
//! \return Either
//!   \li true, if loading success.
//!   \li false, otherwise.
//----------------------------------------------------------------------------

bool load_buff( ifst_type & ifst, 
                buff_type & buff )
{
  for( size_type i = 0; i < BUFF_SIZE; ++i )
  for( size_type j = 0; j < BUFF_SIZE; ++j )
  {
    if( false == !!(ifst >> buff[i][j]) )
      return false;
  }

  return true;
}

//----------------------------------------------------------------------------
//! \brief Evaluate the game result.
//! \param buff Buffer that held the current game state.
//! \param flag Buffer that will held the result of game evaluation.
//! \return Either
//!   \li true, if evaluation success.
//!   \li false, otherwise.
//----------------------------------------------------------------------------

bool eval_buff( buff_type & buff,
                size_type & flag )
{
  size_type count_d = 0;
  size_type count_o = 0;
  size_type count_t = 0;
  size_type count_x = 0;

  // Check for the horizontal matched
  for( size_type i = 0; i < BUFF_SIZE; ++i )
  {
    count_o = 0;
    count_t = 0;
    count_x = 0;

    for( size_type j = 0; j < BUFF_SIZE; ++j )
    {
      char_type value = buff[i][j];
      switch( value )
      {
        case TILE_D: { ++count_d; break; }
        case TILE_T: { ++count_t; break; }
        case TILE_O: { ++count_o; break; }
        case TILE_X: { ++count_x; break; }
        default:
        {
          std::wcerr << "Error: Found invalid tile '" << value << "'." << std::endl;
          break;
        }
      }
    }

    if( BUFF_SIZE == (count_o + count_t) ) goto summary;
    if( BUFF_SIZE == (count_x + count_t) ) goto summary;
  }

  // Check for the vertical matched
  for( size_type j = 0; j < BUFF_SIZE; ++j )
  {
    count_o = 0;
    count_t = 0;
    count_x = 0;

    for( size_type i = 0; i < BUFF_SIZE; ++i )
    {
      char_type value = buff[i][j];
      switch( value )
      {
        case TILE_D: { ++count_d; break; }
        case TILE_T: { ++count_t; break; }
        case TILE_O: { ++count_o; break; }
        case TILE_X: { ++count_x; break; }
        default:
        {
          std::wcerr << "Error: Found invalid tile '" << value << "'." << std::endl;
          break;
        }
      }
    }

    if( BUFF_SIZE == (count_o + count_t) ) goto summary;
    if( BUFF_SIZE == (count_x + count_t) ) goto summary;
  }

  // Check for the left-right diagonal matched
  {
    count_o = 0;
    count_t = 0;
    count_x = 0;

    for( size_type i = 0; i < BUFF_SIZE; ++i )
    {
      char_type value = buff[i][i];
      switch( value )
      {
        case TILE_D: { ++count_d; break; }
        case TILE_T: { ++count_t; break; }
        case TILE_O: { ++count_o; break; }
        case TILE_X: { ++count_x; break; }
        default:
        {
          std::wcerr << "Error: Found invalid tile '" << value << "'." << std::endl;
          break;
        }
      }
    }

    if( BUFF_SIZE == (count_o + count_t) ) goto summary;
    if( BUFF_SIZE == (count_x + count_t) ) goto summary;
  }

  // Check for the left-right diagonal matched
  {
    count_o = 0;
    count_t = 0;
    count_x = 0;

    for( size_type i = 0; i < BUFF_SIZE; ++i )
    {
      char_type value = buff[i][BUFF_SIZE - i - 1];
      switch( value )
      {
        case TILE_D: { ++count_d; break; }
        case TILE_T: { ++count_t; break; }
        case TILE_O: { ++count_o; break; }
        case TILE_X: { ++count_x; break; }
        default:
        {
          std::wcerr << "Error: Found invalid tile '" << value << "'." << std::endl;
          break;
        }
      }
    }

    if( BUFF_SIZE == (count_o + count_t) ) goto summary;
    if( BUFF_SIZE == (count_x + count_t) ) goto summary;
  }

summary:
  if( BUFF_SIZE == (count_o + count_t) )
  {
    flag = FLAG_OWON;
  }
  else
  if( BUFF_SIZE == (count_x + count_t) )
  {
    flag = FLAG_XWON;
  }
  else
  if( count_d == 0 )
  {
    flag = FLAG_DRAW;
  }
  else
  {
    flag = FLAG_NONE;
  }

  return true;
}

//----------------------------------------------------------------------------
//! \brief Main entrance of this program.
//! \param argc, number of input arguments.
//! \param argv, list of input arguments.
//! \return 0 if program exits successfully.
//----------------------------------------------------------------------------

int main( int     argc, 
          char ** argv )
{
  char const * file_i = argv[1];
  char const * file_o = argv[2];
  if( argc != 3 )
  {
    std::wcerr << "Usage: ./run.out <input-file> <output-file>" << std::endl;
    return 1;
  }

  ifst_type ifst( file_i );
  if( false == ifst.is_open( ) )
  {
    std::wcerr << "Error: Unable to open file '" << file_i << "'." << std::endl;
    return 1;
  }

  ofst_type ofst( file_o );
  if( false == ofst.is_open( ) )
  {
    std::wcerr << "Error: Unable to create file '" << file_o << "'." << std::endl;
    return 1;
  }

  size_type loop = 0;
  if( false == !!(ifst >> loop) )
  {
    std::wcerr << "Error: Found invalid number of loops." << std::endl;
    return 1;
  }

  buff_type buff;
  for( size_type i = 0; i < loop; ++i )
  {
    if( false == load_buff( ifst, buff ) )
    {
      std::wcerr << "Error: Unable to load input data #" << i << "." << std::endl;
      return 1;
    }

    size_type flag = FLAG_NONE;
    if( false == eval_buff( buff, flag ) )
    {
      std::wcerr << "Error: Unable to process input data #" << i << "." << std::endl;
      return 1;
    }

    switch( flag )
    {
      case FLAG_XWON: 
        ofst << "Case #" << (i+1) << ": X won" << std::endl; 
        break;

      case FLAG_OWON: 
        ofst << "Case #" << (i+1) << ": O won" << std::endl; 
        break;

      case FLAG_DRAW: 
        ofst << "Case #" << (i+1) << ": Draw" << std::endl; 
        break;

      case FLAG_NONE: 
        ofst << "Case #" << (i+1) << ": Game has not completed" << std::endl; 
        break;

      default:
        std::wcerr << "Error: Found invalid return flag '" << flag << "'." << std::endl;
        break;
    }
  }

  return 0;
}

//----------------------------------------------------------------------------
// End-of-file
//----------------------------------------------------------------------------

