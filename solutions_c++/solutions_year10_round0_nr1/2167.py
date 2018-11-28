
//--------------------------------------------------------------------------
//! \file main.cpp
//! \brief Google Codejam 2010 - 1st round - Snapper Chain.
//--------------------------------------------------------------------------

#include<iostream>
#include<cmath>

//--------------------------------------------------------------------------
//! \brief Is 'K' snaps enough to turn on light bulb for 'N' snapper device.
//! \param N Number of snapper devices.
//! \param K Number of available snaps.
//! \return True if 'K' snaps is enough for 'N' devices, otherwise false.
//--------------------------------------------------------------------------

bool had_enough_snap( size_t N, size_t K )
{
  size_t snap = std::pow( 2, N ); 
  return (K > 0) && !((K + 1) % snap);
}

//--------------------------------------------------------------------------
//! \brief Main entry point of the function.
//! \param argc Number of input arguments.
//! \param argv List of input arguments.
//! \return Error code if any, otherwise 0.
//--------------------------------------------------------------------------

int main( int argc, char ** argv )
{
  size_t T = 0; // Number of test cases

  // Read number of test cases
  if( !(std::cin >> T) )
  {
    std::cerr << "Error: Read number of test cases failed !!!" 
              << std::endl;

    return -1;
  }

  // Process each test case
  for( size_t i = 1; i <= T; ++i )
  {
    size_t K = 0; // Number of available snaps
    size_t N = 0; // Number of devices
  
    // Read input datas of current test case
    if( !(std::cin >> N >> K) )
    {
      std::cerr << "Error: Read input datas of case '"
                << i 
                << "' failed !!!" 
                << std::endl;

      return -1;
    }

    // Process and show the result
    std::cout << "Case #" 
              << i 
              << ": " 
              << (had_enough_snap( N, K ) ? "ON" : "OFF")
              << std::endl;
  }

  // Successfully return
  return 0;
}

//--------------------------------------------------------------------------
// End of file
//--------------------------------------------------------------------------

