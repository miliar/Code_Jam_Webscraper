
//--------------------------------------------------------------------------
//! \file main.cpp
//! \brief Google Codejam 2010 - 1st round - Theme Park.
//--------------------------------------------------------------------------

#include <iostream>
#include <valarray>
#include <deque>

//--------------------------------------------------------------------------
//! \typedef loop_t Type of loop variable.
//! \typedef data_t Type of data.
//! \typedef dque_t Type of player groups queue.
//--------------------------------------------------------------------------

typedef unsigned long        loop_t;
typedef unsigned long long   data_t;
typedef std::deque< data_t > dque_t;

//--------------------------------------------------------------------------
//! \brief Get the 'GCD' of 'x' and 'y'.
//! \param x An integer number.
//! \param y Another integer number.
//! \return 'GCD' value of 'x' and 'y'.
//--------------------------------------------------------------------------

data_t gcd( data_t x,
            data_t y )
{
  if( x < y ) 
    std::swap( x, y );

  for( data_t g = x % y; g != 0; g = x % y )
  {
    x = y;
    y = g;
  }

  return y;
}

//--------------------------------------------------------------------------
//! \brief Make the substract list of the input.
//! \param source List of inputs.
//! \param output List of outputs.
//! \return Size of the output, also return 0 if any error occur.
//--------------------------------------------------------------------------

loop_t make_substract_list( dque_t const & source,
                            dque_t       & output )
{
  output.clear( );

  // If input is not empty
  loop_t N = source.size( ); 
  if( N == 0 )
    return 0;

  // Get absolute substract value for each adjacent pair
  data_t p = source[0];
  for( loop_t i = 1; i < N; ++i )
  {
    data_t q = source[i];
    data_t d = p > q ? p - q : q - p;

    if( d > 0 )
      output.push_back( d );
  }

  // Return size of the output
  return output.size( );
}

//--------------------------------------------------------------------------
//! \brief Get the minimum waiting time.
//! \param source List of input.
//! \return Minimum waiting time.
//--------------------------------------------------------------------------

data_t find_minimum_waiting( dque_t const & source )
{
  dque_t sublst;

  // Find the substract list
  loop_t N = make_substract_list( source, sublst );
  if( N == 0 )
    return 0;

  // Find the 'GCD' for each item in substract list
  data_t minval = sublst[0];
  for( loop_t i = 1; i < N; ++i )
    minval = gcd( minval, sublst[i] );

  // Find diff value
  data_t difval = (source[0] % minval);
  if( difval == 0 )
    return 0;

  // Return minimum 'GCD' value
  return minval - difval;
}

//--------------------------------------------------------------------------
//! \brief Main entry point of the function.
//! \param argc Number of input arguments.
//! \param argv List of input arguments.
//! \return Error code if any, otherwise 0.
//--------------------------------------------------------------------------

int main( int argc, char ** argv )
{
  loop_t T; // Number of test cases

  // Read number of test cases
  if( !(std::cin >> T) )
  {
    std::cerr << "Error: Read number of test cases failed !!!" 
              << std::endl;

    return -1;
  }

  // Process each test case
  for( loop_t i = 1; i <= T; ++i )
  {
    data_t N; // Size of input list
    dque_t Q; // List of input
 
    // Read size of input list
    if( !(std::cin >> N) )
    {
      std::cerr << "Error: Read size of input failed !!!" 
                << std::endl;

      return -1;
    }
 
    // Read addition datas of current test case
    for( loop_t j = 0; j < N; ++j )
    {
      data_t d = 0; // Group size

      // Read size of each group
      if( !(std::cin >> d) )
      {
        std::cerr << "Error: Read input datas of case '"
                  << i
                  << "', sub group '"
                  << j
                  << "' failed !!!" 
                  << std::endl;
      
        return -1;
      }

      // Add new item to the queue
      Q.push_back( d );
    }

    // Process and show the result
    std::cout << "Case #" 
              << i 
              << ": " 
              << find_minimum_waiting( Q )
              << std::endl;
  }

  // Successfully return
  return 0;
}

//--------------------------------------------------------------------------
// End of file
//--------------------------------------------------------------------------

