#include <fstream>
#include <cstring>
#include <cstdlib>
using namespace std;

// calculate exponential
long calExpo (long number, long power);

// main begins here
int main (int argc, char *argv[]) {

  ifstream input  (argv[1]);        // input file
  ofstream output ("snapper_output.txt");   // output file
  
  // Get the no of test cases
  string line;
  getline (input, line);
  int no_of_test_cases = atoi(line.c_str());

  // For all test cases
  for (int index=0; index<no_of_test_cases; index++) {
    getline (input, line);
    int no_of_snappers = atoi(strtok(const_cast<char*>(line.c_str()), " ")); 
    long no_of_triggers = atoi(strtok(NULL, " ")); 
    
    //  cout << "number_of_snappers" << no_of_snappers << endl;
    long wrapping_pos = calExpo (2, no_of_snappers);
    if ( ((no_of_triggers+1) % wrapping_pos) == 0 ) {
      output << "Case #" << index+1 << ": " << "ON" <<endl;
    } else {
      output << "Case #" << index+1 << ": " << "OFF" <<endl;
    }
  }
  return 0;
}

long calExpo (long number, long power) {
  long result;
  if (power >= 2) {
    if (power%2 == 0) {
      result = calExpo(number, power/2) * calExpo(number, power/2);
    } else {
      result = calExpo(number, power/2) * calExpo(number, power/2) * number;
    }
  } else {
    return number;
  }
  return result;
}
