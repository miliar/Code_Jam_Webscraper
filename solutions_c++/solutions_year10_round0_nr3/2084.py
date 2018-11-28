
//--------------------------------------------------------------------------
//! \file main.cpp
//! \brief Google Codejam 2010 - 1st round - Theme Park.
//--------------------------------------------------------------------------

#include <iostream>
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
//! \brief Calculate income of 1 round.
//! \param Q Queue of player groups.
//! \param k Number of available seats.
//! \return Income of this round (alway <= k).
//--------------------------------------------------------------------------

data_t calculate_round_income( dque_t & Q, 
                               data_t   k )
{
  loop_t max = Q.size( ); // Number of groups inside 'Q'
  data_t sum = 0;         // Income of this round

  // Loop atmost 'max' group inside the 'Q'
  for( loop_t i = 0; i < max; ++i )
  {
    data_t g = Q.front( ); // Size of first group
    
    // If no space left
    if( (sum + g) > k )
      break;

    // Rotate queue
    Q.pop_front( );
    Q.push_back( g );

    // Update income
    sum += g;
  }

  // Return result
  return sum;
}

//--------------------------------------------------------------------------
//! \brief Calculate income of all rounds.
//! \param Q Queue of player groups.
//! \param R Number of available rounds.
//! \param k Number of available seats.
//! \return Income of all rounds.
//--------------------------------------------------------------------------

data_t calculate_all_income( dque_t & Q, 
                             data_t   R, 
                             data_t   k )
{
  data_t sum = 0; // Income of all rounds

  // Do for 'R' rounds
  for( loop_t i = 0; i < R; ++i )
    sum += calculate_round_income( Q, k );

  // Return result
  return sum;
}

//--------------------------------------------------------------------------
//! \brief Main entry point of the function.
//! \param argc Number of input arguments.
//! \param argv List of input arguments.
//! \return Error code if any, otherwise 0.
//--------------------------------------------------------------------------

int main( int argc, char ** argv )
{
  loop_t T = 0; // Number of test cases

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
    data_t R = 0; // Number of available rounds
    data_t k = 0; // Number of available seats
    data_t N = 0; // Number of available groups
    dque_t Q;     // Queue of player groups
  
    // Read input datas of current test case
    if( !(std::cin >> R >> k >> N) )
    {
      std::cerr << "Error: Read input datas of case '"
                << i 
                << "' failed !!!" 
                << std::endl;

      return -1;
    }

    // Read addition datas of current test case
    for( loop_t j = 0; j < N; ++j )
    {
      data_t g = 0; // Group size

      // Read size of each group
      if( !(std::cin >> g) )
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
      Q.push_back( g );
    }

    // Process and show the result
    std::cout << "Case #" 
              << i 
              << ": " 
              << calculate_all_income( Q, R, k )
              << std::endl;
  }

  // Successfully return
  return 0;
}

//--------------------------------------------------------------------------
// End of file
//--------------------------------------------------------------------------

