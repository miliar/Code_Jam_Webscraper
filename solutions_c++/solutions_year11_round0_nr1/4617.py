
//---------------------------------------------------------------------------
//! \file main.cpp
//! \brief Entry point of the program.
//---------------------------------------------------------------------------

// Standard library
#include <algorithm>
#include <iostream>
#include <vector>
#include <deque>

// Our library
#include "buff.hpp"
#include "type.hpp"

//---------------------------------------------------------------------------
//! \type dque_type Type of an input list.
//! \type tset_type Type of an input case.
//---------------------------------------------------------------------------

typedef std::deque< uint_type >  dque_type;
typedef std::vector< dque_type > tset_type;
typedef std::vector< tset_type > goal_type;

//---------------------------------------------------------------------------
//! \brief Processing buffer.
//---------------------------------------------------------------------------

struct buff_type
{
  // [Case][Robot][Switch]
  goal_type goal;
};

//---------------------------------------------------------------------------
//! \brief Parse the input data.
//! \param buff Processing buffer.
//! \return Either
//!   \li true, if operation success.
//!   \li false, otherwise.
//---------------------------------------------------------------------------

bool prepare( char const * file,
              buff_type  & buff )
{
  goal_type & goal = buff.goal;

  goal.clear( );

  ifst_type ifst( file );
  if( true == ifst.bad( ) )
    return false;

  uint_type M;
  if( true == !(ifst >> M))
    return false;

  for( uint_type i = 0; i < M; ++i )
  { 
    tset_type c( 3, dque_type( ) );

    uint_type N;
    if( true == !(ifst >> N) )
      return false;

    for( uint_type j = 0; j < N; ++j )
    {
      char_type bot;
      uint_type pos;

      if( true == !(ifst >> bot >> pos) )
        return false;

      if( bot == T('O') )
      {
        c[0].push_back( pos );
        c[2].push_back( 0 );
      }
      else
      if( bot == T('B') )
      {
        c[1].push_back( pos );
        c[2].push_back( 1 );
      }
      else
      {
        return false;
      }
    }
      
    // std::sort( c[0].begin( ), c[0].end( ) );
    // std::sort( c[1].begin( ), c[1].end( ) );
    goal.push_back( c );
  }

  return true;
}

//---------------------------------------------------------------------------
//! \brief Processing routine.
//! \param buff Processing buffer.
//! \return Either
//!   \li true, if operation success.
//!   \li false, otherwise.
//---------------------------------------------------------------------------

bool process( char const * file,
              buff_type  & buff )
{
  goal_type & goal = buff.goal;

  ofst_type ofst( file );
  if( true == ofst.bad( ) )
    return false;

  uint_type S = goal.size( );
  for( uint_type s = 0; s < S; ++s )
  {
    dque_type & s1 = goal[s][0];
    dque_type & s2 = goal[s][1];
    dque_type & s3 = goal[s][2];
    sint_type   t1 = 1;
    sint_type   t2 = 1;
    uint_type   ct = 0;

    for( ct = 0; !s3.empty( ); ct = ct )
    {
      ct += 1;
      // std::wcout << T("T: ") << ct << std::endl;

      bool f1 = false;
      if( !s1.empty( ) && t1 != s1.front( ) ) 
      {
        f1 = true;
        t1 += (t1 < s1.front( ) ? 1 : -1);
        // std::wcout << T("O.move: ") << t1 << std::endl;
      }

      bool f2 = false;
      if( !s2.empty( ) && t2 != s2.front( ) ) 
      {
        f2 = true;
        t2 += (t2 < s2.front( ) ? 1 : -1);
        // std::wcout << T("B.move: ") << t2 << std::endl;
      }

      if( !f1 &&
          !s1.empty( ) && t1 == s1.front( ) &&
          !s3.empty( ) && 0 == s3.front( ) )
      { 
          // std::wcout << T("O.push: ") << t1 << std::endl;
          s1.pop_front( ); 
          s3.pop_front( );
      }
      else
      if( !f2 &&
          !s2.empty( ) && t2 == s2.front( ) &&
          !s3.empty( ) && 1 == s3.front( ) )
      {
          // std::wcout << T("B.push: ") << t2 << std::endl;
          s2.pop_front( );
          s3.pop_front( );
      }

      /*
      if( !s1.empty( ) && t1 == s1.front( ) ) 
      { 
        if( !s3.empty( ) && 0 == s3.front( ) )
        {
          std::wcout << T("O.push: ") << t1 << std::endl;
          s1.pop_front( ); 
          s3.pop_front( );
        }
      }
      else
      {
        t1 += (t1 < s1.front( ) ? 1 : -1);
        std::wcout << T("O.move: ") << t1 << std::endl;
      }

      if( !s2.empty( ) && t2 == s2.front( ) ) 
      {
        if( !s3.empty( ) && 1 == s3.front( ) )
        {
          std::wcout << T("B.push: ") << t2 << std::endl;
          s2.pop_front( );
          s3.pop_front( );
        }
      }
      else
      {
        t2 += (t2 < s2.front( ) ? 1 : -1);
        std::wcout << T("B.move: ") << t2 << std::endl;
      }
      // */
    }

    ofst << T("Case #") << (s + 1) << T(": ") << ct << std::endl;  
  }

  return true;
}

//---------------------------------------------------------------------------
//! \brief Entry point of the program.
//! \param argc Number of input arguments.
//! \param argv List of input arguments.
//! \return Either
//!   \li 0, if no error occur.
//!   \li Error code, otherwise.
//---------------------------------------------------------------------------

int main( int argc, char ** argv )
{
  char const * ofile = argc > 2 ? argv[2] : "output.txt";
  char const * ifile = argc > 1 ? argv[1] : "input.txt";

  buff_type buff;

  if( false == prepare( ifile, buff ) ||
      false == process( ofile, buff ) )
  {
    return -1;
  }

  return 0;
}

//---------------------------------------------------------------------------
// End of file
//---------------------------------------------------------------------------

