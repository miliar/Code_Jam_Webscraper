/*********************************************************************/
/*                                                                   */
/* Program to solve the "Recycled Numbers" problem, posed for the    */
/* 2012 Google Code Jam. Uses only standard C++ libraries.           */
/*                                                                   */
/* Using gcc, compile as: g++ -o recycled recycled.cpp               */
/*                                                                   */
/* Usage: recycled <input data file> <output file>                   */
/*                                                                   */
/* By Peter Mattsson (peter.mattsson@lineone.net)                    */
/*                                                                   */
/* Licence: Public Domain (or as specified by Google)                */
/*                                                                   */
/*********************************************************************/

#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int num_digits(int number) {
  int digits = 0;
  while (number > 0) {
    digits++;
    number /= 10;
  }
  return digits;
}
  
int main(int argc, const char* argv[]) {
  if (argc != 3) {
    cout << "Usage: " << argv[0] << " <input data file> <output file>\n";
    return 1;
  }
  ifstream input;
  ofstream output;
  int num_inputs;
  int A,B,pairs, start, end;
  int results[7];
  int powers[8];
  for (int n=0; n < 8; n++) {
    powers[n] = pow(10, n);
  }
  input.open(argv[1]);
  output.open(argv[2]);
  if ((!input.is_open()) || (!output.is_open())) return 1;
  input >> num_inputs;
  for (int n = 0; n < num_inputs; n++) {
    input >> A >> B;
    pairs = 0;
    int min_digits = num_digits(A);
    int max_digits = num_digits(B);
    for (int digits = min_digits; digits <= max_digits; digits++) {
      if (digits == min_digits) start = A;
      else start = powers[digits-1];
      if (digits == max_digits) end = B+1;
      else end = powers[digits];
      for (int num = start; num < end; num++) {
	for (int shift = 1; shift < digits; shift++) {
	  int new_num = (num/powers[shift]) + (num%powers[shift])*(powers[digits-shift]);
	  results[shift] = new_num;
	  if ((new_num > num) && (new_num <= B)) {
	    bool newres = true;
	    for (int test = 1; test < shift; test++) {
	      if (results[test] == new_num) {
		newres = false;
		break;
	      }
	    }
	    if (newres) pairs++;
	  }
	}
      }
    }
    output << "Case #" << (n+1) << ": " << pairs << "\n";
  }
  input.close();
  output.close();
  return 0;
}